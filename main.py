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
    n = int(input("Please enter a large number for the computer to generate random math problems on: "))
    ops_count = {
        "+": 0,
        "-": 0,
        "*": 0,
        "/": 0,
        "//": 0,
        "%": 0,
        "**": 0,
        "<<": 0,
        ">>": 0,
        "^": 0,
        "&": 0,
        "|": 0   
    }
    for i in range(1, n + 1):
        rand1 = random.randint(5, 10)
        rand2 = random.randint(10, 20)
        
        symb = random.choice(list(ops.keys()))
        ops_count[symb] = ops_count.get(symb, 0) + 1
        func = ops[symb]
        answer = func(rand1, rand2)
        
        print(f"Line {i}: {rand1} {symb} {rand2} to get {answer}")
    for symb in ops:
        if ops_count[symb] > 0:
            print(f"{symb} was used {ops_count[symb]} amount of times.")
        
def slow():
    n = int(input("Please enter a large number for the computer to generate random math problems on: "))
    ops_count = {
        "+": 0,
        "-": 0,
        "*": 0,
        "/": 0,
        "//": 0,
        "%": 0,
        "**": 0,
        "<<": 0,
        ">>": 0,
        "^": 0,
        "&": 0,
        "|": 0   
    }
    for i in range(1, n + 1):
        rand1 = random.randint(5, 10)
        rand2 = random.randint(10, 20)
        
        symb = random.choice(list(ops.keys()))
        ops_count[symb] = ops_count.get(symb, 0) + 1
        func = ops[symb]
        answer = func(rand1, rand2)
        
        print(f"Line {i}: {rand1} {symb} {rand2} to get {answer}")
        time.sleep(0.001)
    for symb in ops:
        if ops_count[symb] > 0:
            print(f"{symb} was used {ops_count[symb]} amount of times.")
            print('Slow mode is "slow" because its waiting 1 millisecond in between each print')
    

def main():
    speed = input("Would you like fast or slow: ")
    if speed == "bogo":
        bogo_secret()
    if speed == "fast":
        fast()
    elif speed == "slow":
        slow()

# secret function ooo
# fix the time taken function
def bogo_secret():
    arr_size = int(input("Enter the array size: "))
    new_arr = []
    for n in range(arr_size):
        i = random.randint(0, 20)
        new_arr.append(i)

    start_time = time.perf_counter()
    while new_arr != sorted(new_arr):
        random.shuffle(new_arr)
        print(new_arr)

    end_time = time.perf_counter()
    time_taken = end_time - start_time
    if time_taken > 1:
        new_time = time_taken
        print(f"It took {new_time:.2f} seconds")
    elif time_taken > 60:
        new_time = time_taken / 60
        print(f"It took {new_time:.2f} minutes")
    else:
        print(f"Took {time_taken:.5f} milliseconds")

if __name__ == "__main__":
    main()
    # bogo_secret()
