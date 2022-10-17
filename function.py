import math

# 内置函数
abs(-200)
max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# 数据类型转换
int('123')
float('123.123')
str(1.23)
bool(1)
bool('')

a = abs
x = a(123.45)
print(x)

n1 = 255
n2 = 1000
print(hex(n1))


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('x must be an integer or float')
    if x >= 0:
        return x
    else:
        return -x


def nop(age):
    if age >= 18:
        pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


r = move(100, 100, 60, math.pi / 6)


def quadratic(a, b, c):
    if not isinstance(a * b * c, (float, int)):
        raise TypeError("quadratic must be a float or int")
    q = b ** 2 - 4 * a * c
    if q < 0:
        print('no solution')
    elif q == 0:
        print('此方程的解是唯一的')
        x = (-b) / (2 * a)
        print(x)
    else:
        x1 = ((-b + math.sqrt(q)) / (2 * a))
        x2 = ((-b - math.sqrt(q)) / (2 * a))
        return x1, x2


def enroll(name, gender, age=6, city='Beijing'):
    pass


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数
# 可变参数在函数调用时自动组装为一个tuple


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n ** 2
    return sum


nums = [1, 2, 3]
calc(*nums)


# 关键字参数
# 允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Bob', 35, city='Beijing')
# name: Bob age: 35 other: {'city': 'Beijing'}

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Bob', 35, **extra)


# 命名关键字参数
# 函数的调用者可以传入任意不受限制的关键字参数, *后面的参数被视为命名关键字参数


def person_2(name, age, *, city='Beijing', job):
    print(name, age, city, job)


# 参数组合


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符


def f2(a, b, c=0, d=1, *arg, e, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'e =', e, 'kw =', kw, 'arg = ', arg)


f2(1, 2, 3, 4, 56, 7, 8, 9, 0, e=4, f=9)


# 练习
def mul(*numbers):
    if not len(numbers) == 0:
        sum = 1
        for n in numbers:
            if not isinstance(n, (int, float)):
                continue  # 跳出本次循环，执行下次循环
            sum *= n
        return sum
    else:
        raise TypeError('numbers must be a list')


# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))

if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9, 'test') != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')


# 递归
def fact_1(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


# 尾递归优化
def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print('fact_iter', fact(10))


# 汉诺塔问题实现
# a存放起始柱，b存放辅助柱、c存放目标柱
def move(n, a, b, c):
    if n == 1:
        print(a, '--->', c)
    else:
        move(n - 1, a, c, b)  # 借助c把第 num 个以外的圆盘从a移动到b
        move(1, a, b, c)  # 把第num个从a移动到c
        move(n - 1, b, a, c)  # 借助a把第 num 个以外的圆盘从b移动到c


move(3, 'A', 'B', 'C')


# 返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 2, 3, 4, 5)
print(f())


# 闭包
def count():
    fs = []

    def f(j):
        def g():
            return j * j

        return g

    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 一个函数可以返回一个计算结果，也可以返回一个函数。

# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

def createCounter():
    x = 0
    def counter():
        nonlocal x # 如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错：
        x = x + 1
        return x
    return counter


counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())

# lambda函名函数
def is_odd(n):
    return n % 2 == 1

L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)
