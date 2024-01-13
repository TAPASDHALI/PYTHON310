## WAP to accept percentage from the user and display the grade according to the following criteria:
## Marks                 Grade
## > 90                  A
## > 80 and <= 90        B
## >=60 and <=80         C
## below 60              D
per = int(input("Enter user defind Number:- "))
if per >= 90:
    print("Grade is A")
elif per >= 80 and per <= 90:
    print("Grade is B")
elif per >= 60 and per <= 80:
    print("Grade is C")
elif per < 60:
    print("Grade is D")
print("Rest of the code")
