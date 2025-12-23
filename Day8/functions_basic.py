import math

def circle_area(radius):
    return math.pi * radius**2

def circle_perimeter(radius):
    return 2 * math.pi * radius

r = float(input("Nhập bán kính hình tròn: "))
print("Diện tích hình tròn:", circle_area(r))
print("Chu vi hình tròn:", circle_perimeter(r))
