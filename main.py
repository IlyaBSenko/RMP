import random
from operator import *
import time

ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": truediv,
        "//": floordiv,
        "%": mod,
        "**": pow,
        "<<": lshift,
        ">>": rshift,
        "^": xor,
        "&": and_,
        "|": or_   
}

def fast():
    n = int(input("Please enter a number (prefferably very large) for the computer to generate random math problems on: "))
    for i in range(1, n + 1):
        rand1 = random.randint(1, 10)
        rand2 = random.randint(1, 20)
        
        symb = random.choice(list(ops.keys()))
        func = ops[symb]
        answer = func(rand1, rand2)
        
        print(f" {rand1} {symb} {rand2} to get {answer}")
        
def slow():
    n = int(input("Please enter a number (prefferably very large) for the computer to generate random math problems on: "))
    for i in range(1, n + 1):
        rand1 = random.randint(1, 10)
        rand2 = random.randint(1, 20)
        
        symb = random.choice(list(ops.keys()))
        func = ops[symb]
        answer = func(rand1, rand2)
        
        print(f" {rand1} {symb} {rand2} to get {answer}")
        time.sleep(0.001)
    

def main():
    # TODO: add fast / slow mode for whether user wants fast output or slow output (fast = default, slow = time.sleep(1.5) or something)
    speed = input("Would you like fast or slow: ")
    if speed == "fast":
        fast()
    elif speed == "slow":
        slow()


if __name__ == "__main__":
    main()