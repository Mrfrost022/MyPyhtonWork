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