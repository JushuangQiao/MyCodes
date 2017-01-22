# coding=utf-8

from math import sqrt


def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def getret(n):
    ret = []
    if isprime(n):
        ret.append(n)
    m = n
    for i in range(2, int(sqrt(n))+1):
        if isprime(i):
            while m % i == 0:
                ret.append(i)
                m /= i
                if isprime(m):
                    ret.append(m)
                    print ret


if __name__ == '__main__':
    getret(12345678901234)
