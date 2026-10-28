secret=int(input("Enter the Number: "))
while True:
    guess=int(input("Enter the Number: "))
    if guess==secret:
        print("Congratulation")
        break
    else:
        print("Try again")