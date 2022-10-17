from functools import partial

int2 = partial(int, base=2)

print(int2('1010101'))


# int2 = functools.partial(参数1，参数2，参数3)
# 参数1：函数对象，
# 参数2：*args  可变参数，接收tuple，list
# 参数3：*kw  关键字参数，接收dict

# int2 = functools.partial(int，10，base=10)

# 参数1必填，参数2和参数3可省略，那就和原函数没区别了，因为参数1就是原函数，参数2就是可变参数，参数3为关键字参数，int自带关键字参数base，当不传为默认值，传入时必须以base=xxx的形式，对应原始的关键字，参数2传入的话会组装成tuple或list，
# 再通过*args 传入int（*args）

# 偏函数可以简化参数操作。
# 当函数的某个参数是我们可以提前获知的，那我们就可以将它固定住！
# 定义一个取余函数，默认和2取余；
def mod(x, y=2):
    # 返回 True 或 False
    return x % y == 0


# 假设我们要计算和3取余，如果不使用partial()函数，那么我们每次调用mod()函数时，都要写y=3
mod(4, y=3)
mod(6, y=3)

# 使用partial()函数
mod_3 = partial(mod, y=3)
