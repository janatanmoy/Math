# calculator
x= float(input("Enter Your First Number: "))
print("Choose Your Operation:-\n1= Addtion\n2= Subtraction\n3= multiplication\n4= division ")
# addition=1
# subtraction=2l
# multiplication=3
# division=4
operation=int(input("Enter Your Operation: "))
if operation not in [1, 2, 3, 4]:
    print("Invalid Input.\nPlease Enter a Valid Number")
    exit()
y=float(input("Enter Your Second Number: "))
if operation==1:
    print("Your Result is:",x+y)
    print ("Thank You For Using Calculator.\nVisit Again.")
elif operation==2:
    print("Your Result is:",x-y)
    print ("Thank You For Using Calculator.\nVisit Again.")
elif operation==3:
    print("Your Result is:",x*y)
    print ("Thank You For Using Calculator.\nVisit Again.")
elif operation==4:
    if y==0:
        print("You cannot divided by zero")
    elif x<y:
        print("Your Second Number is Greater than Your First Number.\nPlease Check Your Number.")
    else:
        print(f"Your Result is:{x/y:.2f}")
        print ("Thank You For Using Calculator.\nVisit Again.")