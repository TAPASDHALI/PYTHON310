## WAP TO ACCEPT TWO NUMBERS AND MATHEMATICAL OPERATORS AND PERFORM OPERATION ACCORDINGLY.

## ENTER FIRST NUMBER:- 7
## ENTER SECOND NUMBER:- 9
## ENTER OPERATOR: +
## YOUR ANSWERIS: 16


nm1 = int(input("Enter 1st Number:- "))
nm2 = int(input("Enter 2nd Number:- "))
op = input("Enter the mathematical operation:- ")

if op == "+":
    print("Result is:- ", nm1 + nm2)
elif op == "-":
    print("Result is:- ", nm1 - nm2)
elif op == "*":
    print("Result is:- ", nm1 * nm2)
elif op == "**":
    print("Result is:- ", nm1 ** nm2)
elif op == "/":
    print("Result is:- ", nm1 / nm2)
elif op == "//":
    print("Result is:- ", nm1 // nm2)