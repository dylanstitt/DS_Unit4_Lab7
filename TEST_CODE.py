##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''


##################################

def result(flag):
    if flag:
        return f"{G}PASSED{W}"

    return f"{R}FAILED{W}"


def TEST_privacy(DEQobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Privacy{W}\n")

    try:
        DEQobj._Deque__deque
        print(f"{W}Deque array is private: {G}PASSED{W}")
    except:
        print(f"{W}Deque array is private: {R}FAILED{W}")

    try:
        DEQobj._Deque__size
        print(f"{W}Deque size is private: {G}PASSED{W}")
    except:
        print(f"{W}Deque size is private: {R}FAILED{W}")

    try:
        DEQobj._Deque__capacity
        print(f"{W}Deque capacity is private: {G}PASSED{W}")
    except:
        print(f"{W}Deque capacity is private: {R}FAILED{W}")

    try:
        DEQobj._Deque__front
        print(f"{W}Deque front is private: {G}PASSED{W}")
    except:
        print(f"{W}Deque front is private: {R}FAILED{W}")

    try:
        DEQobj._Deque__is_empty()
        print(f"\n{W}is_empty() is private: {G}PASSED{W}")
    except:
        print(f"\n{W}is_empty() is private: {R}FAILED{W}")

    try:
        DEQobj.resize()
        print(f"{W}resize() is private: {R}FAILED{W}")
    except:
        print(f"{W}resize() is private: {G}PASSED{W}")

    print("~" * 50, "\n\n")


def TEST_new_deq(DEQobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Deque Creation{W}\n")

    print(f"{B}Initial Deque: {DEQobj}{W}\n")

    test = len(DEQobj) == 0
    print(f"Initial deque contains ZERO elements: {result(test)}")

    test = str(DEQobj) == "FRONT> <BACK"
    print(f"Correct to-string method: {result(test)}")

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    test = cap == 5
    print(f"New deque has a capacity of 5: {result(test)}")

    test = front == 0
    print(f"New deque's front is index 0: {result(test)}")

    try:
        DEQobj.first()
        print(f"first() unavailable with empty deque: {R}FAILED{W}")
    except:
        print(f"first() unavailable with empty deque: {G}PASSED{W}")

    try:
        DEQobj.last()
        print(f"last() unavailable with empty deque: {R}FAILED{W}")
    except:
        print(f"last() unavailable with empty deque: {G}PASSED{W}")

    print("~" * 50, "\n\n")


def TEST_add_last(DEQobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: add_last{W}\n")

    DEQobj.add_last("A")
    DEQobj.add_last("B")
    DEQobj.add_last("C")
    print(f"{B}Deque of 3 elements: {DEQobj}{W}\n")

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    test = True
    for i, el in enumerate("ABC"):
        if deq[i] != el:
            test = False

    print(f"Elements added to back: {result(test)}")

    test = len(DEQobj) == 3
    print(f"add_last() affects size: {result(test)}")

    for el in "WXYZ":
        DEQobj.add_last(el)

    print(f"\n{B}Deque of 7 elements: {DEQobj}{W}\n")

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    test = cap == 10
    print(f"Capacity doubles when deque is full: {result(test)}")

    test = front == 0
    print(f"Deque's front not affected by add_last(): {result(test)}")

    test = deq[0] == "A" and deq[6] == "Z"
    print(f"Deque array is organized properly: {result(test)}")

    test = DEQobj.first() == "A"
    print(f"first() returns the correct value: {result(test)}")

    test = DEQobj.last() == "Z"
    print(f"last() returns the correct value: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_add_first(DEQobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: add_first{W}\n")

    print(f"{B}Current Deque: {DEQobj}{W}\n")

    DEQobj.add_first("L")

    print(f"{B}Element added with add_first: {DEQobj}{W}\n")

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    test = DEQobj.first() == "L"
    print(f"Elements added to front: {result(test)}")

    test = cap == 10 and front == 9 and deq[front] == "L"
    print(f"New front added in correct position: {result(test)}")

    test = len(DEQobj) == 8
    print(f"add_first() affects size: {result(test)}")

    for el in "MNOP":
        DEQobj.add_first(el)

    print(f"\n{B}Updated Deque: {DEQobj}{W}\n")

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    test = cap == 20
    print(f"Capacity doubles when deque is full: {result(test)}")

    test = front == 18
    print(f"Front pointer properly affected by add_first: {result(test)}")

    test = "".join(deq[:4]) == "NMLA" and "".join(deq[-2:]) == "PO"
    print(f"Deque array is properly organized: {result(test)}")

    test = DEQobj.first() == "P"
    print(f"first() returns the correct value: {result(test)}")

    test = DEQobj.last() == "Z"
    print(f"last() returns the correct value: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_delete_last(DEQobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: delete_last{W}\n")

    print(f"{B}Current Deque: {DEQobj}{W}\n")

    ele = DEQobj.delete_last()

    print(f"{B}Last element was deleted: {DEQobj}{W}\n")

    test = ele == "Z"
    print(f"Correct element was deleted: {result(test)}")

    test = len(DEQobj) == 11
    print(f"delete_last() affects Deque size: {result(test)}")

    test = DEQobj.first() == "P"
    print(f"first() returns the correct value: {result(test)}")

    test = DEQobj.last() == "Y"
    print(f"last() returns the correct value: {result(test)}")

    expected = "YXWCBALMNOP"
    test = True
    for let in expected:
        ele = DEQobj.delete_last()
        if let != ele:
            test = False

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    print(f"\n{B}Deque was emptied: {DEQobj}{W}\n")

    print(f"Elements are removed from Deque correctly: {result(test)}")

    noneTest = True
    for el in deq:
        if el != None:
            noneTest = False

    test = len(DEQobj) == 0 and noneTest
    print(f"Deque array contains only None: {result(test)}")

    test = front == 18
    print(f"delete_last() does not impact front pointer: {result(test)}")

    try:
        ele = DEQobj.delete_last()
        print(f"Delete from empty Deque raises exception: {R}FAILED{W}")
    except:
        print(f"Delete from empty Deque raises exception: {G}PASSED{W}")

    print("~" * 50, "\n\n")


def TEST_add_first2(DEQobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Re-test add_first{W}\n")

    print(f"{B}Current Deque: {DEQobj}{W}\n")

    DEQobj.add_first("A")

    print(f"{B}One element was added: {DEQobj}{W}\n")

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    test = front == 18 and deq[front] == "A"
    print(f"add_first() inserts at index front when deque is empty: {result(test)}")

    for el in "BCDE":
        DEQobj.add_first(el)

    print(f"\n{B}Four elements were added: {DEQobj}{W}\n")

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    test = deq[18] == "A" and deq[14] == "E" and deq[-1] == None
    print(f"Elements were populated in the array correctly: {result(test)}")

    test = cap == 20 and len(DEQobj) == 5
    print(f"Size and capacity are correct: {result(test)}")

    for el in "ABCDEFGHIJKLMNO":
        DEQobj.add_first(el)

    print(f"\n{B}Deque is full: {DEQobj}{W}\n")

    DEQobj.add_first("X")

    print(f"{B}One element was added: {DEQobj}{W}\n")

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    test = cap == 40 and len(DEQobj) == 21
    print(f"Capacity doubled: {result(test)}")

    test = deq[0] == "O" and front == 39 and deq[front] == "X"
    print(f"Resize sets the front to index 0: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_delete_first(DEQobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: delete_first{W}\n")

    print(f"{B}Current Deque: {DEQobj}{W}\n")

    ele = DEQobj.delete_first()

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    print(f"{B}First element was deleted: {DEQobj}{W}\n")

    test = ele == "X"
    print(f"Correct element was deleted: {result(test)}")

    test = len(DEQobj) == 20
    print(f"delete_first() affects Deque size: {result(test)}")

    test = front == 0 and DEQobj.first() == "O"
    print(f"delete_first() moves the front pointer: {result(test)}")

    test = DEQobj.first() == "O"
    print(f"first() returns the correct value: {result(test)}")

    test = DEQobj.last() == "A"
    print(f"last() returns the correct value: {result(test)}")

    test = True
    for el in "ONMLKJIHGFEDCBAEDCBA":
        let = DEQobj.delete_first()
        if let != el:
            test = False

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    print(f"\n{B}Deque was emptied: {DEQobj}{W}\n")

    print(f"Elements are removed from Deque correctly: {result(test)}")

    noneTest = True
    for el in deq:
        if el != None:
            noneTest = False

    test = len(DEQobj) == 0 and noneTest
    print(f"Deque array contains only None: {result(test)}")

    test = front == 20
    print(f"delete_first() modifies front pointer: {result(test)}")

    try:
        ele = DEQobj.delete_first()
        print(f"Delete from empty Deque raises exception: {R}FAILED{W}")
    except:
        print(f"Delete from empty Deque raises exception: {G}PASSED{W}")

    print("~" * 50, "\n\n")


def TEST_add_last2(DEQobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Re-test add_last{W}\n")

    print(f"{B}Current Deque: {DEQobj}{W}\n")

    DEQobj.add_last("A")

    print(f"{B}One element was added: {DEQobj}{W}\n")

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    test = front == 20 and deq[front] == "A"
    print(f"add_last() inserts at index front when deque is empty: {result(test)}")

    for el in "BCDE":
        DEQobj.add_last(el)

    print(f"\n{B}Four elements were added: {DEQobj}{W}\n")

    cap = DEQobj._Deque__capacity
    front = DEQobj._Deque__front
    deq = DEQobj._Deque__deque

    test = deq[20] == "A" and deq[24] == "E" and deq[-1] == None
    print(f"Elements were populated in the array correctly: {result(test)}")

    test = cap == 40 and len(DEQobj) == 5
    print(f"Size and capacity are correct: {result(test)}")

    print("~" * 50, "\n\n")


def TEST_docs(DEQobj):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Docstrings{W}\n")

    doc = DEQobj.add_first.__doc__
    if doc != None:
        print(f"{B}add_first() Documentation:{W} {doc}\n")
    else:
        print(f"{R}add_first() Documentation Missing{W}\n")

    doc = DEQobj.add_last.__doc__
    if doc != None:
        print(f"{B}add_last() Documentation:{W} {doc}\n")
    else:
        print(f"{R}add_last() Documentation Missing{W}\n")

    doc = DEQobj.delete_first.__doc__
    if doc != None:
        print(f"{B}delete_first() Documentation:{W} {doc}\n")
    else:
        print(f"{R}delete_first() Documentation Missing{W}\n")

    doc = DEQobj.delete_last.__doc__
    if doc != None:
        print(f"{B}delete_last() Documentation:{W} {doc}\n")
    else:
        print(f"{R}delete_last() Documentation Missing{W}\n")

    doc = DEQobj.first.__doc__
    if doc != None:
        print(f"{B}first() Documentation:{W} {doc}\n")
    else:
        print(f"{R}first() Documentation Missing{W}\n")

    doc = DEQobj.last.__doc__
    if doc != None:
        print(f"{B}last() Documentation:{W} {doc}\n")
    else:
        print(f"{R}last() Documentation Missing{W}\n")

    doc = DEQobj._Deque__resize.__doc__
    if doc != None:
        print(f"{B}resize() Documentation:{W} {doc}\n")
    else:
        print(f"{R}resize() Documentation Missing{W}\n")

    doc = DEQobj._Deque__is_empty.__doc__
    if doc != None:
        print(f"{B}is_empty() Documentation:{W} {doc}\n")
    else:
        print(f"{R}is_empty() Documentation Missing{W}\n")

    doc = DEQobj.__len__.__doc__
    if doc != None:
        print(f"{B}len() Documentation:{W} {doc}\n")
    else:
        print(f"{R}len() Documentation Missing{W}\n")

    doc = DEQobj.__str__.__doc__
    if doc != None:
        print(f"{B}str() Documentation:{W} {doc}\n")
    else:
        print(f"{R}str() Documentation Missing{W}\n")

    print("~" * 50, "\n\n")