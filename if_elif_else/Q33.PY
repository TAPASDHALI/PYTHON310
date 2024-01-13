## ACCEPT THE NUMBER OF DAYS FROM THE USER AND CALCULATE THE CHARGE FOR LIBRARY ACCORDING TO FOLLOWING:- 

## TILL FIVE DAYS: RS 2/DAY
## SIX TO TEN DAYS: RS 3/DAY
## 11 TO 15 DAYS:   RS 4/DAY
## AFTER 15 DAYS:   RS 5/DAY

nd = int(input("Enter number of days:- "))
cl = 0
if nd <= 5:
    cl = nd * 2
elif nd > 5 and nd <= 10:
    cl = nd * 3
elif nd <= 15:
    cl = nd * 4
elif nd > 15:
    cl = nd * 5
print("Calculate the charge for library:- ", cl)