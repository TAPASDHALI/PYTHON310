## A COMPANY DECIDED TO GIVE BONUS TO EMPLOYEE ACCORDING TO FOLLOWING CRITERIA :

## TIME PERIOD TO SERVICE     BONUS
## MORE THAN 10 YEARS         10%
## >=6 AND <= 10              8%
## LESS THAN 6 YEARS          5%

## ASK USER THEIR SALARY AND YEARS OF SERVICE AND PRINT THE NET BONUS AMOUNT.

ser = int(input("Enter the time period of service:- "))
sal = int(input("Enter your salary:- "))

bns = 0
if ser > 10:
    bns = 10/100*sal
elif ser >= 6 and ser <= 10:
    bns = 8/100*sal
elif ser < 6:
    bns = 5/100*sal
print("Bonus is :- ", bns)
