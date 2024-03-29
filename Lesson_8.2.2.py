"""Задание 2

Создать 3 класса:
AmericanPerson, RussianPerson, GermanyPerson
в каждом классе определить метод i_love_science()
AmericanPerson.i_love_science() - "I love science"
RussianPerson.i_love_science() - "Я люблю науку"
GermanyPerson.i_love_science() - "ich liebe Wissenschaft"

Написать функцию person_love_science, которая принимает объект и вызывает метод i_love_science. 
Функция должна возвращать строку вида
"{obj.__class__.__name__} says that: {obj.i_love_science()}"

В блоке if __name__ == "__main__": сделать объекты трех классов и по
очереди передать их в функцию person_love_science.

"""


#Создаём классы
class AmericanPerson:
    def i_love_science(self):
        return "I love science"


class RussianPerson:
    def i_love_science(self):
        return "Я люблю науку"
        
        
class GermanPerson:
    def i_love_science(self):
        return "Ich liebe Wissenschaft"


#Пишем функцию вывода сообщения для "утиных" объектов
def person_love_science(some_man):
    print(f"{some_man.__class__.__name__} says that: {some_man.i_love_science()}")
    
    
if __name__ == '__main__':
    american = AmericanPerson()
    russian = RussianPerson()
    german = GermanPerson()


person_love_science(american)      #Вывод: AmericanPerson says that: I love science
person_love_science(russian)       #Вывод: RussianPerson says that: Я люблю науку
person_love_science(german)        #Вывод: GermanPerson says that: Ich liebe Wissenschaft

