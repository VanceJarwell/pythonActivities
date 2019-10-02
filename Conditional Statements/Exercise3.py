#Exercise 3 of conditional statements

#loops the whole program
while 1:
    try:
        #gets the value of input and comapres it
        grade = float(input('Enter score: '))
        if grade == 0:
            print('Score out of range')
            continue
        elif grade < 0.6:
            print('F')
            break
        elif grade < 0.7:
            print('D')
            break
        elif grade < 0.8:
            print('C')
            break
        elif grade < 0.9:
            print('B')
            break
        elif grade < 1:
            print('A')
            break
        elif grade >= 1:
            print('Score out of range')
            continue
        else:
            print('Bad score')
            continue

    except:
        print('Bad score')

    
    
