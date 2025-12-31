#include <stdio.h>
#include <string.h>

int main() {
    char input[50];
    printf("Nhập flag: ");
    scanf("%49s", input);

    if(strcmp(input, "CTF{reverse_demo_flag}") == 0) {
        printf("✅ Chính xác! Bạn đã tìm thấy flag.\n");
    } else {
        printf("❌ Sai flag!\n");
    }
    return 0;
}
