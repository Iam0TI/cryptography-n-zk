#Exercise 7 (Binary Representation). Write an algorithm that computes the binary representation 3.13 of any non-negative integer  n= k-1 sum _sub(j=0) b_sub(j).2^j
import argparse

def to_binary(n):
    assert n >= 0
    if n == 0:
        return "0"
    arr = []
    while n > 0:
        r = n % 2
        arr.append(r)
        n = n // 2
    arr.reverse()  # Reverse to get MSB-first
    return ''.join(map(str, arr))

parser = argparse.ArgumentParser(description="Compute binary")
parser.add_argument("a", type=int, help="number")
args = parser.parse_args()
q = to_binary(args.a)
print(f"{args.a} = {q} in binary")