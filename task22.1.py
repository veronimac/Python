from datetime import date

class Person():
    def __init__(self, name, age): #init - конструктор, (свойства экзепляра)
        self.name = name # свойства
        self.age = age


    def ptintname(self):
        print(self.name, self.age)

    @classmethod
    def classmethod(cls, year):
        return Person("Nastya", date.today().year - year)

    @staticmethod
    def staticmethod(age):
        if age < 18:
            return "no soversh"
        else:
            return "yes soversh"


nastya = (Person.classmethod(2004))
print(nastya.name)
print(nastya.age)
print(nastya.staticmethod(18))