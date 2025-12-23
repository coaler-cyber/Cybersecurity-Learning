def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Không thể chia cho 0!"
    return a / b

x = float(input("Nhập số thứ nhất: "))
y = float(input("Nhập số thứ hai: "))

print("Kết quả cộng:", add(x, y))
print("Kết quả trừ:", subtract(x, y))
print("Kết quả nhân:", multiply(x, y))
print("Kết quả chia:", divide(x, y))
