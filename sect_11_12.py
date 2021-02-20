# Section 11: FUNCTIONS (part 1)
def add_values(val_1, val_2):
    return val_1 + val_2

print('\n7 + 3 =', add_values(7, 3))

def assign_name():
    name = 'Norman Bates'

assign_name()

#print(name) # error

print('\n*****************************************\n')

def change_name_0(name):
    name = 'Luke Kemp'

name_0 = 'Bruce Wayne'

change_name_0(name_0) # doesn't work

print(name_0)

print('\n*****************************************\n')

def change_name_1():
    return 'Colin Firth'

name_1 = 'Edward Norton'

print(name_1)

name_1 = change_name_1() # this works

print(name_1)

print('\n*****************************************\n')

def change_name_2():
    global global_name

    global_name = 'John Kennedy'

global_name = 'Max Payne'

print(global_name)

change_name_2()

print(global_name)

print('\n*****************************************\n')

def add(num1, num2):
    result = num1 + num2

print(add(5, 4))

print('\n*****************************************\n')

def is_float(str_val):
    try:
        float(str_val)

        return True
    except ValueError:
        return False

pi1 = 3.14

print('Is pi1 a float?', is_float(pi1))

pi2 = '3.14'

print('Is pi2 a float?', is_float(pi2))

pi3 = 'A'

print('Is pi3 a float?', is_float(pi3))

# a challenge
def solve_equation(equation):
    x, add, val_1, equal, val_2 = equation.split()

    val_1, val_2 = int(val_1), int(val_2)

    return 'x = ' + str(val_2 - val_1)

print(solve_equation('x + 4 = 9'))

print('\n--------------------------------------------------------------------------------\n')

# Section 12: FUNCTIONS (part 2)
def multiply_divide(val_1, val_2):
    return (val_1 * val_2), (val_1 / val_2)

multiply, divide = multiply_divide(5, 4)

print(f'5 * 4 = {multiply}')

print(f'5 / 4 = {divide}')

print('\n*****************************************\n')

def is_prime(val):
    for i in range(2, val):
        if(val % i) == 0:
            return False
    return True

def get_primes(max_val):
    list_of_primes = []

    for val in range(2, max_val):
        if is_prime(val):
            list_of_primes.append(val)
    
    return list_of_primes

max_num = int(input('Search for primes up to: '))

listOfPrimes = get_primes(max_num)

for prime in listOfPrimes:
    print(prime)

print('\n*****************************************\n')

def sum_all(*args):
    total = 0

    for i in args:
        total += i
    
    return total

print('Total: ', sum_all(23, 47, 51, 7, 69, 13))

print('\n*****************************************\n')

import math

def get_area(shape):
    shape = shape.lower()

    if shape == 'rectangle':
        get_rect_area()
    elif shape == 'circle':
        get_circle_area()
    else:
        print('rectangle or circle only')

def get_rect_area():
    length = float(input('\nThe rectangle length: '))

    width = float(input('\nThe rectangle width: '))

    print(f'\n\tThe rectangle area: {length * width}')

def get_circle_area():
    radius = float(input('\nThe circle radius: '))

    area = math.pi * math.pow(radius, 2)

    print(f'\n\tThe circle area: {area}')

def main():
    shape_type = input('Enter rectangle or circle: ')

    get_area(shape_type)

main()