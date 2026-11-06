numbers=list(map(int,input("enter the numbers:").split()))
positive=0
negative=0
for n in numbers:
    if n>0:
        positive+=1
    elif n<0:
        negative+=1
print("Count of positive and negative numbers are:",positive,negative)