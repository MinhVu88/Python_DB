# CLASSES & OBJECTS
class Dog:
    def __init__(self, name='', height = 0, weight = 0):
        self.name = name
        self.height = height
        self.weight = weight
    
    def run(self):
        print('\n{} runs quickly'.format(self.name))
    
    def sniff(self):
        print('\n{} sniffs the ground'.format(self.name))
    
    def bark(self):
        print('\n{} barks loudly'.format(self.name))

def main_1():
    dog1 = Dog('Laika', 23, 7)

    dog1.sniff()

main_1()

print('\n*****************************************\n')

class Square:
    def __init__(self, height = '0', width = '0'):
        self.height = height
        self.width = width
    
    @property
    def height(self):
        print('\nRetrieving the height')
        return self.__height
    
    @height.setter
    def height(self, val):
        if val.isdigit():
            self.__height = val
        else:
            print('\nnumeric values only for height')
    
    @property
    def width(self):
        print('\nRetrieving the width')
        return self.__width
    
    @width.setter
    def width(self, val):
        if val.isdigit():
            self.__width = val
        else:
            print('\nnumeric values only for width')
    
    def get_area(self):
        return int(self.__height) * int(self.__width)

def main_2():
    square = Square()

    square.height = input('\nEnter height: ')

    square.width = input('\nEnter width: ')

    print('\nHeight: ', square.height)

    print('\nWidth: ', square.width)

    print('\nThe square area: ', square.get_area())

main_2()