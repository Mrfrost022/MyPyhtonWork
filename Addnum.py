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