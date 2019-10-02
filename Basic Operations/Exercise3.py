#Exercise3

#User input
width = int(input('Width = '))
height = int(input('Height = '))

#Input calculations
widthDivInt = width//2
widthDivFlo = width/2.0
heightDiv = height/2

#Output
print('width//2 is ' + str(widthDivInt), type(widthDivInt))
print('width/2.0 is ' + str(widthDivFlo), type(widthDivFlo))
print('height/3 is ' + str(heightDiv), type(heightDiv))
