import os
import sys
import time
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import logging

# ========== CONFIG ==========
KEY = b'YuvaPrasathSafe1'  # ✅ Exactly 16 bytes
BLOCK_SIZE = AES.block_size
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
log_file = os.path.join(LOG_DIR, f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# ========== UTILS ==========
def pad(data):
    pad_len = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([pad_len]) * pad_len

def unpad(data):
    return data[:-data[-1]]

def is_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()
        return True
    except:
        return False

def colorize(text, color):
    colors = {
        "green": "\033[92m",
        "red": "\033[91m",
        "yellow": "\033[93m",
        "cyan": "\033[96m",
        "bold": "\033[1m",
        "end": "\033[0m"
    }
    return f"{colors.get(color, '')}{text}{colors['end']}"

# ========== ENCRYPT ==========
def encrypt_image(path):
    try:
        if not is_image(path):
            print(colorize("[✘] Invalid image file.", "red"))
            return
        with open(path, 'rb') as f:
            raw_data = f.read()
        iv = get_random_bytes(BLOCK_SIZE)
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(pad(raw_data))
        enc_path = path + ".enc"
        with open(enc_path, 'wb') as ef:
            ef.write(iv + encrypted)
        print(colorize(f"[✔] Encrypted → {enc_path}", "green"))
        logging.info(f"Encrypted: {path}")
    except Exception as e:
        print(colorize(f"[✘] Encryption failed: {e}", "red"))
        logging.error(f"Encryption error: {e}")

# ========== DECRYPT ==========
def decrypt_image(path):
    try:
        if not path.endswith(".enc"):
            print(colorize("[✘] File must end with .enc", "red"))
            return
        with open(path, 'rb') as f:
            data = f.read()
        iv, enc = data[:BLOCK_SIZE], data[BLOCK_SIZE:]
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(enc))
        out_path = path.replace(".enc", ".decrypted.jpg")
        with open(out_path, 'wb') as df:
            df.write(decrypted)
        print(colorize(f"[✔] Decrypted → {out_path}", "green"))
        logging.info(f"Decrypted: {path}")
    except Exception as e:
        print(colorize(f"[✘] Decryption failed: {e}", "red"))
        logging.error(f"Decryption error: {e}")

# ========== INTERACTIVE MODE ==========
def interactive_mode():
    print(colorize("\n[+] Interactive Mode Enabled", "cyan"))
    action = input("Do you want to (e)ncrypt or (d)ecrypt?: ").strip().lower()
    path = input("Enter full path to file: ").strip()
    if not os.path.exists(path):
        print(colorize("[✘] File not found.", "red"))
        return
    if action.startswith("e"):
        encrypt_image(path)
    elif action.startswith("d"):
        decrypt_image(path)
    else:
        print(colorize("[✘] Invalid choice. Use 'e' or 'd'.", "red"))

# ========== BANNER ==========
def print_banner():
    print(colorize("="*65, "bold"))
    print(colorize("	IMAGE ENCRYPTION TOOL – Secure Your Visual Data", "cyan"))
    print("	Developed by Yuva Prasath")
    print("	Date:", datetime.now().strftime("%Y-%m-%d"))
    print(colorize("="*65, "bold"))

def print_usage():
    print("\nUsage:")
    print("  python image_encryptor.py encrypt <image.jpg>")
    print("  python image_encryptor.py decrypt <image.jpg.enc>")
    print("  python image_encryptor.py  # (for interactive mode)\n")

# ========== MAIN ==========
def main():
    print_banner()
    args = sys.argv

    if len(args) == 1:
        interactive_mode()
        return

    if len(args) != 3:
        print(colorize("[✘] Invalid number of arguments.", "red"))
        print_usage()
        return

    action, file_path = args[1].lower(), args[2]

    if not os.path.exists(file_path):
        print(colorize(f"[✘] File not found: {file_path}", "red"))
        return

    if action == "encrypt":
        encrypt_image(file_path)
    elif action == "decrypt":
        decrypt_image(file_path)
    else:
        print(colorize(f"[✘] Unknown action: {action}", "red"))
        print_usage()

if __name__ == "__main__":
    main()

