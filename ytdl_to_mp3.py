import yt_dlp

def youtube_to_mp3(url, output_folder="downloads"):
    ydl_opts = {
        'format': 'bestaudio/best',   # Ambil audio kualitas terbaik
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Nama file dari judul video
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Konversi audio
            'preferredcodec': 'mp3',      # Format MP3
            'preferredquality': '192',    # Bitrate 192kbps
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Masukkan URL YouTube: ")
    youtube_to_mp3(video_url)
    print("✅ Selesai! File MP3 ada di folder 'downloads'")
