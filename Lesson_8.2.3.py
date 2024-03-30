"""Задание 3

Описать абстрактный класс Transport:
- атрибут brand - фирма, выпустившая транспорт (тип - str)
- атрибут model - модель (тип - str)
- атрибут issue_year - год выпуска (тип - int)
- атрибут color - цвет (тип - str)
- атрибут mileage - пробег (тип - int)
- магический метод __init__, который принимает brand, model, issue_year и color, а mileage устанавливает значение 0
- абстрактный метод move, который принимает num_km - количество километров, которое должен пройти транспорт.
Метод проверяет, чтобы num_km было больше 0 и увеличивает mileage на значение num_km. 
Если num_km меньше 0, то бросить исключение ValueError("Расстояние должно быть положительным числом")


Описать класс Car, который наследуется от Transport:
- атрибут engine_type - тип двигателя (тип str)
- магический метод __init__, который принимает brand, model, issue_year и color и engine_type
- переопределить метод move. Внутри метода вызвать родительский метод.
Потом вернуть строку "{brand} {model} ({color} - {issue_year}) проехала {km} километров"


Описать класс Airplane, который наследуется от Transport:
- атрибут lifting_capacity - грузоподъемность (тип - int)
- магический метод __init__, который принимает brand, model, issue_year и color и lifting_capacity
- переопределить метод move. 
Внутри метода вызвать родительский метод, а потом вернуть строку "{brand} {model} ({color} - {issue_year}) пролетел {km} километров"

"""


#Создаём родительский класс Транспорт, задаём аттрибуты
from abc import ABC, abstractmethod
class Transport(ABC):
    def __init__(
        self, 
        brand: str, 
        model: str, 
        issue_year: int, 
        color: str, 
        mileage: int
        ):
            self.brand = brand
            self.model = model
            self.issue_year = issue_year
            self.color = color
            self.mileage = 0
    

#Абстрактный метод для потомков
    @abstractmethod
    def move(self, num_km: int):
        if num_km > 0:
            self.mileage += num_km
        else:
            raise ValueError("Расстояние должно быть положительным числом")
            

#Создаём подкласс Автомобиля с новым аттрибутом
class Car(Transport):
    def __init__(
    self, 
    brand, 
    model, 
    issue_year, 
    color, 
    engine_type: str
    ):
        super().__init__(brand, model, issue_year, color, mileage=0)      #обращаемся к родительским аттрибутам и назначаем новый
        self.engine_type = engine_type
        
        
    def move(self, num_km):
        super().move(num_km)                                              #обращаемся к родительскому методу и формируем ответ функции
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) проехала {self.mileage} километров на {self.engine_type} двигателе."


#Создаём класс Самолётов с новым аттрибутом, аналогично классу Автомобилей
class Airplane(Transport):
    def __init__(
    self, 
    brand, 
    model, 
    issue_year, 
    color, 
    lifting_capacity: int
    ):
        super().__init__(brand, model, issue_year, color, mileage=0)
        self.lifting_capacity = lifting_capacity
        
        
    def move(self, num_km):
        super().move(num_km)
        return f"{self.brand} {self.model} ({self.color} - {self.issue_year}) грузоподъёмностью {self.lifting_capacity} кг, проетел {self.mileage} километров."        
            

#Основная программа, инициализируем объекты подклассов
if __name__ == '__main__':
    car_1 = Car("Toyota", "Celica", 1993, "Black", "Petrol")
    car_2 = Car("BMW", "E46", 2003, "Silver", "Diesel")
    plane_1 = Airplane("Concorde", "№001", 1969, "White", 20000)
    plane_2 = Airplane("Colt", "Annushka", 1947, "Camouflage", 2000)
    


#Пример работы программы
print(car_1.move(100))         #Вывод: Toyota Celica (Black - 1993) проехала 100 километров на Petrol двигателе.
print(car_1.move(588000))      #Вывод: Toyota Celica (Black - 1993) проехала 588100 километров на Petrol двигателе.
print(car_2.move(312000))      #Вывод: BMW E46 (Silver - 2003) проехала 312000 километров на Diesel двигателе.
print(car_2.move(26000))       #Вывод: BMW E46 (Silver - 2003) проехала 338000 километров на Diesel двигателе.
print(plane_1.move(30))        #Вывод: Concorde №001 (White - 1969) грузоподъёмностью 20000 кг, проетел 30 километров.
print(plane_1.move(22222))     #Вывод: Concorde №001 (White - 1969) грузоподъёмностью 20000 кг, проетел 22252 километров.
print(plane_2.move(1001001))   #Вывод: Colt Annushka (Camouflage - 1947) грузоподъёмностью 2000 кг, проетел 1001001 километров.
print(plane_2.move(50000))     #Вывод: Colt Annushka (Camouflage - 1947) грузоподъёмностью 2000 кг, проетел 1051001 километров.
# print(car_2.move(0))         #Можно разкомментить, проверить выброс ошибки (строка кода 55).
