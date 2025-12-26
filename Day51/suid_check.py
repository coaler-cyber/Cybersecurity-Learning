import os

print("🔍 Kiểm tra file SUID trong hệ thống:")
for root, dirs, files in os.walk("/"):
    for f in files:
        try:
            path = os.path.join(root, f)
            if os.stat(path).st_mode & 0o4000:
                print(f"✅ File SUID: {path}")
        except Exception:
            pass
