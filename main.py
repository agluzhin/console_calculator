# Input variables which contain numbers and math operation
a = int(input())
b = int(input())
math_operation = input()

# Functions which return math operation's results
def calculation_sum(a,b):
    return a + b

def calculation_subtract(a,b):
    return a - b

def calculation_division(a,b):
    return a / b

def calculation_multiply(a,b):
    return a * b

# Conditions which control selected operation and output relevant result
if math_operation == '+':
    result = calculation_sum(a,b)
    print(f'The result of the sum of the numbers {a} and {b} is {result}')
elif math_operation == '-':
    result = calculation_subtract(a,b)
    print(f'The result of the subtract of the numbers {a} and {b} is {result}')
elif math_operation == '/' or math_operation == ':':
    result = calculation_division(a,b)
    print(f'The result of the division of the numbers {a} and {b} is {result}')
elif math_operation == '*':
    result = calculation_multiply(a,b)
    print(f'The result of the multiply of the numbers {a} and {b} is {result}')
else: 
    print('Error! The operation may have been entered incorrectly. Try again.')