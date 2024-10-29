class READER:
    def __init__(self, name, number, date_of_birth):
        self.name = name
        self.number = number
        self.date_of_birth = date_of_birth
        self.read_books = []
        self.current_books = []

    def add_book(self, book):
        self.current_books.append(book)

    def return_book(self, book):
        if book in self.current_books:
            self.current_books.remove(book)
            self.read_books.append(book)
        else:
            print(f"{book} не знайдено у списку поточних книг.")

    def show_current_books(self):
        print(f"Поточні книги у {self.name}: {', '.join(self.current_books) if self.current_books else 'Немає книг'}")

    def show_read_books(self):
        print(f"Прочитані книги у {self.name}: {', '.join(self.read_books) if self.read_books else 'Немає книг'}")
