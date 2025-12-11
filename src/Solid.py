from abc import ABC, abstractmethod

# S - Single Responsibility Principle
# O - Open / Closed Principle
# L
# I
# D


# S - Single Responsibility Principle

# Code that does not follow SRP

# class UserManager:


#     def create_user(self , name):

#         self.name = name
#         print(f"Creating User {name}")

#     def save_to_db(self):

#         print(f"Saving {self.name} to database")

# Code that follows SRP


class UserManager:

    def __init__(self, name):

        self.name = name

    def create_user(self):

        print(f"User {self.name} has been created")


class UserRepository:

    def __init__(self, name):

        self.name = name

    def save_to_db(self):

        print(f"Saving {self.name} to database")


manager = UserManager("Alice")
manager.create_user()

userRepo = UserRepository("John")
userRepo.save_to_db()


# Old / Closed Principle (OCP)


# Defining the Base class to implement inheritance


class PaymentProcess(ABC):

    @abstractmethod
    def processPayment(self, **kwargs):

        pass


class CreditCardPaymentProcess(PaymentProcess):

    def processPayment(self, amount, cardNo):

        print(f"{amount} has been paid from card with number: {cardNo}")


class PayPalPaymentProcess(PaymentProcess):

    def processPayment(self, amount, PaypalId):

        print(f"{amount} has been paid from PayPal with id: {PaypalId}")


ccpayment = CreditCardPaymentProcess()
ccpayment.processPayment(100, "19873")

paypalpayment = PayPalPaymentProcess()
paypalpayment.processPayment(500, "PP123")


# Liskov Substituition Principle (LSP)

# LSP violating code


class Rectangle:

    def __init__(self, w, h):

        self.width = w
        self.height = h

    def area(self):

        return self.width * self.height


class Square(Rectangle):

    def __init__(self, size):

        super().__init__(size, size)
        self.size = size

    def area(self):

        rectArea = super().area()
        # Does not replicate Rectangle behaviour
        print(f"rect area: {rectArea}")

        return self.size * self.size


sq = Square(5)
sqArea = sq.area()
print("sq Area:", sqArea)


# 4. Interface Segregation Problem


# 1. Interfaces
class IVegetarianMenu(ABC):

    @abstractmethod
    def getVegetarianItems(self):
        pass


class INonVegetarianMenu(ABC):

    @abstractmethod
    def getNonVegetarianItems(self):
        pass


class IDrinkMenu(ABC):

    @abstractmethod
    def getDrinkItems(self):
        pass


# 2. Implementations


class VegetarianMenu(IVegetarianMenu):
    def getVegetarianItems(self):
        return ["Vegetable Curry", "Paneer Tikka", "Salad"]


class NonVegetarianMenu(INonVegetarianMenu):
    def getNonVegetarianItems(self):
        return ["Chicken Curry", "Fish Fry", "Mutton Biryani"]


class DrinkMenu(IDrinkMenu):
    def getDrinkItems(self):
        return ["Water", "Soda", "Juice"]


# 3. Display functions


def displayVegetarianItems(menu):
    print("Vegetarian Menu:")
    for item in menu.getVegetarianItems():
        print(f"- {item}")


def displayNonVegetarianItems(menu):
    print("Non-Vegetarian Menu:")
    for item in menu.getNonVegetarianItems():
        print(f"- {item}")


# 4. Main function


def main():
    vegMenu = VegetarianMenu()
    nonVegMenu = NonVegetarianMenu()

    displayVegetarianItems(vegMenu)
    displayNonVegetarianItems(nonVegMenu)


if __name__ == "__main__":
    main()
