import sys

fileName = input("Enter the file name: ")

if fileName == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    sys.exit(0)

try:
    file = open(fileName, 'r')
except:
    print("File cannot be opened: " + fileName)
    sys.exit(1)


linesList = [line.strip("\n") for line in file]


def countedSubjectLines(data):
    counter = 0
    for line in linesList:
        if line.startswith("Subject"):
            counter += 1
    print(counter)

countedSubjectLines(linesList)
