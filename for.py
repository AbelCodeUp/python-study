from collections.abc import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for value in d.values():
    print(value)

for k, v in d.items():
    print('key:', k, 'value:', v)

isIns = isinstance('abc', Iterable)

for i, value in enumerate(['A', 'B', 'C']):
    print('i:', i, 'value:', value)


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    min = L[0]
    max = L[0]
    for num in L:
        if num < min:
            min = num
        if num > max:
            max = num
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
