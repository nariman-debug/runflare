import http.server
import socket
import urllib.request
import os

# تنظیمات
PORT = 8080
FILE_TO_SEND = "example.txt"  # اسم فایلی که میخوای دانلود بشه

# ایجاد فایل
with open(FILE_TO_SEND, 'w') as f:
    f.write('You do it !!!!!!')

def get_public_ip():
    try:
        with urllib.request.urlopen('https://api.ipify.org?format=text', timeout=5) as response:
            return response.read().decode().strip()
    except:
        return "نمیتونم IP عمومی رو بگیرم (ممکنه فیلتر باشه)"

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "خطا در دریافت IP"

if __name__ == "__main__":
    # 1. بررسی وجود فایل
    if not os.path.exists(FILE_TO_SEND):
        print(f"❌ فایل '{FILE_TO_SEND}' پیدا نشد! لطفاً یک فایل با این اسم بساز.")
        exit()

    # 2. گرفتن IPها
    local_ip = get_local_ip()
    public_ip = get_public_ip()

    # 3. ساخت آدرس‌ها
    local_url = f"http://{local_ip}:{PORT}/{FILE_TO_SEND}"
    public_url = f"http://{public_ip}:{PORT}/{FILE_TO_SEND}"

    print(f"🚀 سرور با موفقیت روی پورت {PORT} شروع شد.")
    print(f"🏠 آدرس دانلود در شبکه داخلی: {local_url}")
    print(f"🌍 آدرس دانلود از بیرون (نیاز به تنظیم روتر دارد): {public_url}")
    print("\n⚠️ نکته: اگر از اینترنت موبایل یا شبکه دیگری وصل شدی، باید پورت {PORT} رو روی مودمت فوروارد کنی.")
    print("حالا می‌تونی فایل رو دانلود کنی...")

    # 4. اجرای سرور
    handler = http.server.SimpleHTTPRequestHandler
    with http.server.HTTPServer(("", PORT), handler):
        print(f"✅ سرور در حال اجراست. برای خروج Ctrl+C رو بزن.")
        http.server.HTTPServer(("", PORT), handler).serve_forever()
