#!/usr/bin/env python3
import os
import sys
import time
import webbrowser
from urllib.parse import quote_plus

GREEN = "\033[92m"
DARK_GREEN = "\033[32m"
RED = "\033[91m"
WHITE = "\033[97m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

EYE = [
r"              .-""""""""-.",
r"           .-'            '-.",
r"         .'    .--------.    '.",
r"        /    .'          '.    \\",
r"       /    /    .----.    \\    \\",
r"      ;    ;    /  " + RED + "██" + GREEN + r"  \\    ;    ;",
r"      |    |   |  " + RED + "●●" + GREEN + r"  |   |    |",
r"      ;    ;    \\  " + RED + "██" + GREEN + r"  /    ;    ;",
r"       \\    \\    '----'    /    /",
r"        \\    '.          .'    /",
r"         '.    '--------'    .'",
r"           '-.            .-'",
r"              '-.______.-'",
]

PLATFORMS = {
    "1": ("GitHub", "https://github.com/search?q={q}&type=users"),
    "2": ("TikTok", "https://www.google.com/search?q=site%3Atiktok.com%2F%40+{q}"),
    "3": ("Instagram", "https://www.google.com/search?q=site%3Ainstagram.com+{q}"),
    "4": ("Facebook", "https://www.google.com/search?q=site%3Afacebook.com+{q}"),
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear_screen()
    print(GREEN + BOLD)
    for line in EYE:
        print(line)
    print(RESET)
    print(GREEN + BOLD + "                 XOSINT V2" + RESET)
    print(DARK_GREEN + "                 new updates" + RESET)
    print(GREEN + "        Public Social Profile Search Helper" + RESET)
    print()

def dashboard():
    print(GREEN + BOLD + "  [1] " + RESET + WHITE + "Cari akun sosmed" + RESET)
    print(GREEN + BOLD + "  [2] " + RESET + WHITE + "Keluar" + RESET)
    print()

def choose_platform():
    print(CYAN + "\nPilih platform:" + RESET)
    print("  [1] GitHub")
    print("  [2] TikTok")
    print("  [3] Instagram")
    print("  [4] Facebook")
    print("  [0] Kembali")
    while True:
        choice = input("\nPilih nomor > ").strip()
        if choice == "0":
            return None
        if choice in PLATFORMS:
            return PLATFORMS[choice]
        print(RED + "Pilihan tidak valid. Pilih 1-4 atau 0." + RESET)

def search_flow():
    platform = choose_platform()
    if not platform:
        return
    name = input("\nMasukkan nama atau username yang ingin dicari: ").strip()
    if not name:
        print(RED + "Nama/username tidak boleh kosong." + RESET)
        input("\nTekan Enter untuk kembali ke dashboard...")
        return
    label, template = platform
    query = quote_plus(name)
    url = template.format(q=query)
    print()
    print(GREEN + f"Platform : {label}" + RESET)
    print(WHITE + f"Kata kunci: {name}" + RESET)
    print(CYAN + "\nMembuka pencarian publik di browser..." + RESET)
    print(GREEN + url + RESET)
    try:
        opened = webbrowser.open(url)
    except Exception:
        opened = False
    if not opened:
        print(WHITE + "\nBrowser tidak terbuka otomatis. Salin URL di atas ke browser." + RESET)
    print("\nCatatan: hasil yang namanya mirip belum tentu orang yang sama.")
    input("\nTekan Enter untuk kembali ke dashboard...")

def main():
    while True:
        banner()
        dashboard()
        choice = input("Pilih menu > ").strip()
        if choice == "1":
            search_flow()
        elif choice == "2":
            print(GREEN + "\nSesi XOSINT V2 selesai. Sampai jumpa!" + RESET)
            break
        else:
            print(RED + "\nPilihan tidak valid. Masukkan 1 atau 2." + RESET)
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(RESET + "\nKeluar dari XOSINT V2.")
        sys.exit(0)
