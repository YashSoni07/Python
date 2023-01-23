# Constructor With Arguments
class Product:

    # def __init__(self):
    #     print('Special Method / Const')
    def __init__(self, pID, pName):
        self.nID = pID  # Instance Variable
        self.pName = pName
        print(self.nID, self.pName)


Product(101, 'ViVo')
