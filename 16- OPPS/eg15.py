from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def a1(self):
        pass


Product().a1()  # TypeError: Can't instantiate abstract class Product with abstract method a1
