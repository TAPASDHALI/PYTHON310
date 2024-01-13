## WAP TO ACCEPT PERCENTAGE AND DISPLAY THE CATEGORY ACCORDING TO THE FOLLOWING CRITERIA:

## PERCENTAGE                           CATEGORY
## < 40                                 FAILED
## >= 40 AND < 55                       FAIR
## >= 55 AND < 65                       GOOD
## >= 65                                EXCELLENT

per = int(input("Enter the percentage:- "))

if per < 40:
    print("Failed")
elif per >= 40 and per < 55:
    print("Fair")
elif per >= 55 and per < 65:
    print("Good")
elif per >= 65:
    print("Excellent")