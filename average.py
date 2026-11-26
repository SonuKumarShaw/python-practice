marks = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))
    marks[name] = mark

sum =0
for mark in marks.values():
    sum+=mark
average=sum/len(marks)
print("marks:",marks)
print("average:",average)
    