from OopsConcept import Calci


class ChildImpl(Calci):
    num2 = 300

    def __init__(self):
        Calci.__init__(self, 100, 200)
        print("Child class constructor")

    def getCompleteData(self):
        #print(ChildImpl.num2 + ChildImpl.num)
        return self.num2 + self.num + self.summation()


Obj2 = ChildImpl()
print("*******************")

V = Obj2.getCompleteData()
print(V)

print(Obj2.num2)
print("*******************")

OB = ChildImpl()
print(OB.num2)
print(OB.num)
print(OB.getData())
