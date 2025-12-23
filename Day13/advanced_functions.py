def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("Tổng các số:", sum_numbers(1, 2, 3, 4, 5))
print("\nThông tin người dùng:")
show_info(name="Giang", age=25, city="Hà Nội")
