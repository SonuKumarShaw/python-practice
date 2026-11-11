numbers=int(input("Enter hour(0-23):"))
if numbers>=5 and numbers<=11:
    print("Good Morning")
elif numbers>=12 and numbers<=16:
    print("Good Afternoon")
elif numbers>=17 and numbers<=20:
    print("Good Evening")
else:
    print("Good Night")
    