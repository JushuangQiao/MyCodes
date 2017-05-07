# coding:utf-8

# 面试题：
# 给出一个文件，求文件中出现最多的五个字符
# 不能用内置函数，自己实现
# 使用哈希表（字典）求数量
# 使用快速排序求结果


def count_max_characters(filename):
    counts = dict()
    with open(filename, 'r') as file:
        for line in file.readlines(1024):
            for c in line:
                if c != '\n':
                    counts[c] = counts[c]+1 if counts.get(c) else 1
    keys = list(counts)
    values = [counts[k] for k in keys]
    quick_sort(values, 0, len(keys)-1, keys)
    if len(counts) <= 5:
        return zip(keys, values)[::-1]
    else:
        return zip(keys, values)[-6:-1][::-1]


def sub_sort(data, left, right, keys):
    tmp = data[left]
    tmp_key = keys[left]
    while left < right:
        while left < right and data[left] < tmp:
            left += 1
        while left < right and data[right] >= tmp:
            right -= 1
        data[left], data[right] = data[right], data[left]
        keys[left], keys[right] = keys[right], keys[left]
    data[left] = tmp
    keys[left] = tmp_key
    return left


def quick_sort(data, left, right, keys):
    if left < right:
        tmp = sub_sort(data, left, right, keys)
        quick_sort(data, left, tmp, keys)
        quick_sort(data, tmp+1, right, keys)

# print count_max_characters('file.txt')
