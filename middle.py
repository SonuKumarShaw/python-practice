
word = input("Enter a word: ")

length = len(word)

if length % 2 != 0:
    middle = length // 2
    print("Middle character:", word[middle])
else:
    print("The word has an even number of characters.")
