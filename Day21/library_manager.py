class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def info(self):
        return f"{self.title} - {self.author}"

class Library:
    def __init__(self):
        self.__books = []  
    
    def add_book(self, book):
        self.__books.append(book)
        print(f"Đã thêm sách: {book.info()}")
    
    def remove_book(self, title):
        for book in self.__books:
            if book.title == title:
                self.__books.remove(book)
                print(f"Đã xóa sách: {title}")
                return
        print("Không tìm thấy sách cần xóa.")
    
    def show_books(self):
        if not self.__books:
            print("Thư viện trống.")
        else:
            print("Danh sách sách trong thư viện:")
            for book in self.__books:
                print("-", book.info())

library = Library()

while True:
    print("\n--- Quản lý Thư viện ---")
    print("1. Thêm sách")
    print("2. Xóa sách")
    print("3. Hiển thị danh sách sách")
    print("4. Thoát")

    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        title = input("Nhập tên sách: ")
        author = input("Nhập tác giả: ")
        new_book = Book(title, author)
        library.add_book(new_book)
    elif choice == "2":
        title = input("Nhập tên sách muốn xóa: ")
        library.remove_book(title)
    elif choice == "3":
        library.show_books()
    elif choice == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập 1-4.")
