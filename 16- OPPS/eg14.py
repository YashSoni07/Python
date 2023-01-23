# OverWriting

class SBI:
    def RateOfIntarest(self):
        return 0


class AXIS(SBI):
    def RateOfIntarest(self):
        return 5


class ICIC(SBI):
    def RateOfIntarest(self):
        return 10


a = AXIS()
print(a.RateOfIntarest())

i = ICIC()
print(i.RateOfIntarest())
