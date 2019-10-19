def backwards(word):
    index = len(word) - 1
    while index >= 0:
        print(word[index])
        index -= 1


word = input("Enter a word: ")
backwards(word)
