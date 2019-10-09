def counter(array):
    x = 0
    for i in array:
        x = x + 1
    print(x)
    
print("Enter a list (Include space in between per integer): ")
array = [x for x in input().split()]
counter(array)
