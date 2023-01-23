class Product:

    def SetDittles(self, id, name):
        self.__id = id
        self.__name = name

    def GetDittles(self):
        return self.__id, self.__name


p = Product()
p.SetDittles(101, "ViVo")
print(p.GetDittles())
