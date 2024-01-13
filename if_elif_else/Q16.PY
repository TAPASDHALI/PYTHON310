## WAP TO find the largest number out of three numbers excepted from user.
nm1 = int(input("Enter 1st number from user:- "))
nm2 = int(input("Enter 2nd number from user:- "))
nm3 = int(input("Enter 3rd number from user:- "))

if nm1 > nm2 and nm1 > nm3:
    print(f'{nm1} is a Largest Number')
elif nm2 > nm1 and nm2 > nm3:
    print(f'{nm2} is a Largest Number')
elif nm3 > nm1 and nm3 > nm2:
    print(f'{nm3} is a Largest Number')

