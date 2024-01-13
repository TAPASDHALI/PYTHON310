## WAP TO CHECK WHETHER A NUMBER(ACCEPTED FROM USER) IS DIVISIBLE BY 2 AND 3 BOTH.

nm = int(input("Enter the number:- "))
if nm % 2 == 0 and nm % 3 == 0:
    print("Number is devigible by 2 and 3 are both")
else:
    print("Not divisilbe Both")