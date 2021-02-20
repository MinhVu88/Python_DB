# FOR & RANGE
for i in [23, 47, 51, 7, 13, 69]:
    print(i)

print('\n*****************************************\n')

for i in range(5):
    print(i)

print('\n*****************************************\n')

for i in range(5, 10):
    print(i)

print('\n*****************************************\n')

for i in range(1, 21):
    if i % 2 != 0:
        print(i)

print('\n*****************************************\n')

my_float = float(input('Enter a float: '))

print('Rounded to 2 decimal places: {:.2f}'.format(my_float))

print('\n*****************************************\n')

''' A challenge: calculate how much money a person will have after investing for 10 years. The program will:

- Have the user enter the investment amount & expected interest

- Each year their investment will increase by investment + (investment * interest rate)

- Display their earnings after a 10-year period
'''
investment = float(input('The investment amount: $'))

interest_rate = float(input('The interest rate: ')) * .01

for i in range(10):
    investment = investment + investment * interest_rate

print('Your earnings after 10 years: ${:.2f}'.format(investment))

print('\n*****************************************\n')

''' The order of operations:

1: exponentiation & root extraction

2: multiplication & division

3: addition & subtraction
'''
print('2 + (3 * 4) -> ', 2 + (3 * 4))

print('(2 + 3) * 4 -> ', (2 + 3) * 4)

print('2 + 3 * 4 -> ', 2 + 3 * 4)