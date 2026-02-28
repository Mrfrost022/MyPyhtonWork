#for printing in same line we can use end parameter in print function
for i in range (1,11):
    print(i,end=" ")
'''This will print all numbers from 1 to 10 like
1 2 3 4 5 6  7 8 9 10 because we have given end parameter as space in print function'''

print("\n")

#there is one more parameter in print function called sep which is used to separate the values with a specific character or string
#print("Hello","World","Python",sep="-") this will print Hello-World-Python because we have given sep parameter as - in print function 
print("Your date of bith is ",end="")
print(10,9,2000, sep="/")
'''This will print Your date of birth is 10/9/2000 because we have given end parameter as space in first print function and sep parameter as / in second print function'''

#Formated string in print function
#code for multiplication table
num=int(input("Enter the number whose table you want to print: "))
for i in range (1,11):
    print(f"{num} x {i} = {num*i}")
'''This will print the multiplication table of the number entered by the user in the format num x i = num*i because we have used formatted string in print function and used curly braces to insert the values of num, i and num*i in the string'''

#similar print will be done using format method of string
for i in range (1,11):
    print("{0} x {1} = {0}".format(num,i,num*i))
'''This will also print the multiplication table of the number entered by the user in the format num x i = num*i because we have used format method of string and used curly braces to insert the values of num, i and num*i in the string'''

#similar print will be done using string modulo operator
for i in range (1,11): 
    print("%d x %d = %d"%(num,i,num*i))
'''This will also print the multiplication table of the number entered by the user in the format num x i = num*i because we have used string modulo operator and used %d to insert the values of num, i and num*i in the string'''