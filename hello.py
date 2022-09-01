#!/usr/bin/env python3

print('hello world')
# name = input()
print('1024 * 768 = ', 1024 * 768)
print('I\'m learning\nPython.')
print(r'\\\\\1233\\\\')
print(r'''
        ... hell\no
        ... world
''')
print(3 > 2 and 2 > 3)
print(not 3 > 2 or 2 > 3)

age = 11
if age >= 18:
    print('adult')
else:
    print('teenager')

x = 10
x = x + 2
print(x)
print(10 / 3)

s4 = r'''Hello,
Lisa!'''
print(s4)

x = b'Hello'
print(x)

print('%2d-%2d' % (3002.22222, 1103.44444))
print('%.2f-%.2f' % (3002.22222, 1103.44444))

print('Hello, %s , I miss you, Do you miss me %.1f' %
      ('zhaowenjuan', 1103.44444))

r = 2.5
s = 3.14 * r**2
print(f'The area of a circle with radius {r} is {s:.2f}')
