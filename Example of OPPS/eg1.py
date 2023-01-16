# Types of Method
# Instance Method, Variable Method and Instance Method

class Product:
    # Instance Method
    # def getProductDatiale(self):
    #     print('Inserted Product Datiales')

    def getProductDatiles(self, pid, pname):
        self.pid = pid  # Instance Variable
        self.pname = pname

    def display(self):
        print(self.pid, self.pname)


P = Product()
P.getProductDatiles(101, "Vivo")
P.display()
