## ACCEPT THE AGE, SEX('M', 'F'), NUMBER OF THE DAYS AND DISPLAY THE WAGES ACCORDINGLY
## AGE              SEX               WAGE/DAY
## >=18 AND < 30    M                 700
##                  F                 750

## >=30 AND <=40    M                 800
##                  F                 850 

## IF AGE DOES NOT FALL IN ANY RANGE DISPLAY THE FOLLOWING MESSAGE: "ENTER APPROPRIATE AGE"

age = int(input("Enter your age:- "))
sex = input("Enter sex(M/F)")
nd = int(input("ENTER NUMBER OF DAYS:- "))
if age >= 18 and age < 30 and sex.upper() == "M":
    amt = nd*700
    print("Total wages is:- ", amt)
elif age >= 18 and age < 30 and sex.upper() == "F":
    amt = nd*750
    print("Total wages is:- ", amt)
elif age >= 30 and age <= 40 and sex.upper() == "M":
    amt = nd*800
    print("Total wages is:- ", amt)
elif age >= 30 and age <= 40 and sex.upper() == "F":
    amt = nd*850
    print("Total wages is:- ", amt)
else:
    print("Enter Appropriate Age")

