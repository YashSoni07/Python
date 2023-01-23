class Product:
    def __init__(self):
        self.__id = 101
        self.__eid = 102
        self.__sid = 103

    def Display(self):
        print(self.__id)
        print(self.__eid)
        print(self.__sid)


p = Product()
p.Display()
