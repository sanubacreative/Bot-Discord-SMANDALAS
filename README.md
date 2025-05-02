# Discord Bot Sejarah SMAN 12 Semarang

Bot ini menyapa anggota baru, menjawab perintah /hello, /pengumuman, /materi, /bertanya_paknastain, /motivasi, dan /pantun.

## Cara Jalankan
1. Buat file `.env` berisi:
    DISCORD_TOKEN=MASUKKAN_TOKEN_DISCORD_KAMU
2. Install dependencies:
    pip install -r requirements.txt
3. Jalankan bot:
    python bot.py

## Deploy ke Render
- Upload ke GitHub
- Buat Web Service baru
- Runtime: Python
- Start Command: `python bot.py`
- Tambahkan Environment Variable `DISCORD_TOKEN`