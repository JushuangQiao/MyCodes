# coding=utf-8
# Stein 算法求最大公约数


def gcd(a, b):
    c = 1
    while a and b:
        if a % 2 == 0 and b % 2 == 0:
            a >>= 1
            b >>= 1
            c <<= 1
        elif a % 2 == 0 and b % 2 != 0:
            a >>= 1
        elif b % 2 == 0 and a % 2 != 0:
            b >>= 1
        else:
            b = min(a, b)
            a = abs(a-b)
    c *= max(a, b)
    return c


# 最小公倍数
def lcm(a, b):
    return a / gcd(a, b) * b
