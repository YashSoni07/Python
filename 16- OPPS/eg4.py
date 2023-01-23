# Class Variables
class Product:

    pId = 101
    pName = 'Vivo'

    # Constructor
    @classmethod
    def getProductDitalies(cls):
        print(cls.pId, cls.pName)

Product.getProductDitalies()