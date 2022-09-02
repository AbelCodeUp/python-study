# 当我们临时需要匿名函数时，我们使用lambda函数。

# 在Python中，我们通常将其用作高阶函数的参数（该函数将其他函数作为arguments）。Lambda函数可以与filter()，map()等内置函数一起使用。

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x % 2 == 0), my_list))

print(new_list)
