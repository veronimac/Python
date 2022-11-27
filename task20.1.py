"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""
class Duck:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print('Quack')
    def clothes(self):
        print("I don't wear clothes.")


class Human:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print('I can quack')
    def clothes(self):
        print("I'm wearing clothes.")

duck1 = Duck(2)
human1 = Human(6)
for i in [duck1, human1]:
    i.sound()
    i.clothes()