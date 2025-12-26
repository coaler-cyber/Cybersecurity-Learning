# Pentest Report - Day45

## Executive Summary
Trong quá trình pentest, chúng tôi phát hiện một số lỗ hổng quan trọng cần khắc phục.

## Scope
- Hệ thống: Web Application `example.com`
- Thời gian: 20–25/12/2025

## Findings
### 1. SQL Injection
- **Severity**: High
- **Description**: Input không được lọc, cho phép chèn SQL.
- **PoC**: `' OR '1'='1`
- **Recommendation**: Dùng parameterized queries, escape input.

### 2. FTP Anonymous Login
- **Severity**: Medium
- **Description**: Cho phép đăng nhập anonymous vào FTP.
- **Recommendation**: Tắt anonymous login, dùng SFTP.

## Conclusion
Hệ thống tồn tại lỗ hổng nghiêm trọng. Cần khắc phục ngay để giảm nguy cơ bị tấn công.
