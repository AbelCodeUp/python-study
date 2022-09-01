#!/usr/bin/python3


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 杨辉三角
def triangles():
    ret = [1]
    while True:
        yield ret
        pre = ret[:]
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
result = list()
item = triangles()
for t in item:
    result.append(list(t))
    n = n + 1
    if n == 10:
        break

for t in result:
    print(t)

if result == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],
              [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1],
              [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1],
              [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]:
    print('测试通过!')
else:
    print('测试失败!')

# 凡是可作用于for循环的对象都是Iterable类型；

# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
