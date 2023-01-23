class Product:
    def __init__(self):
        print("Spaical Method")

    # def __new__(cls):
    #     print("Magic Method")

    def __del__(self):
        print("Delete Method")


Product()