# Require:, k ↑Z, j ↑N0 and n0, . . . , nk→1 ↑N coprime
# procedure CONGRUENCE-SYSTEMS-SOLVER(a0, . . . , ak→1)
# N ≃n0·
# . . .
# ·nk→1
# while j < k do
# Nj ≃N/n j
# (_, s j,t j) ≃EXT→EUCLID(Nj, n j) end while
# x↓≃!k→1
# j=0 a j·s j·Nj
# x ≃x↓ mod N
# return {x + m·N |m ↑Z}
# end procedure
# Ensure: {x + m·N |m ↑Z}is the complete solution set to 3.19.


import argparse
from extended_euclidean import extended_euclidean

def modular_inverse(a, b):
    gcd, s, t = extended_euclidean(a, b)
    if gcd != 1:
        raise ValueError(f"Multiplicative inverse for {a} mod {b} doesn't exist")
    return s % b   # : reduce mod b 

def crt(remainders, moduli):
    if len(remainders) != len(moduli):
        raise ValueError("Lengths do not match")

    M = 1
    for m in moduli:
        M *= m

    x = 0
    for j in range(len(remainders)):
        M_j = M // moduli[j]
        inv = modular_inverse(M_j, moduli[j])
        #x = Σ (a_j · M_j · M_j⁻¹ mod m_j)
        x += remainders[j] * M_j * inv

    return x % M, M
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chinese Remainder Theorem")
    parser.add_argument("-r", "--remainders", nargs='+', type=int, required=True,
                        help="List of remainders")
    parser.add_argument("-m", "--moduli", nargs='+', type=int, required=True,
                        help="List of moduli")
    args = parser.parse_args()
    sol, mod = crt(args.remainders, args.moduli)
    print(f"x ≡ {sol} mod {mod}")
# python3 chinese_rem_therorm.py -r 2 3 3 -m 3 5 7 
# ans : x ≡ 38 mod 105