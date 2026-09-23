<!-- Created by Erion Nezha — © 2026 All rights reserved -->
# Telegram QR Bot

Bot Telegram që gjeneron QR code nga çdo tekst që i dërgon. Demoja web gjeneron QR direkt në browser me librarinë qrcode-generator (lokale, pa internet).

## ▶️ Live Demo
Hap `demo/index.html` në browser — ose shiko Live Demo-n në GitHub Pages.

## 📁 Struktura
- `index.html — faqja showcase (Live Demo + Kodi Burim)`
- `demo/index.html — demo web (gjenerues QR)`
- `demo/vendor/qrcode-generator.min.js — libraria qrcode-generator (lokale)`
- `original/qr_-_Bot.py — kodi origjinal Python (i paprekur)`
- `README.md, PROVENANCE_LICENSE.txt`

## 🖥️ Si ekzekutohet origjinali
Kërkon Python + `pip install pyTelegramBotAPI qrcode`. Vendos token-in te `telebot.TeleBot("Token")` dhe ekzekuto me `python qr_-_Bot.py`.

---
Krijuar nga **Erion Nezha** — © 2026
