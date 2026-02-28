# code for checking the entered number is palindrome or not
num=int(input("Enter a number: "))
absNum=abs(num)
rev_num=0
#reverse the number
while absNum>0:
    l=absNum%10
    rev_num=rev_num*10+l
    absNum=absNum//10
#check for palindrome
if num>=0:
    if num==rev_num:
        print("The given number is a palindrome")
    else:
        print("The given number is not a palindrome")
else:
    if num==rev_num*(-1):
        print("The given number is a palindrome")
    else:
        print("The given number is not a palindrome")