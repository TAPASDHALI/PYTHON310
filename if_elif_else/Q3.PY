## WAP TO CHECK WHETHER A LAST DIGIT NUMBER(ENTERED BY USER) IS DIVIGIBLE BY 3 OR NOT
num = int(input("Enter any number:- "))
num1 = num%10
if num1 % 3 == 0:
    print("Last digit of a number divisible by 3")
else:
    print("Last digit of a number not divisible by 3")