class Product:
    def __init__(self):
        self.id = 101
        self._eid = 102
        self.__sid = 103


p = Product()
print(p.id)
print(p._eid)
# print(p.__sid) #AttributeError: 'Product' object has no attribute '__sid'. Did you mean: '_eid'?

print(p.Product__sid)
