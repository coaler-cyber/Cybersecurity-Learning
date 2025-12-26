TARGET="scanme.nmap.org"

echo "🔍 Quét port và dịch vụ trên $TARGET ..."
nmap -sV -O -p 1-1000 $TARGET
