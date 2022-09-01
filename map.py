from functools import reduce
from collections.abc import Iterator


def f(x):
    return x * x


r = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print(list(r))


def add(x, y):
    return x + y


print(reduce(add, [1, 3, 5, 7, 9]))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 3, 5, 7, 9]))


def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):

    def fn(x, y):
        return x * y

    return reduce(fn, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    n = s.find('.')
    print('n', n)
    num_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }

    def char2int(s):
        return num_dict[s]

    def add(x, y):
        return (x * 10 + y)

    strInt = map(char2int, s.replace('.', ''))
    return reduce(add, strInt) / (10**n)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
