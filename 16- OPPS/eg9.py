# Single level Inheritance

class Parent:
    def a1(self):
        print("Hello")


class Child(Parent):
    def a2(self):
        print('Hy')


a = Child()
a.a1()
a.a2()
