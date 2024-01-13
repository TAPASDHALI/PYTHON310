## WAP TO CHECK WHETHER A NUMBER IS PRIME OR NOT?

k = 0
num = int(input("Enter any number:- "))
if num == 0 or num == 1:
    k = 1
for i in range(2, num):
    if num % i == 0:
        k = 1
if k == 1:
    print("number is not prime")
else:
    print("Number is prime number")