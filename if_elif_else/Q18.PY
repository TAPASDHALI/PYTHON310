### ACCEPT THE AGE OF 4 PEOPLE AND DISPLAY THE YOUNGEST ONE?

ag1 = int(input("Enter the 1st age:- "))
ag2 = int(input("Enter the 2nd age:- "))
ag3 = int(input("Enter the 3rd age:- "))
ag4 = int(input("Enter the 4th age:- "))


if ag1 < ag2 and ag1 < ag3 and ag1 < ag4:
    print(f'Age Youngest person is {ag1}')
elif ag2 < ag1 and ag2 < ag3 and ag2 < ag4:
    print(f'Age Youngest person is {ag2}')
elif ag3 < ag1 and ag3 < ag2 and ag3 < ag4:
    print(f'Age Youngest person is {ag3}')
elif ag4 < ag1 and ag4 < ag3 and ag4 < ag3:
    print(f'Age Youngest person is {ag4}')
