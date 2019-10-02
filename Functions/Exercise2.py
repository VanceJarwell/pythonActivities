#Exercise 3 of conditional statements


def computegrade(grade):
    while 1:
        try:
            if grade <= 0:
                print('Score out of range')
                return grade
            elif grade < 0.6:
                print('F')
                return grade
            elif grade < 0.7:
                print('D')
                return grade
            elif grade < 0.8:
                print('C')
                return grade
            elif grade < 0.9:
                print('B')
                return grade
            elif grade < 1:
                print('A')
                return grade
            elif grade <= 1:
                print('Score out of range')
                return grade
            else:
                print('Bad score')
                return grade
        except:
            print('Bad score')

#loops the whole program
while 1:
    try:
        #gets the value of input and comapres it
        grade = float(input('Enter score: '))
        computegrade(grade)
        if grade >0 and grade < 1:
            break
            
    except:
        print('Bad score')
        continue

    
    
