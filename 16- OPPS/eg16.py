from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def a1(self):
        pass

    @abstractmethod
    def a2(self):
        pass


class ProductImpl(Product):
    def a1(self):
        print("Hello....")

    def a2(self):
        print("Hy....")


ProductImpl().a1()
ProductImpl().a2()
