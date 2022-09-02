# filter


def is_odd(n):
    return n % 2 == 1


list(filter(is_odd, [1, 2, 34, 4, 5, 6, 7, 8]))


def not_empty(s):
    return s and s.strip()


list(filter(not_empty, ['A', 'B', 'C', '', 'D', '    ', 'E']))


# 素数
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# 打印1000以内的素数:
for n in primes():
    if n < 10:
        print(n)
    else:
        break


# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    L = [i for i in str(n)]
    return L == L[::-1]


def is_palindrome_1(n):
    if str(n) == str(n)[::-1]:
        return n


#  测试:

output = filter(is_palindrome_1, range(1, 100))

print('1~100:', list(output))
