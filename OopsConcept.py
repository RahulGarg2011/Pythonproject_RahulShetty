# self keyword is mandatory for calling variables names inside methods.
# instance and class variables have different purpose.
# constructor name should be __init__.
# new keyword is not required when you create an object.



class Calci:
    num = 200                                     # class variables

    def __init__(self, a, b):
        self.Fn = a                               # instance variables- Variables depending on objects
        self.Sn = b

        print("I am called automatically when the object is created")
        print("{} {}".format("Value of class variable is", 200))
        print(Calci.num)


    def getData(self):
        print("Method inside Class")
        print(Calci.num)

    def summation(self):
        return self.Fn + self.Sn + self.num        # self.num or Calci.num (2 ways)


object1 = Calci(2, 3)
print("*********************")

object1.getData()
print("************************")

print(object1.summation())
print("***************************")

Data = object1.num
print(Data)
print("*****************")

obj = Calci(1000, 1000)
print("******************")

print(obj.summation())
print("***************************")

ob = Calci(10, 15)
print("****************************")

print(ob.summation())
print("OOPs Program ends here")


