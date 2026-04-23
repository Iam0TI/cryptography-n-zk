# Algorithm 1 Extended Euclidean Algorithm
# Require: a, b ↑N with a ↗b
# procedure EXT-EUCLID(a, b)
# r0 ≃a and r1 ≃b
# s0 ≃1 and s1 ≃0
# t0 ≃0 and t1 ≃1
# k ≃2
# while rk→1 ↔= 0 do
# qk ≃rk→2 div rk→1
# rk ≃rk→2 mod rk→1
# sk ≃sk→2→qk·sk→1
# tk ≃tk→2→qk·tk→1
# k ≃k + 1
# end while
# return gcd(a, b) ≃rk→2, s ≃sk→2 and t ≃tk→2
# end procedure
# Ensure: gcd(a, b) = s·a + t·b
import argparse
# import long_div

def extended_euclidean(a, b):
    if b < 0 or a < 0:
        raise ValueError("Division by zero is undefined")
    original_a, original_b = a, b
    #given the gcd(a,b) = as + bt for any gcd(n,0) = n1 + 0t we will limit t to 0
    if b == 0 and a == 0:
        return (0, 0, 0) 
    if b == 0 or a == 0:
        return (b, 1, 0) if b > a else (a, 1,0)
    a, b = minmax(a,b)
    r = []
    s = []
    t = []
    r.append(a)
    r.append(b)
    s.append(1)
    s.append(0)
    t.append(0)
    t.append(1)
    k = 2
    while r[k-1] != 0:
        q = r[k-2] // r[k-1]
        r.append(r[k-2] % r[k-1])
        s.append(s[k-2] - q * s[k-1])
        t.append(t[k-2] - q * t[k-1])
        k += 1
    gcd = r[k-2]
    coeff_s = s[k-2]
    coeff_t = t[k-2]
    # Adjust coefficients for original order
    if original_b > original_a:
        coeff_s, coeff_t = coeff_t, coeff_s
    return gcd, coeff_s, coeff_t

def minmax(a, b):
    return (b, a) if b > a else (a, b)

parser = argparse.ArgumentParser(description="Compute EEA")
parser.add_argument("a", type=int, help="Dividend")
parser.add_argument("b", type=int, help="Divisor")
args = parser.parse_args()
gcd, s, t = extended_euclidean(args.a, args.b)
print(f"gcd{minmax(args.a, args.b)} = {gcd}, s = {s}, t = {t}")
print(f"{gcd} = {s} * {args.a} + {t} * {args.b}")