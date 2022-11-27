"""
Создайте композицию User состояющую из:
Объекта Profile со свойствами: name,last_name,age,pasport и методом print_info.
Объекта Address со свойствами : City,street,zipcode
Объекта Role со свойствами: role,hours_worked
Объекта BankAccount со свойствами: card_number, balance
Объекта Order с методом устанавливающими параметры заказа: Item,date,delivery,price
Добавьте в композицию методы создания профиля, установки адреса, роли, привязки банковского аккаунта и добавления заказа
"""

class Profile:
    def __init__(self, name, last_name, age, pasport):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.pasport = pasport

    def print_info(self):
        print(self.name, self.last_name, self.age, self.pasport)


class Address:
    def __init__(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode

class Role:
    def __init__(self, role, hours_worked):
        self.role = role
        self.hours_worked = hours_worked

class BankAccount:
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance

class Order:
    def __init__(self, item, price, date, delivery):
        self.item = item
        self.price = price
        self.date = date
        self.delivery = delivery

    def create_order(self):
        print(self.item, self.date, self.delivery, self.price)

class User:
    def __init__(self, profile, role):
        self.profile = profile
        self.role = role
        self.address = []
        self.bank_ac = []
        self.order = []

    def new_profile(self, name, last_name, age, pasport):     #метод класса User
        self.profile = Profile(name, last_name, age, pasport) #экземпляр класса профиль

    def your_address(self, city, street, zipcode):
        self.address.append(Address(city, street, zipcode))

    def create_role(self, role, hours_worked):
        self.role = Role(role, hours_worked)

    def create_bank_account(self, card_number, balance):
        self.bank_ac = BankAccount(card_number, balance)

    def create_order(self, item, price, date, delivery):
        self.order = Order()
        self.order.set_all(item, price, date, delivery)


user1 = User(None, None)
user1.new_profile('Лиза', 'Иванова', 20, 232442526)
user1.your_address('Сочи', 'Ленина', 1234)


print(user1.profile.name, user1)
print(user1.address[0].city)



