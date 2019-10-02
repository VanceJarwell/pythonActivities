#Set the counter and total to 0
counter = 0
total = 0

#Loop
while True:
    number = input("Enter a number: ")    
    if number == 'done' or number == "Done":
        break
    #Sets input to a float if input is a string returns error and tries again
    try:
        getNum = float(number)
    except:
        print('Invalid input')
        continue
    #Increments counter and adds the inputed number to the total
    counter = counter + 1
    total = total + getNum

#Displays the Total, Counter and Average
print (total, counter, total/counter)
