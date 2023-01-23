# Class Variables
class Product:

    @classmethod
    def getProductDetalies(cls, pId, pName):
        print(pId, pName)


Product.getProductDetalies(101, 'ViVo')
