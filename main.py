# Dylan Stitt
# Unit 4 Lab 7
# Deque Class

# Implementation & testing of the Deque class

from DequeClass import Deque
from TEST_CODE import *
import os

def main():
    testDEQ = Deque()

    # TEST 1 - Test privacy
    # BEFORE TESTING: implement __init__, __is_empty(), __resize()
    # Methods can just contain pass
    TEST_privacy(testDEQ)

    # TEST 2 - Test queue creation
    # BEFORE TESTING: implement __len__, __str__, .first(), .last()
    TEST_new_deq(testDEQ)

    # TEST 3 - Test add_last
    # BEFORE TESTING: implement .add_last(), .__resize(), .last()
    TEST_add_last(testDEQ)

    # TEST 4 - Test add_first
    # BEFORE TESTING: implement .add_first(), .__resize(), .first()
    TEST_add_first(testDEQ)

    # TEST 5 - Test delete_last
    # BEFORE TESTING: implement delete_last()
    TEST_delete_last(testDEQ)

    # TEST 6 - Test add_first again
    # BEFORE TESTING: implement .add_first()
    TEST_add_first2(testDEQ)

    # TEST 7 - Test delete_first
    # BEFORE TESTING: implement delete_first()
    TEST_delete_first(testDEQ)

    # TEST 8 - Test add_last again
    # BEFORE TESTING: implement .add_last()
    TEST_add_last2(testDEQ)

    # TEST 9 - Test docstrings
    # BEFORE TESTING: implement all methods & docstrings
    TEST_docs(testDEQ)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
