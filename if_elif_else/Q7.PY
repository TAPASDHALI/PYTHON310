## WAP TO ACCEPT A NUMBER FROM 1 TO 7 AND DISPLAY THE NAME OF THE DAY LIKE 1 FOR SUNDAY, 2 FOR MONDAY AND SO ON.
num = int(input("Enter any number between 1 to 7:- "))
if num == 1:
    print("It is Sunday")
elif num == 2:
    print("It is Monday")
elif num == 3:
    print("It is Tuesday")
elif num == 4:
    print("It is Wednesday")
elif num == 5:
    print("It is Thursday")
elif num == 6:
    print("It is Friday")
elif num == 7:
    print("It is Saturday")
else:
    print("Please Enter the number between 1 to 7")