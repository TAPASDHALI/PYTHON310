## ACCEPT THE PERCENTAGE FROMTHE USER AND DISPLAY THE GRADE ACCORDING TO THE FOLLOWING CRITERIA:
## below 25 --- D
## 25 to 45 --- C
## 45 to 50 --- B
## 50 to 60 --- B+
## 60 to 80 --- A
## Above 80 --- A+

per = int(input("Enter any number not above 100:- "))

if per > 80:
    print("Grade is A+")
elif per <= 80 and per > 60:
    print("Grade is A")
elif per <= 60 and per > 50:
    print("Grade is B+")
elif per <=50 and per > 45:
    print("Grade is B")
elif per <= 45 and per >= 25:
    print("Grade is C")
else:
    print("Grade is D")