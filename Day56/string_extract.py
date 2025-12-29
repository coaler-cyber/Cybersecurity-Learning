import subprocess

binary = "re_demo"
result = subprocess.run(["strings", binary], capture_output=True, text=True)
print("🔍 Các chuỗi tìm thấy trong binary:")
print(result.stdout)
