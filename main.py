import random
import time
from operator import *

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
    n = int(input("Please enter a number for the computer to generate random math problems on: "))
    for i in range(1, n + 1):
        rand1 = random.randint(5, 10)
        rand2 = random.randint(10, 20)
        
        symb = random.choice(list(ops.keys()))
        func = ops[symb]
        answer = func(rand1, rand2)
        
        print(f"Line {i}: {rand1} {symb} {rand2} to get {answer}")
        
def slow():
    n = int(input("Please enter a number for the computer to generate random math problems on: "))
    for i in range(1, n + 1):
        rand1 = random.randint(5, 10)
        rand2 = random.randint(10, 20)
        
        symb = random.choice(list(ops.keys()))
        func = ops[symb]
        answer = func(rand1, rand2)
        
        print(f"Line {i}: {rand1} {symb} {rand2} to get {answer}")
        time.sleep(0.001)
    

def main():
    speed = input("Would you like fast or slow: ")
    if speed == "fast":
        fast()
    elif speed == "slow":
        slow()


if __name__ == "__main__":
    main()