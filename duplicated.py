name=list(map(int,input("enter the list: ").split()))
freq={}
duplicates=[]
for num in name:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for key,value in freq.items():
    if value>1:
        duplicates.append(key)
print("Duplicates: ",duplicates)
        