## ACCEPT THE AGE OF 4TH PEOPLE AND DISPLAY WHO IS THE OLDESST ONE?

ag1 = int(input("Enter the age of the 1st man:- "))
ag2 = int(input("Enter the age of the 2nd man:- "))
ag3 = int(input("Enter the age of the 3rd man:- "))
ag4 = int(input("Enter the age of the 4th man:- "))

if ag1 > ag2 and ag1 > ag3 and ag1 > ag4:
    print("Age one is the oldest man")
elif ag2 > ag1 and ag2 > ag3 and ag2 > ag4:
    print("Age two is the oldest man")
elif ag3 > ag1 and ag3 > ag2 and ag3 > ag4:
    print("Age three is the oldest man")
elif ag4 > ag1 and ag4 > ag2 and ag4 > ag3:
    print("Age four is the oldest man")
elif ag1 >= ag2 and ag1 >= ag3 and ag1 >= ag4:
    print("All people are the same age")
