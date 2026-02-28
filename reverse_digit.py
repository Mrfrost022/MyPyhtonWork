# Code for reversing the digit of a number
num=input("Enter a number: ")
if int(num)>=0:
    rev_num=int(num[::-1])
    print("The reverse of the given number is", rev_num)
else:
    num=num[1:]
    rev_num=int(num[::-1])
    print("The reverse of the given number is", rev_num*(-1))