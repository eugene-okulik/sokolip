class Book:
    text = True
    page_material = 'paper'

    def __init__(self, title, ISBN, autor, page_count):
        self.title = title
        self.ISBN = ISBN
        self.autor = autor
        self.page_count = page_count
        self.reservation = False


book_1 = Book('Война и мир', '123456', 'Достоевский', 250)
book_2 = Book('Братья Карамазовы', '135790', 'Достоевский', 234)
book_3 = Book('Незнайка на луне', '987654', 'Носов', 1240)
book_4 = Book('Колобок', '5676428', 'Народ', 5)
book_5 = Book('1984', '15738296', 'Оруэл', 415)
book_1.reservation = True

def reservation(n):
    if n.reservation == True:
        print(f'Название: {book_1.title}, Автор: {book_1.autor}, страниц: {book_1.page_count}, '
      f'материал: {book_1.page_material}, зарезервирована')
    else:
        print(f'Название: {book_1.title}, Автор: {book_1.autor}, страниц: {book_1.page_count}, '
      f'материал: {book_1.page_material}')

reservation(book_1)
reservation(book_2)
reservation(book_3)
reservation(book_4)
reservation(book_5)