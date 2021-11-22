import random
from insertion import *
from selection import *

def main():
    print("Select a arrangement configuration:\n")
    print("1 - Random\n")
    print("2 - Inverted\n")
    print("3 - Crescent\n")
    print("4 - Decrescent\n")

    x = int(input());
    
    print("\n")

    vector = random.sample(range(10), 10)

    if x == 1:
        pass
    elif x == 2:
        vector.reverse()
    elif x == 3:
        vector.sort()
    elif x == 4:
        vector.sort()
        vector.reverse()
    else:
        print("Non existent configuration\n")

    print("Select a algorithm\n")
    print("1 - Insertion Sort\n")
    print("2 - Selection Sort\n")
    
    y = int(input())

    if y == 1:
        insertion(vector)
    elif y == 2:
        selection(vector)
    else:
        print("Non existent algorithm\n")


if __name__ == "__main__":
    main()