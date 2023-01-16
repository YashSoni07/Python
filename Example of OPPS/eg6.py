# Static Variables
class Product:
    pId = 101
    pName = "ViVo"

    @staticmethod
    def getProductDitales():
        print(Product.pName, Product.pId)


Product.getProductDitales()
