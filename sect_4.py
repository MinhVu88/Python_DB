# USER INPUT & MATH FUNCTIONS
import math

name = input('\nwhat\'s your name? ')

print(f'\nHello {name.title()}')

# accept 2 or more values with the input() function
num_1, num_2 = input('\nEnter 2 numbers: ').split()

num_1 = int(num_1)

num_2 = int(num_2)

addition = num_1 + num_2

print('\t{} + {} = {}'.format(num_1, num_2, addition))

subtraction = num_1 - num_2

print('\t{} - {} = {}'.format(num_1, num_2, subtraction))

multiplication = num_1 * num_2

print('\t{} * {} = {}'.format(num_1, num_2, multiplication))

division = num_1 / num_2

print('\t{} / {} = {}'.format(num_1, num_2, division))

remainder = num_1 % num_2

print('\t{} % {} = {}'.format(num_1, num_2, remainder))

''' A challenge:

- Ask the user to input the number of miles

- Convert miles to kilometers (km = miles * 1.60934)

- Print the result in a format like this example: 5 miles = 8.0467 km
'''
miles = int(input('\nEnter the miles: '))

kilometers = miles * 1.60934

print('\t{} miles = {} kilometers'.format(miles, kilometers))

print('\n--------------------------------------------------------------------------------')

# the math module's functions
print('\nmath.ceil(4.4) -> ', math.ceil(4.4))

print('\nmath.floor(4.4) -> ', math.floor(4.4))

print('\nmath.fabs(-4.4) -> ', math.fabs(-4.4))

# factorial = 1 * 2 * 3 * 4
print('\nmath.factorial(4) -> ', math.factorial(4))

# return remainder of division
print('\nmath.fmod(5, 4) -> ', math.fmod(5, 4))

# receive a float & return an int
print('\nmath.trunc(4.2) -> ', math.trunc(4.2))

# return x^y
print('\nmath.pow(2, 2) -> ', math.pow(2, 2))

# return the square root
print('\nmath.sqrt(9) -> ', math.sqrt(9))

# special values
print('\nmath.pi -> ', math.pi)

print('\nmath.e -> ', math.e)

# define the base & 10^3 = 1000
print('\nmath.log(1000, 10) -> ', math.log(1000, 10))

# you can also use base 10 like this
print('\nmath.log10(1000) -> ', math.log10(1000))

# the trig functions: sin, cos, tan, asin, acos, atan, atan2, asinh, acosh, atanh, sinh, cosh, tanh
print('\nmath.sin(0) -> ', math.sin(0))

# convert radians to degrees & vice versa
print('\nmath.degrees(1.5708) -> ', math.degrees(1.5708))

print('\nmath.radians(90) -> ', math.radians(90))