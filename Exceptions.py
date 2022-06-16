
itemsincart = 0
# 2 items will be added to the cart

if itemsincart != 2:  # raise Exception("Product count does not match")
    pass

# assert(itemsincart == 2)   # false
# assert(itemsincart == 0)   # true

# try, catch(except in Python)

# with open('file.txt', 'r') as reader:
#     reader.read()

# try:
#     with open('file.txt', 'r') as reader:
#         reader.read()
#
# except:
#     print("Try block has invalid code so the execution reached to except block")

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as A:
    print(A)

finally:                              # This block will get executed no matter what happens in try and except block
    print("Cleaning all the records")


# try:
#     with open('test.txt', 'r') as reader:
#         reader.read()
#
# except Exception as A:
#     print(A)