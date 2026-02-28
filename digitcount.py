#code for counting the number of digitd in the given number
num=int(input("Enter a number: "))
count=0
if num<0:
    num=num*(-1)
elif num==0:
    count=1
while num>0:
    count=count+1
    num=num//10
print("The number of digits in the given number is", count)