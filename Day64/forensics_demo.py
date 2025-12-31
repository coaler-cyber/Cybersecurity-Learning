def find_flag(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    for line in lines:
        if "CTF{" in line:
            print(f"✅ Flag tìm thấy: {line.strip()}")

if __name__ == "__main__":
    sample_log = "Day64/sample.log"
    with open(sample_log, "w") as f:
        f.write("2025-12-31 10:00 User login success\n")
        f.write("2025-12-31 10:05 Suspicious activity detected\n")
        f.write("2025-12-31 10:10 Flag: CTF{forensics_demo_flag}\n")

    find_flag(sample_log)
