import socket
import urllib.request

def get_public_ip():
    try:
        # درخواست به یک سرویس رایگان برای گرفتن IP عمومی
        with urllib.request.urlopen('https://api.ipify.org?format=text', timeout=5) as response:
            return response.read().decode().strip()
    except Exception as e:
        return f"نمیتونم IP عمومی رو بگیرم (ممکنه فیلتر باشه یا اینترنت قطع): {e}"

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return f"خطا در IP داخلی: {e}"

if __name__ == "__main__":
    public_ip = get_public_ip()
    local_ip = get_local_ip()
    
    print(f"🌍 IP عمومی (برای دسترسی از بیرون): {public_ip}")
    print(f"🏠 IP داخلی (در شبکه خودت): {local_ip}")
    print("\n⚠️ نکته مهم: اگر IP عمومی‌ت با IP داخلی‌ت فرق داره، یعنی پشت NAT هستی.")
    print("برای دسترسی از بیرون، باید پورت سرورت (مثلا 8000) رو روی مودم Forward کنی.")
