#!/usr/bin/env python3
"""
Script deployment untuk YouTube to MP3 Downloader
Mendukung multiple deployment options
"""

import os
import sys
import subprocess
import webbrowser
import time
from threading import Thread

def check_dependencies():
    """Cek dependencies yang diperlukan"""
    print("🔍 Mengecek dependencies...")
    
    required_packages = ['flask', 'yt-dlp', 'werkzeug']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package}")
    
    if missing_packages:
        print(f"\n📦 Installing missing packages...")
        for package in missing_packages:
            subprocess.run([sys.executable, '-m', 'pip', 'install', package])
    
    return len(missing_packages) == 0

def get_network_info():
    """Dapatkan informasi jaringan"""
    import socket
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"

def show_access_info(ip, port):
    """Tampilkan informasi akses"""
    print("\n" + "="*60)
    print("🎉 YouTube to MP3 Downloader - READY!")
    print("="*60)
    print(f"📱 AKSES DARI HP:")
    print(f"   URL: http://{ip}:{port}")
    print(f"   Pastikan HP dan komputer dalam WiFi yang sama")
    print("")
    print(f"💻 AKSES DARI KOMPUTER LAIN:")
    print(f"   URL: http://{ip}:{port}")
    print(f"   Pastikan dalam jaringan yang sama")
    print("")
    print(f"🏠 AKSES LOKAL:")
    print(f"   URL: http://localhost:{port}")
    print("")
    print("📋 CARA SHARE KE TEMAN:")
    print(f"   1. Kirim URL: http://{ip}:{port}")
    print(f"   2. Pastikan teman dalam WiFi yang sama")
    print(f"   3. Atau gunakan ngrok untuk akses internet")
    print("")
    print("🔧 TROUBLESHOOTING:")
    print("   - Jika tidak bisa akses, cek firewall")
    print("   - Matikan antivirus sementara")
    print("   - Pastikan port tidak diblokir")
    print("="*60)

def start_server():
    """Start Flask server"""
    from app import app
    
    local_ip = get_network_info()
    port = 5000
    
    show_access_info(local_ip, port)
    
    print("🚀 Starting server...")
    print("📋 Tekan Ctrl+C untuk stop")
    
    try:
        app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
    except KeyboardInterrupt:
        print("\n🛑 Server dihentikan")

def main():
    print("🎵 YouTube to MP3 Downloader - Deployment Script")
    print("=" * 50)
    
    # Cek dependencies
    if not check_dependencies():
        print("❌ Ada masalah dengan dependencies")
        return
    
    # Pastikan folder downloads ada
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
        print("📁 Membuat folder downloads")
    
    # Start server
    start_server()

if __name__ == "__main__":
    main()
