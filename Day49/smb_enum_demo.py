from impacket.smbconnection import SMBConnection

target = "192.168.1.10"  
user = "guest"
password = ""

try:
    conn = SMBConnection(target, target)
    conn.login(user, password)
    shares = conn.listShares()
    for share in shares:
        print(f"✅ Tìm thấy share: {share['shi1_netname']}")
except Exception as e:
    print(f"❌ Lỗi kết nối SMB: {e}")
