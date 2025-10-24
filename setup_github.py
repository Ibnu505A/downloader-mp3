#!/usr/bin/env python3
"""
Script untuk setup GitHub repository
"""

import os
import subprocess
import sys

def check_git():
    """Cek apakah git sudah terinstall"""
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Git sudah terinstall: {result.stdout.strip()}")
            return True
    except FileNotFoundError:
        print("❌ Git belum terinstall")
        return False

def init_git_repo():
    """Initialize git repository"""
    print("\n🔄 Initializing git repository...")
    try:
        subprocess.run(['git', 'init'], check=True)
        print("✅ Git repository initialized")
        return True
    except subprocess.CalledProcessError:
        print("❌ Gagal initialize git repository")
        return False

def add_files():
    """Add files to git"""
    print("\n🔄 Adding files to git...")
    try:
        subprocess.run(['git', 'add', '.'], check=True)
        print("✅ Files added to git")
        return True
    except subprocess.CalledProcessError:
        print("❌ Gagal add files")
        return False

def commit_files():
    """Commit files"""
    print("\n🔄 Committing files...")
    try:
        subprocess.run(['git', 'commit', '-m', 'Initial commit - YouTube to MP3 Downloader'], check=True)
        print("✅ Files committed")
        return True
    except subprocess.CalledProcessError:
        print("❌ Gagal commit files")
        return False

def show_github_instructions():
    """Show GitHub setup instructions"""
    print("\n" + "="*60)
    print("📋 LANGKAH SELANJUTNYA - SETUP GITHUB")
    print("="*60)
    print("1. Buka https://github.com/")
    print("2. Login ke akun GitHub")
    print("3. Klik 'New repository'")
    print("4. Nama repository: yt-mp3-downloader")
    print("5. Description: YouTube to MP3 Downloader")
    print("6. Pilih 'Public'")
    print("7. JANGAN centang 'Add README'")
    print("8. Klik 'Create repository'")
    print("")
    print("9. Copy URL repository (contoh: https://github.com/username/yt-mp3-downloader.git)")
    print("10. Jalankan command di bawah ini:")
    print("")
    print("git remote add origin https://github.com/username/yt-mp3-downloader.git")
    print("git branch -M main")
    print("git push -u origin main")
    print("")
    print("="*60)

def show_deploy_options():
    """Show deployment options"""
    print("\n" + "="*60)
    print("🚀 PILIHAN DEPLOY KE INTERNET")
    print("="*60)
    print("")
    print("1. RAILWAY (TERMUDAH):")
    print("   - Buka https://railway.app/")
    print("   - Login dengan GitHub")
    print("   - Klik 'New Project'")
    print("   - Pilih repository Anda")
    print("   - Railway auto-deploy!")
    print("")
    print("2. RENDER (GRATIS):")
    print("   - Buka https://render.com/")
    print("   - Login dengan GitHub")
    print("   - Klik 'New Web Service'")
    print("   - Connect repository")
    print("   - Build: pip install -r requirements.txt")
    print("   - Start: python app.py")
    print("")
    print("3. HEROKU (GRATIS dengan limit):")
    print("   - Install Heroku CLI")
    print("   - heroku login")
    print("   - heroku create your-app-name")
    print("   - git push heroku main")
    print("")
    print("="*60)

def main():
    print("🎵 YouTube to MP3 Downloader - GitHub Setup")
    print("=" * 50)
    
    # Cek git
    if not check_git():
        print("\n❌ Install git dulu dari https://git-scm.com/")
        return
    
    # Initialize git
    if not init_git_repo():
        return
    
    # Add files
    if not add_files():
        return
    
    # Commit files
    if not commit_files():
        return
    
    print("\n✅ Git repository berhasil dibuat!")
    
    # Show instructions
    show_github_instructions()
    show_deploy_options()
    
    print("\n🎉 Setup selesai! Sekarang upload ke GitHub dan deploy!")

if __name__ == "__main__":
    main()
