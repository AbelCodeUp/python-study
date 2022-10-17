# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

height = 1.76
weight = 75

bmi = weight / (height ** 2)
print('bmi = %.f' % bmi)
if bmi <= 18.5:
    print('过轻')
elif bmi > 18.5 and bmi <= 25:
    print('正常')
elif bmi > 25 and bmi <= 28:
    print('过重')
elif bmi > 28 and bmi <= 32:
    print('肥胖')
elif bmi > 32:
    print('严重肥胖')
