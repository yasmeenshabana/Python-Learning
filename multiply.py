
# Function by user input
def multiply():
    first= input("Input 1st number is \n")
    second=input("Input 2nd number is \n")

    product= int(first)*int(second)
    print("Result is :", product)

# multiply()

# Function by parameter

def multiplication(a,b):
    return a*b 

result = multiplication(3,5)
print("Value 1 ", result)
print("Value 2 ", multiplication(3,5))

