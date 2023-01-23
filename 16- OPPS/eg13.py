# # Polymorphic
#
# from  multipledispatach import dispatch
# class Product:
#     @dispatch(float, str)
#     def getProductDittles(self, pID, pName):
#         self.pID = pID
#         self.pName = pName
#         print(self.pID, self.pName)
#
#     @dispatch(float, str)
#     def getProductDittles(self, pID, pName):
#         self.pID = pID
#         self.pName = pName
#         print(self.pID, self.pName)
#
#     @dispatch(str):
#     def __init__(self, job):
#         self.job = job
#         print(self.job)
#
#     @dispatch(int):
#     def __int__(self, contact):
#         self.contact = contact
#         print(self.contact)
#
# a = Product("sales Jobs")
# a.getProductDittles(101, 'Ap')
# a.getProductDittles(101.1, "APPP")
# a = Product(101101)
#