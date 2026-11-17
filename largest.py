
def largest(set):
    
    if len(set)==1:
        return set[0]
    else:
        return max(set[0],largest(set[1:]))
set=list(map(int,input("Enter the number:").split()))
print(largest(set))
