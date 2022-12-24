#随机生成十个密码
import random
big = 'qwertyuiopasdfghjklzxcvbnm123456789'
lis = []
for i in big:
    if i.isalpha():
        lis.append(i)
        up = i.upper()
        lis.append(up)
    else:
        lis.append(i)

for i in range(10):
    mima = ''
    for j in range(8):
        mima += random.choice(lis)
    print(f'第{i + 1}个随机密码为：', mima)