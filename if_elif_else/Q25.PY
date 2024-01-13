## ACCEPT THE MARKED PRICE THE USER AND CALCULATE THE NET AMOUNT AS(MARKED PRIC - DUSCOUNT) TO PAY ACCORDING TO FOLLOWING CRITERIA:

## MARKED PRICE                              DISCOUNT
## > 10000                                   20%
## > 7000 AND <= 10000                       15%
## <= 7000                                   10%

mrk = int(input("Enter the total amount of the marked price:- "))

pay = 0
if mrk > 10000:
    dis = 20/100*mrk
elif mrk > 7000 and mrk <= 10000:
    dis = 15/100*mrk
elif mrk <= 7000:
    dis = 10/100*mrk
pay = mrk -dis
print("Net amount to pay:- ", pay) 
