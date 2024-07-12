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
    if n.reservation:
        print(f'Название: {n.title}, Автор: {n.autor}, страниц: {n.page_count},'
              f'материал: {n.page_material}, зарезервирована')
    else:
        print(f'Название: {n.title}, Автор: {n.autor}, страниц: {n.page_count}, '
              f'материал: {n.page_material}')


reservation(book_1)
reservation(book_2)
reservation(book_3)
reservation(book_4)
reservation(book_5)


class StudyBook(Book):

    def __init__(self, title, ISBN, autor, page_count, subject, grade, task):
        super().__init__(title, ISBN, autor, page_count)
        self.subject = subject
        self.grade = grade
        self.task = task


def reservation(n):
    if n.reservation:
        print(f'Название: {n.title}, Автор: {n.autor}, страниц: {n.page_count}, '
              f'предмет: {n.subject}, класс: {n.grade}, зарезервирована')
    else:
        print(f'Название: {n.title}, Автор: {n.autor}, страниц: {n.page_count}, '
              f'предмет: {n.subject}, класс: {n.grade}')


studybook_1 = StudyBook('Алгебра', '03813924', 'Каменский', 458, 'Математика', 5, True)
studybook_2 = StudyBook('Мир вокруг нас', '032984924', 'Колумб', 400, 'География', 9, True)
studybook_3 = StudyBook('Есстествознание', '34857924', 'Пифагор', 998, 'Социология', 3, False)
studybook_2.reservation = True
reservation(studybook_2)
reservation(studybook_1)
reservation(studybook_3)
