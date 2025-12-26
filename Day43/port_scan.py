import socket

target = "scanme.nmap.org"
ports = [21, 22, 80, 443]

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"✅ Port {port} mở trên {target}")
    else:
        print(f"❌ Port {port} đóng")
    sock.close()
