def reverse(data_list):
    length = len(data_list)
    s = length

    new_list = [None]*length

    for item in data_list:
        s = s - 1
        new_list[s] = item
    
    print(new_list)

print("Enter a list of items (Include space in between per item): ")
data_list = [x for x in input().split()]
reverse(data_list)


