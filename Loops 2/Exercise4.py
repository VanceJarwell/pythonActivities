def int_list(grades):   
    summ = 0 
    for n in grades:
        summ += n
    print(summ)

while 1:
    try:
        print("Enter integers to be added (Include space in between per integer): ")
        grades = [int(x) for x in input().split()]
        int_list(grades)
        break

    except:
        print("Not integers. Try again")
        continue
        

