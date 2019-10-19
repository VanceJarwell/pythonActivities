fileName = input("Enter file name: ")
file = open(fileName)
for i in file:
    i = i.rstrip().upper()
    print(i)
