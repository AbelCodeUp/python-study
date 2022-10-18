# f = open('test.txt', 'w+')
# f.write('hello world. morning.')
# f.seek(0)
# print(f.read())  # hello world.
#
# f = open('test.txt', 'r')
# lines = f.readlines()
# print(lines)
# f.close()

# 事实上，我们可以将 f 放在一个循环中，得到它每一行的内容：
# f = open('test.txt')
# for line in f:
#     print(line)
# f.close()

import os
import math


# f = open('binary.bin', 'wb')
# f.write(os.urandom(10))
# f.close()

# while True:
#     try:
#         text = input('>')
#         if text[0] == 'q':
#             break
#         x = float(text)
#         y = 1 / math.log10(x)
#         print('y', y)
#         print("1/log10({0}) = {1}".format(x, y))
#     except ValueError:
#         print("value must bigger than 0")
#     except ZeroDivisionError:
#         print("the value must not be 1")

class CommandError(ValueError):
    print("bad command operation. must input 'start', 'stop', 'pause'")


valid_commands = {'start', 'stop', 'pause'}
while True:
    command = input('>')
    if command == 'q':
        break
    try:
        if command.lower() not in valid_commands:
            raise CommandError('Invaild command: %s' % command)
        print('input command:', command)
    except CommandError:
        print("bad command string: %s" % command)
    finally:
        print('finally was called.')
    