# Multi Level Inheritance
class GrandPranet:
    def a1(self):
        print("Hello")


class Pranet(GrandPranet):
    def a2(self):
        print("Hy")


class Child(Pranet):
    def a3(self):
        print('Hi')


a = Child()
a.a1()
a.a2()
a.a3()
