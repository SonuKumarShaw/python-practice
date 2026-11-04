numbers=list(map(int,input("ENter the numbers:").split()))
def even(numbers):
    even_numbers=[]
    for n in numbers:
        if n%2==0:
            even_numbers.append(n)
    return even_numbers

print("Even Numbers are:", even(numbers))