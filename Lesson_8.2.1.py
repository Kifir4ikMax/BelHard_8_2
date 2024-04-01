"""Задание 1

Блок 1: 
Создать класс BookCard, в классе должны быть:
- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
Блок 2:
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year.
В сеттерах сделать проверку на тип данных, если тип данных не подходит, то бросить ValueError.
Для года издания дополнительно проверить на валидность (> 0, <= текущего года).
Аксессоры реализоваться через property.

"""



#Создаём класс для книг по Блоку 1 из Задания 1
class BookCard:
    def __init__(self, author: str, title: str, year: int):
        self.__author = author
        self.__title = title
        self.__year = year


#Создаём функцию для опледеления шаблона представления объектов в классе
    def __repr__(self):
        return f"Title: {self.__title}\nAuthor: {self.__author}\nYear: {self.__year}\n"
        

#Создаём функцию которая проверит актуальность вводимой информации (проверяет год издания) по Блоку 2 из Задания 1
    def __ge__(self, other=2025):
        if self.__year >= other:
            print("***Not a valid book***")  
            return True
        else:
            return False
            
            
    def __le__(self, other=0):
        if self.__year <= other:
            print("***Not a valid book***")  
            return True
        else:
            return False

  
#Добавляем метод сравнения по Блоку 2 из Задания 1
    def __gt__(self, other):
        if self.__year > other:
            return True
        else:
            return False

    
#Добавляем методы извлечения и изменения атрибутов по Блоку 2 из Задания 1
#Геттер и сеттер авторства  
    @property
    def get_author(self):
        return self.__author
        
    def set_author(self, author):                        #для сеттера @propery не получилось исполнить, так как обязательно нужен новый аргумент для замены
        if not isinstance(author, str):
            raise ValueError("Wrong type for 'Author'.")
        else:
            self.__author = author
            return self.__author  
        

#Геттер и сеттер названия книги
    @property
    def get_title(self):
        return self.__title
        
    def set_title(self, title):
        if not isinstance(title, str):
            raise ValueError("Wrong type for 'Title'.")
        else:
            self.__title = title
            return self.__title  
    

#Геттер и сеттер года издания книги
    @property
    def get_year(self):
        if 0 > self.__year >= 2025:
            print(f"Invalid year!: {self.__year}")
            return self.__year
        else:    
            return self.__year
    
    def set_year(self, year):
        if not isinstance(year, int):
            raise ValueError("Wrong type for 'Year'.")
        else:    
            self.__year = year
            return self.__year        


#Создаём класс Библиотеки, которая будет хранить Книги в списке    
class Library:
    def __init__(self):
        self.books = []

  
#Проверка подлинности по шаблону из класса Книги и наполнение Библиотеки     
    def __iadd__(self, other):
        if not isinstance(other, BookCard):
            print("Not a book")
        self.books.append(other)
        return self

  
#Метод для представления списка Книг в Библиотеке
    def __repr__(self):
        return self.books

  
#Отмечаем что это будет контейнер
    def __iter__(self):
        return iter(self.books)

  
#Отмечаем что контейнер может быть какой-то длины
    def __len__(self):
        return len(self.books)
        

#Основная программа
if __name__ == '__main__':

    #Добавляем объекты в класс Книг
    book_1 = BookCard(
        "Mark Twain", "The Adventures of Tom Sawyer", 1876
        )
    book_2 = BookCard(
        "Alexander Pushkin", "Ruslan and Ludmila", 1820
        )
    book_3 = BookCard(
        "A.A. Milne", "Winnie-the-Pooh", 1926
        )
    book_4 = BookCard(
        "Kifir", "Python 3", 2025
        )   
    book_5 = BookCard(
        "Zero", "Zeros", 0
        )       
    

    #Добавляем эти Книги в Библиотеку, список книг назовём "shelf"
    lib = Library()
    shelf = lib.__repr__()
    lib += book_1
    lib += book_2
    lib += book_3
    lib += book_4
    lib += book_5


    #Сортируем книжки по году издания "пузырьком"
    iterations = len(shelf) - 1
    for i in range(iterations):
        for j in range(iterations-i):
            if shelf[j].get_year > shelf[j+1].get_year:
                shelf[j], shelf[j+1] = shelf[j+1], shelf[j]

"""Поехали!
Применяем методы, можно разкомментить следующий блок (выводим объекты на экран)"""

# print(book_4.__repr__())
# print(lib.__repr__())
# for book in lib:
#     book.__le__()
#     book.__ge__()
#     print(book)

"""Можно снова закомментить верхний блок"""


"""Применяем аксессоры, можно разкомментить следующий блок (выводим объекты на экран)"""

# print(book_2.get_author)  
# print(book_3.get_year)       
# print(book_5.get_title) 
# print(shelf[3].get_author)       #Можно также обращаться через "shelf[index]"
# print(shelf[4].get_author)
# shelf[4].set_author("MAXIM")
# print(shelf[4].get_author)

"""Можно снова закомментить верхний блок"""


"""Попробуем изменить год издания книжек, можно разкомментить следующий блок"""

# print(shelf)
# print(shelf[4].get_year)
# print(shelf[0].get_year)
# shelf[4].set_year(2024)
# shelf[0].set_year(999)
# print(shelf[4].get_year)
# print(shelf[0].get_year)
# print(shelf)

"""Можно снова закомментить верхний блок"""


"""Внесем пару изменений и снова проверим полку на подлинность книг, можно разкомментить следующий блок"""

# shelf[4].set_year(2024)
# shelf[0].set_year(999)
# for book in lib:
#     book.__le__()
#     book.__ge__()
#     print(book)

"""Конец"""
