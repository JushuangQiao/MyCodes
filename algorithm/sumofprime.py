# coding=utf-8
# 求100以内的素数和

from math import sqrt


def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def sumofprime(num):
    return sum(filter(isprime, xrange(num)))


if __name__ == '__main__':
    print sumofprime(6)
