TARGET="scanme.nmap.org"

echo "🔍 Đang quét $TARGET ..."
nmap -sV $TARGET
