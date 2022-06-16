file = open('test.txt')

# Read all the contents of the file

# print(file.read())

# print(file.read(3))

# print(file.read(16))

# To read one single line at a time

# print(file.readline())
# print(file.readline())
# print(file.readline())

# Print line by line using readline method

# line = file.readline()
#
# while line != "":
#     print(line)
#     line = file.readline()

# j = [Rahul, Belmont, Vijay Nagar, Indore, MP, 123, #hello, @gmail.com]
j = file.readlines()          # readlines method saves the values/data in a list format
for i in j:
    print(i)


file.close()



