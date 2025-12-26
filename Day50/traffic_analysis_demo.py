from scapy.all import rdpcap

packets = rdpcap("capture.pcap")  for pkt in packets:
    if pkt.haslayer("TCP") and pkt.haslayer("Raw"):
        data = pkt["Raw"].load.decode(errors="ignore")
        if "password" in data.lower():
            print(f"⚠️ Phát hiện dữ liệu nhạy cảm: {data}")
