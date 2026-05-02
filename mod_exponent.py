# Write a computer program to calculate a^x (mod n) by the method of repeated squares.
# What are the largest values of n and x that your program will accept?

import argparse
from get_bin_sum import get_bin_sum

def mod_exp(a,x,n) -> int:
    if n <= 0:
        raise ValueError("modulus n must be positive")
    if x < 0:
        raise ValueError("exponent x must be non-negative")
    if x == 0:
        return 1 % n
    #conver to bin and get the sum of power
    pow_of_2 = get_bin_sum(x)
    arr= [] 
    inner = a % n
    ## get the relevant of a **(2** i) mod(n)
    for i in range(0,max(pow_of_2)+1):
        if i > 0 :
            inner = mod_mul(inner,inner, n)
        if i in pow_of_2:
            arr.append(inner)
    ## compute for a **(2** i) mod(n) to get  a **x mod(n)
    return mod_mul_from_list(arr,n)

def mod_mul(a, b, n) -> int:
    return (a * b) % n

def mod_mul_from_list(values, n) -> int:
    result = 1
    for value in values:
        result = mod_mul(result, value, n)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute mod exponent")
    parser.add_argument("a", type=int, help="number")
    parser.add_argument("x", type=int, help="exponent")
    parser.add_argument("n", type=int, help="modulo")
    args = parser.parse_args()
    q = mod_exp(args.a, args.x,args.n)
    # print(f"q = {q}, r = {r}")
    print(f"{args.a}^{args.x} mod({args.n}) = {q}")

# python3 mod_exponent.py 271 321 481
# 271^321 mod(481) = 47