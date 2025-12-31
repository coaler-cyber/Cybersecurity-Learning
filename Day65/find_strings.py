import subprocess

binary = "Day65/re_ctf_demo"
result = subprocess.run(["strings", binary], capture_output=True, text=True)
print("🔍 Các chuỗi tìm thấy trong binary:")
print(result.stdout)
