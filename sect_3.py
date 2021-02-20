# VARIABLES | DATA TYPES | CASTING
import sys

name = 'Maynard Keenan'

age = 56

print(f'My name is {name} & i am {age} years old')

'''
Escape sequences for strings:

    - New line: \n

    - Backslash: \\

    - Single quote: \'

    - Backspace: \b

    - Tab: \t
'''

print(f'My name is {name} & i\'m {age} years old')

print(sys.maxsize)

print(sys.float_info.max)

float1 = 1.1111111111111111

float2 = 1.1111111111111111

print(float1 + float2) # error

complex_number = 5 + 6j

print(complex_number)

bool_val = True

print(bool_val)

val_0 = 23

print(val_0)

val_0 = 'something else'

print(val_0)

print('Casting (float -> int): ', type(int(47.51)))

print('Casting (float -> string): ', type(str(47.51)))

print('Casting (unicode -> string): ', type(chr(97)))

print('Casting (char -> unicode): ', type(ord('x')))

print('Casting (int -> float): ', type(float(47)))

val_1 = '7'

val_2 = '13'

print(f'{val_1} + {val_2} = {int(val_1) + int(val_2)}')