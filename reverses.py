def reverse(n):
    if len(n)==0:
        return n
    else:
        return reverse(n[1:])+ n[0]
n=input("enter the numbers: ")
print(reverse(n))
    