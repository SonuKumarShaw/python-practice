dictionary={}
n=int(input("Enter the elements: "))
for i in range(n):
    word=input("enter word")
    meaning=input("enter the meanings: ")
    dictionary[word]=meaning
search_word=input("enter the word to be search: ")
if search_word in dictionary:
    print("meaning: ", dictionary[search_word])
else:
    print("word not found")
    