#Exercise 7 (Binary Representation). Write an algorithm that computes the binary representation 3.13 of any non-negative integer  n= k-1 sum _sub(j=0) b_sub(j).2^j
import argparse

def to_binary(n,rev=True) -> list[int]:
    assert n >= 0
    if n == 0:
        return [0]
    arr = []
    while n > 0:
        r = n % 2
        arr.append(r)
        n = n // 2
    if rev :
        arr.reverse()
        return arr  # Reverse to get MSB-first
    return arr
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute binary")
    parser.add_argument("a", type=int, help="number")
    args = parser.parse_args()
    arr = to_binary(args.a)
    q =''.join(list(map(str, arr)))
    print(f"{args.a} = {q} in binary")