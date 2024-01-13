## WAP TO ACCEPT THE COST PRICE OF A BIKE AND DISPLAY THE ROAD TAX TO BE PAID ACCORDING TO THE FOLLOWING CRITERIA:
## COST PRICE(IN RS)             TAX
## > 100000                      15%
## > 50000 AND <= 100000         10%
## <= 50000
tax = 0
pr = int(input("The cos price of a Bike:- "))
if pr > 100000:
    tax = 15/100*pr
elif pr > 50000 and pr <= 100000:
    tax = 10/100*pr
else:
    tax = 5/100*pr
print("Tax to be Paid:- ", tax) 