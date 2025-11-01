# 👻 AI Horror Story Generator

Aplikasi AI generator cerita horror menggunakan Google Gemini AI dan Streamlit dengan tema gelap yang menyeramkan.

## 🚀 Fitur

- Generate cerita horror dengan AI
- Pilihan emosi: Sedih, Senang, Takut, Khawatir, Marah
- Kontrol panjang cerita (100-500 kata)
- Tema UI horror yang menyeramkan
- Powered by Google Gemini AI

## 🛠️ Instalasi Lokal

1. Clone repository ini
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Buat file `.env` dan tambahkan API key:
```
GOOGLE_API_KEY=your_google_api_key_here
```

4. Jalankan aplikasi:
```bash
streamlit run AI-streamlit.py
```

## 🌐 Deploy ke Streamlit Cloud (GRATIS)

### Langkah 1: Push ke GitHub

1. Buat repository baru di GitHub
2. Push kode ke GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/username/repo-name.git
git push -u origin main
```

### Langkah 2: Deploy di Streamlit Cloud

1. Buka [share.streamlit.io](https://share.streamlit.io)
2. Login dengan GitHub
3. Klik "New app"
4. Pilih repository, branch (main), dan file (AI-streamlit.py)
5. Klik "Advanced settings" → "Secrets"
6. Tambahkan secrets:
```toml
GOOGLE_API_KEY = "your_api_key_here"
```
7. Klik "Deploy"!

Aplikasi akan live dalam beberapa menit di URL: `https://username-repo-name.streamlit.app`

## 🔑 Mendapatkan Google API Key

1. Buka [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Login dengan akun Google
3. Klik "Create API Key"
4. Copy API key dan simpan di secrets

## 📦 Dependencies

- streamlit
- google-generativeai
- python-dotenv

## 👨‍💻 Dibuat oleh

Fatih - AI Horror Story Generator

## 📄 Lisensi

MIT License
