#CONCATENATE
a = "My name is Rahul"

b = "I am an IT professional."

print(a, "and", b)

print(a + " and " + b)

#LIST DATA TYPES
MyList = [10, 89, "Belmont Park", 12.34, "Garg"]

print(MyList)
print(MyList[0])
print(MyList[-4])
print(MyList[1:4])
print(MyList[0:2])
print(MyList[0:3])

MyList.insert(0, "Rah")
MyList.insert(5, "IB")

print(MyList)

MyList.insert(-1, "IBD")
print(MyList)

MyList.append("Last")
print(MyList)

MyList[3] = "Royal Amar Green"
print(MyList)

MyList[4] = "Human Beings"
print(MyList)


del MyList[4]
print(MyList)

# TUPLE

VAL = (1, "boss", 5)
print(VAL)

# print(VAL[3])
print(VAL[2])
print(VAL[-1])

# VAL[2]= "Hello" - 'tuple' object does not support item assignment'
print(VAL)


# Dictionary

D = {"Guna": "HDM", 2: "MVJ", "age": 30}

print(D["Guna"])

print(D["age"])

print(D[2])

#
dict = {}

dict["firstname"] = "Rahul"

dict["lastname"] = "Garg"

dict["age"] = 30

dict[30] = "age"

print(dict)

print(dict["firstname"])
print(dict["lastname"])
print(dict[30])
print(dict["age"])

t = (1, )          # tuple
t1 = (1)               #int type

print(type(t))
print(type(t1))