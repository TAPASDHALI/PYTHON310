## WAP TO ACCEPT A NUMBER FROM 1 TO 12 AND DISPLAY THE NAME OF THE MONTH AND DAYS -
# IN THAT MONTHLIKE 1 FOR JANUARY AND NUMBER OF DAYS 31 AND SO ON.

nm1 = int(input("Enter the number between 1 to 12:- "))
if nm1 == 1:
    print("This is January and total days this month 31")
elif nm1 == 2:
    print("This is February and total days this month 28")
elif nm1 == 3:
    print("This is March and total days this month 31")
elif nm1 == 4:
    print("This is April and total days this month 30")
elif nm1 == 5:
    print("This is May and total days this month 31")
elif nm1 == 6:
    print("This is June and total days this month 30")
elif nm1 == 7:
    print("This is Julay and total days this month 31")
elif nm1 == 8:
    print("This is August and total days this month 31")
elif nm1 == 9:
    print("This is September and total days this month 30")
elif nm1 == 10:
    print("This is Octobar and total days this month 31")
elif nm1 == 11:
    print("This is November and total days this month 30")
elif nm1 == 12:
    print("This is December and total days this month 31")
else:
    print("Please write number between 1 to 12")
