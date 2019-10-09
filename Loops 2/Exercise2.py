def getMax(array):
    Max = 0;
    for number in array:
        if Max < number:
            Max = number;
    print(Max)

while 1:
    try:
        print("Enter integers (Include space in between per integer): ")
        array = [int(x) for x in input().split()]
        getMax(array)
        break

    except:
        print("Not integers. Try again")
        continue

