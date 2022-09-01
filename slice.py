L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
n = 3
for i in range(n):
    r.append(L[i])

print(L[0:10])
print(L[:3])
print(L[-2])
print(L[-2:-1])

L0 = list(range(100))

# 前10个数
L0[:10]

# 后10个数
L0[-10:]

# 每5个取一个
L0[::5]

# 复制一个list
L0[:]

# 前11-20个数
print(L0[:10:3])

# 前10个数
(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)[:10]


# 练习

def trim(s):
    x = 0
    y = -1
    while x <= len(s):
        if s[x] == ' ':
            x += 1
        else:
            break

    while y <= 0:
        if s[y] == ' ':
            y -= 1
        else:
            break
    return s[x:y+1]


print(trim('     xxx     '))
