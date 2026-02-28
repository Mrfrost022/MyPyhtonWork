#add first 10 number using for loop 
add=0
for i in range (10):
    add=add+i
print("the sum of first 10 number is",add)

#multiplication of first 10 number using for loop
mul=1
for i in range (1,11):
    mul=mul*i
print("the multiplication of first 10 number is",mul)

#table of n(user inputed) using for loop
n=int(input("Enter the number whose table you want to print: "))
for i in range (1,11):
    print(n,"x",i,"=",n*i)

#for loop range variation- step
for i in range (1,11,2):
    print(i)
'''this will print odd number from 1 to 10 because we have given step as 2 and starting point is 1
if we give step as 2 and starting point as 0 then it will print even number from 0 to 10'''

#reverse number counting in for loop range variation
'''for printing 9,8,7,6....0 we can use range(9,-1,-1) because the starting point is 9 and ending point is -1 and step is -1'''
for i in range(9,-1,-1):
    print(i)

#for loop without range funtion
a="Country"
for i in a:
    print(i)
'''This will print each character of the string in new line because we are iterating through the string using for loop and each character is treated as an element of the string'''