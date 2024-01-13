## ACCEPT THE ELECTRIC UNITS FROM THE USER AND CALCULATES THE BILL ACCORDING TO THE FOLLOWING RATES

## FIRST UNITS 100     :FREEE
## NEXT 200 UNITS      : RS. 2 PER UNITS.
## ABOVE 300 UNITS     : RS. 5 PER UNITS

## IF NUMBER OF UNIT IS 500 THEN TOTAL BILL = 0 + 400 + 1000 = 1400

units = int(input("Enter the Electric Units:- "))
b =0
if units <= 100:
    print("FIRST 100 UNITES ELECTRIC BILL IS FREE")
elif units > 100 and units <= 300:
    b = (units-100) * 2
else:
    b = 400 + (units - 100) * 5
print("Total amount of pay is Electric Bill:- ", b)
