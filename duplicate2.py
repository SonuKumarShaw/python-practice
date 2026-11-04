numbers=list(map(int,input("Enter the numbers:").split()))
def duplicate(numbers):
    unique = []
    for item in numbers:
        if item not in unique:
          unique.append(item)
    return unique
     
            
print("Unique Numbers are:", duplicate(numbers))