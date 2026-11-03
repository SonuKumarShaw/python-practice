def average (num):
    return sum(num) / len(num)

num=list(map(float, input("Enter the numbers :").split()))
print("The average of the numbers are: ",average(num))