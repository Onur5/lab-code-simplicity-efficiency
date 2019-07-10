"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')

# Substitution of words for digits and signs (+ or -)
# Changed type of inputs
# Changed variable name
FIRST_NUM = int(input('Please choose your first number (0 to 5): '))
OPERATION = input('What do you want to do? + or - : ')
SECOND_NUM = int(input('Please choose your second number (0 to 5): '))

# Changed the list of different lines by a function
def operations(num_1, operator, num_2):
    """input: num_1, num_2 is a number from 0 to 5
                operator is a operator sign
        out: gives de operation results"""
   if num_1 not in list(range(6)) or num_2 not in list(range(6)) or operator not in ["+", "-"]:
       return print("I am not able to answer this question. Check your input.")

   else:
        if operator == "+":
            result = num_1 + num_2
        else:
            result = num_1 - num_2
        print(f"{num_1} {operator} {num_2} equlas {result}")
        print("Thanks for using this calculator, goodbye :)")
operations(FIRST_NUM, OPERATION, SECOND_NUM)

