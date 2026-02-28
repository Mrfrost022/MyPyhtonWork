'''# Code for reversing the digit of a number
num=input("Enter a number: ")
if int(num)>=0:
    rev_num=int(num[::-1])
    print("The reverse of the given number is", rev_num)
else:
    num=num[1:]
    rev_num=int(num[::-1])
    print("The reverse of the given number is", rev_num*(-1))
'''
'''
#code for reversing the digit of a number using while loop
num=int(input("Enter a number: "))
rev_num=0
if num<0:
    num=num*(-1)
    while num>0:
        l=num%10
        rev_num=rev_num*10+l
        num=num//10
    rev_num=rev_num*(-1)
elif num==0:
    rev_num=0
else:
    while num>0:
        l=num%10
        rev_num=rev_num*10+l
        num=num//10
print("The reverse of the given number is", rev_num)
'''
#optimised code for reversing the digit of a number using while loop
num=int(input("Enter a number: "))
absNum=abs(num)
rev_num=0
while absNum>0:
    l=absNum%10
    rev_num=rev_num*10+l
    absNum=absNum//10
if num>=0:
    print("The reverse of the given number is", rev_num)
else:
    print("The reverse of the given number is", rev_num*(-1))