# read the file and store in list format
# reverse the list
# write the list back to the file

with open('test.txt','r') as reader:
    c = reader.readlines()       # [Rahul, Belmont, ... ]
    reversed(c)                  # [@gmail.com, #hello, ...]
    with open('test.txt', 'w') as writer:
        for line in reversed(c):
            writer.write(line)