pit = 5

while pit > 1:
    print(pit)
    pit = pit - 1

print("********************")

pit = 5
while pit > 1:
    if pit != 4:
        print(pit)

    pit = pit - 1
print("*********************")

it = 10

while it > 1:
    if it == 9:
        it = it - 1   #could be 2,3,4 to skip the iteration
        continue
    if it == 3:
        break

    print(it)
    it = it - 1

print("While loop ends")


