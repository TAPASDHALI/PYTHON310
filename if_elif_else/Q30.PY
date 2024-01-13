## ACCEPT THE THREE NUMBERS FROM USER AND DISPLAY THE SECOND LARGEST NUMBER?

nm1 = int(input("Enter 1st Number:- "))
nm2 = int(input("Enter 2nd Number:- "))
nm3 = int(input("Enter 3rd Number:- "))

if (nm1 > nm2 and nm1 < nm3) or (nm1 < nm2 and nm1 > nm3):
    print("Second Largest Number is:- ", nm1)
elif (nm2 > nm1 and nm2 < nm3) or (nm2 < nm1 and nm2 > nm3):
    print("Second largest Number is:- ", nm2)
elif (nm3 > nm1 and nm3 < nm2) or (nm3 < nm1 and nm3 > nm2):
    print("Second largest number is:- ", nm3)