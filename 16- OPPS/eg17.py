from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def a1(self):
        pass

    @classmethod
    @abstractmethod
    def a2(cls):
        pass

    @staticmethod
    @abstractmethod
    def a3():
        pass


class ProductImpl(Product):
    def a1(self):
        print("a1 Method")

    @classmethod
    def a2(cls):
        print("a1 Method")

    @staticmethod
    def a3():
        print("a3 Method")


ProductImpl().a1()
ProductImpl().a2()
ProductImpl().a3()
