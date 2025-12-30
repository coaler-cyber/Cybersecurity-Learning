def analyze_log(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    for line in lines:
        if "Failed login" in line:
            print(f"⚠️ Phát hiện đăng nhập thất bại: {line.strip()}")
        if "DELETE" in line:
            print(f"❌ Phát hiện hành vi xóa dữ liệu: {line.strip()}")

if __name__ == "__main__":
    sample_log = "Day57/sample.log"
    with open(sample_log, "w") as f:
        f.write("2025-12-30 10:00 Failed login from 192.168.1.5\n")
        f.write("2025-12-30 10:05 DELETE /important/data.txt\n")
    analyze_log(sample_log)
