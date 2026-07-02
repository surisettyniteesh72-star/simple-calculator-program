#"""Calculator Program

#input:
#num1
#num2
#operator
#output:
#perform the operations on the inputs
#"""

num1= int(input("give 1st number:"))
num2= int(input("give 2nd number:"))
operator= input("give operator: ")

if operator == "+":
    print(f" addition of 2 numbers is {num1+num2}")
elif operator == "-":
    print(f" subtraction of 2 numbers is {num1-num2}")    
elif operator == "*":
    print(f" multiplication of 2 numbers is {num1*num2}")
elif operator == "/":
    print(f" division of 2 numbers is {num1/num2}")
else:
    print("invalid operator")
