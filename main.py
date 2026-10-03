import random
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


def main():
    # TODO: add fast / slow mode for whether user wants fast output or slow output (fast = default, slow = time.sleep(1.5) or something)
    n = int(input("Please enter a number (prefferably very large) for the computer to generate random math problems on:"))
    for i in range(1, n + 1):
        rand1 = random.randint(1, 10)
        rand2 = random.randint(1, 20)
        
        symb = random.choice(list(ops.keys()))
        func = ops[symb]
        answer = func(rand1, rand2)
        
        print(f" {rand1} {symb} {rand2} to get {answer}")


if __name__ == "__main__":
    main()