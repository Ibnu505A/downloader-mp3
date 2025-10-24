from flask import Flask, render_template, request, jsonify, send_file, flash, redirect, url_for
import yt_dlp
import os
import threading
import time
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Ganti dengan secret key yang aman

# Global variable untuk tracking download progress
download_progress = {}

def download_video_progress(url, download_id):
    """Fungsi untuk download video dengan progress tracking"""
    try:
        downloaded_filename = None
        
        def progress_hook(d):
            nonlocal downloaded_filename
            if d['status'] == 'downloading':
                if 'total_bytes' in d:
                    percent = (d['downloaded_bytes'] / d['total_bytes']) * 100
                    download_progress[download_id] = {
                        'status': 'downloading',
                        'percent': round(percent, 2),
                        'speed': d.get('speed', 0),
                        'filename': d.get('filename', '')
                    }
                else:
                    download_progress[download_id] = {
                        'status': 'downloading',
                        'percent': 0,
                        'speed': d.get('speed', 0),
                        'filename': d.get('filename', '')
                    }
            elif d['status'] == 'finished':
                downloaded_filename = d['filename']
                download_progress[download_id] = {
                    'status': 'finished',
                    'percent': 100,
                    'filename': d['filename']
                }

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [progress_hook],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        # Cari file MP3 yang baru dibuat
        if downloaded_filename:
            mp3_filename = downloaded_filename.replace('.webm', '.mp3').replace('.m4a', '.mp3')
            if os.path.exists(mp3_filename):
                final_filename = os.path.basename(mp3_filename)
            else:
                final_filename = os.path.basename(downloaded_filename)
        else:
            # Fallback: cari file MP3 terbaru di folder downloads
            import glob
            mp3_files = glob.glob('downloads/*.mp3')
            if mp3_files:
                final_filename = os.path.basename(max(mp3_files, key=os.path.getctime))
            else:
                final_filename = "unknown.mp3"
            
        download_progress[download_id] = {
            'status': 'completed',
            'percent': 100,
            'filename': final_filename,
            'download_url': f'/downloads/{final_filename}'
        }
        
    except Exception as e:
        download_progress[download_id] = {
            'status': 'error',
            'error': str(e)
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list_files')
def list_files():
    """List semua file MP3 yang ada di folder downloads"""
    try:
        import glob
        mp3_files = glob.glob('downloads/*.mp3')
        files_info = []
        for file_path in mp3_files:
            filename = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)
            file_time = os.path.getctime(file_path)
            files_info.append({
                'filename': filename,
                'size': file_size,
                'time': file_time,
                'download_url': f'/downloads/{filename}'
            })
        # Sort by creation time (newest first)
        files_info.sort(key=lambda x: x['time'], reverse=True)
        return jsonify(files_info)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if not url:
        flash('URL tidak boleh kosong!', 'error')
        return redirect(url_for('index'))
    
    # Generate unique download ID
    download_id = str(int(time.time()))
    
    # Start download in background thread
    thread = threading.Thread(target=download_video_progress, args=(url, download_id))
    thread.daemon = True
    thread.start()
    
    return jsonify({'download_id': download_id})

@app.route('/progress/<download_id>')
def progress(download_id):
    if download_id in download_progress:
        return jsonify(download_progress[download_id])
    else:
        return jsonify({'status': 'not_found'})

@app.route('/downloads/<filename>')
def download_file(filename):
    file_path = os.path.join('downloads', filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True, download_name=filename)
    else:
        return jsonify({'error': 'File tidak ditemukan!'}), 404

if __name__ == '__main__':
    # Pastikan folder downloads ada
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    
    app.run(debug=True, host='0.0.0.0', port=5000)
