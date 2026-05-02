# Write a computer program that will write any decimal number as the sum of distinct
# powers of 2. What is the largest integer that your program will handle?
import argparse
from binary_rep import to_binary

def get_bin_sum(n: int) -> list[int]:
    arr = to_binary(n,False)
    arr2 = []
    for i,var in enumerate(arr):
       if var == 1 :
        arr2.append(i)
    return arr2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sum of power of 2")
    parser.add_argument("a", type=int, help="number")
    args = parser.parse_args()
    
    q = get_bin_sum(args.a)
    print(f"{args.a} = {' + '.join(f'2^{i}' for i in reversed(q))}")