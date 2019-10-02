#Exercise 1 and 2 Conditional Statements

#try again if error
while 1:
    try:
        hours = float(input('Enter Hours: '))
        rate = float(input('Enter Rate: '))
        break
    except:
        print('Error, please enter numeric input')

#calculation code for hours and rate
if hours > 40:
    payForty = hours - 40
    forty = (40 * rate) + (payForty * (rate)*1.5)
    print('Pay: ', forty)
else:
    pay = hours*rate
    print('Pay: ' + str(pay))
