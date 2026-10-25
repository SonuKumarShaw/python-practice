a=input("Enter a string: ")
print(a)
print(a[::-1])
if a==a[::-1]:
    print("Both are equal: true")
else:
    print("Both are not equal: false")