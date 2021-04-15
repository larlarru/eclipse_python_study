from Cython.Compiler.Naming import self_cname
class Animal:
    def __init__(self):
        self.age = 0
        self.egg = False
    def getOld(self):
        self.age+=1
    def changeEgg(self):
        self.egg = not self.egg

class Human(Animal):
    def __init__(self):
#         super.__init__()
        Animal.__init__(self)
        self.moneypower = 11
    def makeMoney(self, earnmoney):
        self.moneypower += earnmoney
         
# class Human:
#     def __init__(self):
#         self.moneypower = 11
#     def makemoney(self):
#         self.moneypower += self.moneypower 
        
a = Animal()
print(a.age)
print(a.egg)

a.getOld()
print(a.age)
print(a.egg)

a.changeEgg()
print(a.age)
print(a.egg)

# b = Human()
# print(b.moneypower)
# b.makemoney()
# print(b.moneypower)

a = Human()
print(a.age)
print(a.egg)
print(a.moneypower)
a.getOld()
a.changeEgg()
a.makeMoney(100)
print(a.age)
print(a.egg)
print(a.moneypower)