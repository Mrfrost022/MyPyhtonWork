num=int(input("Enter a number whose factorial you want: "))
factorial=1
n=1
if num<0:
    print("Not Defined")
    exit()
while n<=num:
    factorial=factorial*n
    n=n+1
print("The factorial of", num, "is", factorial)