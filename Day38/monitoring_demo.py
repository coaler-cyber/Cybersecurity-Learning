import time

def monitor_log():
    with open("access.log") as f:
        lines = f.readlines()
        failed_attempts = [line for line in lines if "Đăng nhập thử" in line]
        if len(failed_attempts) > 5:
            print("⚠️ Phát hiện nhiều lần đăng nhập sai liên tiếp!")

if __name__ == "__main__":
    while True:
        monitor_log()
        time.sleep(10)  
