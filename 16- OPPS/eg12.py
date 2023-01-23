# Hierarchical Inheritance
class GrandPranet:
    def a1(self):
        print("Hello")


class Pranet(GrandPranet):
    def a2(self):
        print("Hy")


class Child(GrandPranet):
    def a3(self):
        print('Hi')


a = Child()
a.a1()
a.a3()

b = Pranet()
b.a1()
b.a2()