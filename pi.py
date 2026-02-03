#!/usr/bin/env python3
from decimal import Decimal, getcontext

def compute_pi(digits: int) -> str:
    extra = 10
    getcontext().prec = digits + extra
    C = 426880 * Decimal(10005).sqrt()
    K = 6
    M = 1
    L = 13591409
    X = 1
    S = Decimal(L)
    for i in range(1, digits // 14 + 2):
        M = (M * (K**3 - 16 * K)) // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12
    pi = C / S
    pi_str = format(pi, 'f')
    if '.' not in pi_str:
        pi_str += '.'
    integer, fractional = pi_str.split('.')
    fractional = fractional[:digits].ljust(digits, '0')
    return f"{integer}.{fractional}"


def main() -> None:
    digits = 100000
    pi_value = compute_pi(digits)
    print(pi_value)


if __name__ == "__main__":
    main()
