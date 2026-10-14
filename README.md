<div align="center">

<img src="assets/xosint-logo.png" alt="XOSINT V2 Logo" width="500">

# XOSINT V2
### Public social profile search helper for Android & Termux

[![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Android-3DDC84?style=for-the-badge)](#requirements)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)

**XOSINT V2** helps you search public profile pages on GitHub, TikTok, Instagram, and Facebook.
Made for Android and Termux — Kali Linux is not required.

</div>

> **Important:** Search results are only leads, not identity verification. A matching name or username does not prove that an account belongs to a particular person. Platform search pages may require login, change URLs, or return incomplete results.

## Features

- Android and Termux friendly
- Terminal banner with green ASCII eye and red pupil
- Interactive dashboard:
  - `1` — Cari akun sosmed
  - `2` — Keluar
- Supports GitHub, TikTok, Instagram, and Facebook search
- Opens public search pages in your browser
- Clears the terminal when the app starts
- Press Enter after a search to return to the dashboard
- Uses Python standard library only

## Requirements

- Android with [Termux](https://termux.dev/)
- Python 3.9+
- Internet access

Kali Linux is **not required**.

## Install

```bash
pkg update
pkg install git python -y
git clone https://github.com/ras806790-gif/XOSINT-V2.git
cd xosint-v2
chmod +x xosint.sh
```

## Usage

Start with Bash:

```bash
./xosint.sh
```

Or run Python directly:

```bash
python xosint.py
```

Choose `1` to search public social profiles, select one of the four supported platforms, then enter a name or username. Your browser will open a search page. When you're done, return to the terminal and press Enter to go back to the dashboard.

Choose `2` to exit the session.

## How search works

XOSINT V2 opens a platform search or a web search scoped to the selected platform. It does **not** scrape private data, bypass login, or confirm that a profile belongs to a particular person. Search results depend on the platform, indexing, and the terms entered.

## Project structure

```text
xosint-v2/
├── .github/
│   └── workflows/
│       └── python-check.yml
├── assets/
│   └── xosint-logo.png
├── docs/
│   └── SAFETY.md
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── xosint.py
└── xosint.sh
```

## Responsible use

Use this tool only for lawful research of publicly available information. Respect platform terms, rate limits, and people's privacy. Do not use it for harassment, stalking, doxxing, impersonation, or targeting anyone. XOSINT V2 does not access private accounts, passwords, or hidden data.

See [Safety notes](docs/SAFETY.md).

## Inspired by

- [Sherlock Project](https://github.com/sherlock-project/sherlock)

## SUPPORT DEVELOPER

**TikTok**  
https://www.tiktok.com/@rasyafunix

**Instagram**  
https://www.instagram.com/rasyahgh

**Telegram**  
https://t.me/roxinih

## Contributing

[Contributions and bug reports are welcome. Please keep changes respectful of privacy and platform terms.](https://github.com/sherlock-project/sherlock/graphs/contributors)

## License

MIT. See [LICENSE](LICENSE).
