## WAP TO CLACULATE THE ELECTRICITY BILL(accept number of unit from user) according to the following criteria

## unit              price
## first 100 units   no charge
## next 100 units    rs 5 per unit
## after 200 units   rs 10 per unit
## (for example if input is 350 than total bill amount is rs. 2000)
## hide answer

amt = 0
nu = int(input("Enter number of electric unit:- "))
if nu <= 100:
    amt = 0
if nu>100 and nu <=200:
    amt = (nu-100)*5
if nu > 200:
    amt = 500 + (nu-200)*10
print("Amount to pay:- ", amt)
 