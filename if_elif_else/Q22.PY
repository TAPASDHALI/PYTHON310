## ACCEPT THE FOLLOWING FROM THE USER AND CALCULATE THE PERCENTAGE OF CLASS ATTENDED:
## A> TOTAL NUMBER OF WORKING DAYS
## B> TOTAL NUMBER OF DAYS ABSENT

## AFTER CALCULATING PERCENTAGE SHOW THAT IF THE PERCENTAGE IS LESS THAN 75 THAN STUDENT WILL NOT BE ABLE TO SIT IN EXAM

pt = int(input("Enter total number of present days:- "))
ab = int(input("Enter total number of absent days:- "))

per = (pt - ab) / pt*100
if per < 75:
    print("You are not eligible for exam")
else:
    print("You are eligible for exam")