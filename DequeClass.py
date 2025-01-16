# Dylan Stitt
# Unit 4 Lab 7
# Deque Class

class Deque:

    def __init__(self):
        """Constructor for Deque"""
        self.__capacity = 5
        self.__size = 0
        self.__front = 0
        self.__deque = [None for i in range(self.__capacity)]

    def __str__(self):
        """Converts deque into printable string"""
        out = "FRONT> "
        pointer = self.__front
        for i in range(self.__size):
            out += str(self.__deque[pointer]) + " "
            pointer = (pointer + 1) % self.__capacity

        return out + "<BACK"

    def __len__(self):
        """Returns the length of the Deque"""
        return self.__size

    def first(self):
        """Returns the first element of the Deque"""
        if self.__is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.__deque[self.__front]
    
    def last(self):
        """Returns the last element of the Deque"""
        if self.__is_empty():
            raise IndexError("Deque is empty")
        else:
            return self.__deque[(self.__size+self.__front-1)%self.__capacity]

    def add_last(self, item):
        """Adds item to the Deque"""
        if self.__size == self.__capacity:
            self.__resize()
        self.__deque[(self.__front+self.__size)%self.__capacity] = item
        self.__size += 1

    def delete_last(self):
        """Deletes the last element of the Deque"""
        if self.__is_empty():
            raise IndexError("Deque is empty")
        else:
            val = self.__deque[(self.__size+self.__front-1)%self.__capacity]
            self.__deque[(self.__size+self.__front-1)%self.__capacity] = None
            self.__size -= 1
            return val

    def add_first(self, item):
        """Adds item to the front of the Deque"""
        if self.__size == self.__capacity:
            self.__resize()

        if not self.__is_empty():
            self.__front = (self.__front-1)%self.__capacity

        self.__deque[self.__front] = item
        self.__size += 1

    def delete_first(self):
        """Removes and returns the first element of the Deque"""
        if self.__is_empty():
            raise IndexError("Deque is empty")
        else:
            val = self.__deque[self.__front]
            self.__deque[self.__front] = None
            self.__front += 1
            self.__front %= self.__capacity
            self.__size -= 1
            return val

    def __is_empty(self):
        """Checks if the Deque is empty"""
        if self.__size == 0:
            return True
        return False

    def __resize(self):
        """Resizes the Deque when it reaches capacity"""
        cap = self.__capacity*2
        size = self.__size

        new = [None for i in range(cap)]
        for i in range(self.__size):
            new[i] = self.delete_first()

        self.__front = 0
        self.__size = size
        self.__capacity = cap
        self.__deque = new
