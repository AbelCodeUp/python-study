import os
# list 列表生成式
classmates = ['Michael', 'Bob', 'Tracy']
classmates.append('Admin')
classmates.insert(2, 'Jack')
# classmates.pop()
print(classmates)
print('classmates length : %d' % len(classmates))
print('classmates length :', len(classmates))

# tuple 元组
tupleList = ('Michael', 'Bob', 'Tracy')
print('tupleList length : %d' % len(tupleList))

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('.')])

L = ['Hello', 'World', 'IBM', 'Apple']
print([x.lower() for x in L])


print([x if x % 2 == 0 else -x for x in range(1, 11)])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print('L2', L2)
