# coding=utf-8
# n%2=1，n%3=2, n%4=3, n%5=4, n%6=5, n%7=0, 求n


def getn():
    for i in xrange(1, 2**32-1):
        n = 7 * i
        if n % 2 == 1 and n % 3 == 2 and n % 4 == 3 and n % 5 == 4 and n % 6 == 5:
            return n

if __name__ == '__main__':
    print getn()
