#include <stdio.h>
#include <string.h>

int main() {
    char buf[10];
    printf("Nhập chuỗi: ");
    gets(buf); // ❌ không kiểm tra độ dài input
    printf("Bạn nhập: %s\n", buf);
    return 0;
}
