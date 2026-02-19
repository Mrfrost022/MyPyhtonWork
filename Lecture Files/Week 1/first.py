# code to check number is even or odd
number=int(input("Enter the number here"))
if (number%2==0):
    print(number, "is Even")
elif(number==0):
    print("This number is neither even nor odd")
else:
    print(number, "is odd")