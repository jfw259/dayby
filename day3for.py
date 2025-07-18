#遍历字符串
for i in 'hello':
    print(i)
# range()函数，产生一个（n,m）的整数序列，包含n，但不包含m
for i in range(1,10):
    print(i)
    if i % 2 == 0:
        print(i,'是偶数')
#计算1-10的累加和
s=0
for i in range(1,11):
    s=s+i
else:
     print('和为ooo',s)