#include <stdio.h>
#include <string.h>

int main() {
    char password[20];
    printf("Nhập mật khẩu: ");
    scanf("%19s", password);

    if(strcmp(password, "secret123") == 0) {
        printf("✅ Đăng nhập thành công!\n");
    } else {
        printf("❌ Sai mật khẩu!\n");
    }
    return 0;
}
