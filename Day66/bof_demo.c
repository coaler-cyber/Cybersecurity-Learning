#include <stdio.h>
#include <string.h>

void secret() {
    printf("✅ Bạn đã chiếm quyền điều khiển! Flag: CTF{pwn_demo_flag}\n");
}

int main() {
    char buffer[50];
    printf("Nhập dữ liệu: ");
    gets(buffer);
    printf("Bạn nhập: %s\n", buffer);
    return 0;
}
