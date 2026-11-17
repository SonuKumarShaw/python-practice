def palin(elements):
    if len(elements)<=1:
        return True
    if elements[0]!=elements[-1]:
        return False
    return palin(elements[1:-1])
elements=input("Enter the elements")
if palin(elements):
    print("Palindrome")
else:
    print("not Palindrom")