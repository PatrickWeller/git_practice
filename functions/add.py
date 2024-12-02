# Script to add two numbers

import argparse

def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    args = parser.parse_args()

    result = add_numbers(args.num1, args.num2)
    print(f"The result is: {result}")
