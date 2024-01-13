## ACCEPT THE KILOMETERS COVERED AND CALCULATE THE BILL ACCORDING TO THE FOLLOWING CRITERIA:- 

## FIRST 10 KM      : RS 11/KM
## NEXT 90KM        : RS 10/KM
## AFTER THAT       : RS 9/KM

km = int(input("Enter the kilomiter:- "))

if km <= 10:
    rs = km * 11
elif km <= 90:
    rs = km * 10
elif km > 90:
    rs = km * 9
print("The kilomiters cover and calculate the Bill:- ", rs)
