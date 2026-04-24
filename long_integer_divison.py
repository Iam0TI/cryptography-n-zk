# Determine the sign of the quotient, then work with the absolute values of the dividend and divisor.
# Divide the first digit of the dividend by the divisor. If the divisor is larger than the first digit of the dividend, divide the first two digits of the dividend by the divisor, and so on.
# Write the quotient above the dividend.
# Multiply the quotient by the divisor and write the product under the dividend.
# Subtract that product from the dividend.
# Bring down the next digit of the dividend.
# Repeat from Step 1 until there are no more digits in the dividend to bring down.
# Check by multiplying the quotient times the divisor.
# Add the sign of division to the quotient of the absolute values.
# def compute(number,divisor):
#     if divisor == 0:
#         raise ValueError("Division by zero is undefined")

#     absn = get_abosolute(number)
#     absd = get_abosolute(divisor)
#     quoient = absn // absd
#     remainder = absn % absd
  
#     if (number < 0 or divisor < 0):
      
#         quoient = quoient + 1
#         remainder= divisor - remainder
#     quoient =  quoient * get_sign(number,divisor)
#     return divisor,number,remainder,quoient

# def get_abosolute(number):
#     if number > 0:
#         return number
#     else:
#        return number * -1
# def get_sign(a,b):
#     if a < 0 and  b > 0:
#         return -1
#     elif a < 0 and b < 0:   
#         return 1
#     elif a > 0 and b < 0:
#         return -1
#     elif a >0 and b > 0:
#         return 1
import argparse

def long_div(a, b):
    if b == 0:
        raise ValueError("Division by zero is undefined")

    # get divisor and 
    q = a // b
    r = a % b

    # to ensure 0 ≤ r < |b| but i don't this code will ever be rreach
    if r < 0:
        if b > 0:
            q -= 1
            r += b
        else:
            q += 1
            r -= b
    assert a == q*b+r
    return q, r
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute quotient and remainder")
    parser.add_argument("a", type=int, help="Dividend")
    parser.add_argument("b", type=int, help="Divisor")
    args = parser.parse_args()
    q, r = long_div(args.a, args.b)
    print(f"q = {q}, r = {r}")
    print(f"{args.a} = {q} * {args.b} + {r}")

## run python3 long_integer_divison.py  a b