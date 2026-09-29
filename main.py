"""
How to use this program: (Rough idea)
user types in a number:
If input is 5 (arbitrary number), then the program outputs:
Soving {rand_number} {rand_operation} {rand_number} to get {output} Line 1
Soving {rand_number} {rand_operation} {rand_number} to get {output} Line 2 
Soving {rand_number} {rand_operation} {rand_number} to get {output} Line 3
Soving {rand_number} {rand_operation} {rand_number} to get {output} Line 4
Soving {rand_number} {rand_operation} {rand_number} to get {output} Line 5
"""

[
    [   # Level 1: Easy Operations
        "+",
        "-",
        "*",
        "/",
        "//",
        "%",
        "**"
    ],
    [
        "math.sqrt()",
        "math.log()",
        "math.pow()",
        "math.sin()",
        "math.cos()",
        "math.tan()",
        "math.factorial()",
        "math.comb()",
        "math.perm()"
    ]
]

def main():
    # TODO: add fast / slow mode for whether user wants fast output or slow output (fast = default, slow = time.sleep(1.5) or something)
    n = int(input("Please enter a number (prefferably very large) for the computer to generate random math problems on:"))
    for i in range(n + 1):
        print(i)



if __name__ == "__main__":
    main()


