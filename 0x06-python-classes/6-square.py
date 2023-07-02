#!/usr/bin/python3
"""Define a class called Square"""


class Square:
    """Represents an empty square."""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (len(position) != 2 or type(position[0]) != int or type(position[0]) != int or
                position[0] < 0 or position[1] < 0):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size*self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    @property
    def position(self):
        return self.__position
    
    @position.setter    
    def position(self, value):
        if len(value) != 2 or value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__position[1] > 0:
            print("\n"*(self.__position[1]-1))
        for i in range(self.__size):
            print(" "*(self.__position[0]), end="")
            print("#"*self.__size, end="")
            print()
        if self.__size == 0:
            print()
