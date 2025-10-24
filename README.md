# YouTube to MP3 Downloader Web App

Aplikasi web sederhana untuk mendownload audio dari YouTube dalam format MP3 dengan interface yang modern dan user-friendly.

## Fitur

- 🎵 Download audio dari YouTube ke format MP3
- 🚀 Interface web yang modern dan responsif
- 📊 Progress bar real-time
- 🎨 Desain yang menarik dengan gradient
- 📱 Responsive design untuk mobile
- ⚡ Download cepat dengan kualitas tinggi (192kbps)

## Instalasi

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Jalankan aplikasi:**
   ```bash
   python app.py
   ```

3. **Buka browser dan kunjungi:**
   ```
   http://localhost:5000
   ```

## Cara Penggunaan

1. Buka website di browser
2. Masukkan URL YouTube yang ingin didownload
3. Klik tombol "Download MP3"
4. Tunggu proses download selesai
5. File MP3 akan tersimpan di folder `downloads/`

## Struktur File

```
yt_mp3/
├── app.py                 # Flask web application
├── templates/
│   └── index.html        # HTML template
├── downloads/            # Folder untuk menyimpan file MP3
├── requirements.txt      # Dependencies
└── README.md            # Dokumentasi
```

## Requirements

- Python 3.7+
- Flask
- yt-dlp
- FFmpeg (untuk konversi audio)

## Catatan

- Pastikan FFmpeg sudah terinstall di sistem Anda
- Aplikasi ini hanya untuk keperluan pribadi
- Patuhi kebijakan YouTube dan hak cipta

## Troubleshooting

Jika mengalami error:
1. Pastikan FFmpeg sudah terinstall
2. Cek koneksi internet
3. Pastikan URL YouTube valid
4. Cek folder `downloads/` ada dan bisa ditulis

