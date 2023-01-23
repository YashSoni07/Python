class Product:
    pid = 101
    pName = "ViVo"

    # Instance Method
    def d1(self):
        print(self.pid, self.pName)

    # Class Method
    @classmethod
    def d2(cls):
        print(cls.pid, cls.pName)

    # Statice Method
    @staticmethod
    def d3():
        print(Product.pid, Product.pName)


Product().d1()
Product.d2()
Product.d3()
