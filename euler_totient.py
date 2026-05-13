# The Euler φ-function is the map φ : N → N defined by φ(n) = 1 for n = 1, and, for n > 1,
# φ(n) is the number of positive integers m with 1 ≤ m < n and gcd(m, n) = 1.
from extended_euclidean import extended_euclidean
import argparse


# so it returns a tuple of the invertible numbers and the numbers
def invertible_numbers_mod_n(n):
    assert n > 0
    if n == 1:
        return [1],1
    arr = []
    for i in range(n):
        gcd,s,t  = extended_euclidean(i,n)
        if gcd == 1:
            arr.append(i) 
    return arr, len(arr)

# print(invertible_numbers_mod_n(10))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute the invertible numbers modulo n and Euler's totient φ(n).")
    parser.add_argument("n", type=int,help="The modulus n. Must be a positive integer.",)
    args = parser.parse_args()
    numbers, phi = invertible_numbers_mod_n(args.n)
    print(f"Invertible numbers modulo {args.n}: {numbers}")
    print(f"φ({args.n}) = {phi}")