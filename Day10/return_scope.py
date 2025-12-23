def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

n = int(input("Nhập một số: "))
if is_even(n):
    print(f"{n} là số chẵn.")
else:
    print(f"{n} là số lẻ.")

x = 10  

def demo_scope():
    x = 5  
    print("Giá trị x bên trong hàm:", x)

demo_scope()
print("Giá trị x bên ngoài hàm:", x)
