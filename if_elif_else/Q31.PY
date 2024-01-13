## ACCEPT THREE SIDES OF TRIANGLE AND CHECK WHETHER THE TRIANGLE IS POSSIBLE OR NOT

## (TRIANGLE IS POSSIBLE ONLY WHEN SUM OF ANY TWO SIDES IS GREATER THAN 3RD SIDE)

s1 = int(input("Enter 1st side triangle:- "))
s2 = int(input("Enter 2nd side triangle:- "))
s3 = int(input("Enter 3rd side triangle:- "))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print("Triangle is possible")
else:
    print("Triangle is not possible") 