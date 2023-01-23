from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def __init__(self):
        pass


class ProductImpl(Product):

    def __init__(self):
        print("Spical Method")


ProductImpl()
