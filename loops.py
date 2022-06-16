#If....else

# eg 1

statement = "Sachin is the God of Cricket"

if statement == "Sachin is the God":
   print(True)
else:
    print("Virat is GOAT")

print("Cricket is the real winner")

# eg 2

num = 10
if num > 15:
    print("condition matches")
else:
    print("condition does not match")

print("Loop ends")

print("**********************")

# for loop

rah = [10, 20, 30, 40, 50]

for j in rah:
    print(j)

print("**********************")

for j in rah:
    print(j*3)

print("*******************")

#Sum of first 5 natural numbers 1+2+3+4+5= 15
#range(i,j) -> i to j-1

sums = 0
for k in range(1, 6):
    sums = sums + k
print(sums)

# sums = 10
# for k in range(1, 4):
#     sums = sums - k
# print(sums)

print("****************")

for i in range(1, 10, 2):
    print(i)

print("*********Skipping First Index*******")

for m in range(10):
    print(m)
