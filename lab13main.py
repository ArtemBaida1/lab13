from lab13reader import READER

reader1 = READER("Іванов І.І.", 101, "1995-01-01")
reader2 = READER("Петров П.П.", 102, "1990-05-15")
reader3 = READER("Сидоренко С.С.", 103, "1985-10-20")

reader1.add_book("Сонячні кларнети")
reader1.add_book("Кобзар")

reader2.add_book("1984")
reader2.add_book("Ворошиловград")

reader3.add_book("Дюна")

reader1.show_current_books()
reader2.show_current_books()

reader1.return_book("Сонячні кларнети")

reader3.return_book("Дюна")

reader1.show_read_books()
reader1.show_current_books()
reader3.show_read_books()
