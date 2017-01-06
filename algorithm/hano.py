# coding=utf-8


def move(n, a, b, c):
    assert n > 0, 'n must be positive integer!'
    if n == 1:
        print a + '->' + c
        return
    move(n-1, a, c, b)
    move(1, a, b, c)
    move(n-1, b, a, c)


def hanonums(n):
    move(n, 'a', 'b', 'c')


if __name__ == '__main__':
    hanonums(-1)
