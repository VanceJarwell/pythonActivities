#Exercise 1 Functions


#function for hour & rate computation
def computepay(hour , rate):
    if hour > 40:
        payForty = hour - 40
        forty = (40 * rate) + (payForty * (rate)*1.5)
        print('Pay: ', forty)
    else:
        pay = hour*rate
        print('Pay: ' + str(pay))
    

#gets the value of hours & rates
while 1:
        try:
            hours = float(input('Enter Hours: '))
            rates = float(input('Enter Rate: '))
            computepay(hours, rates)
            break
        except:
            print('Error, please enter numeric input')

        
