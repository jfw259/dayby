s=0
i=1
while i<=100:
    if i%2==1:#奇数
        i=i+1
        continue#跳过本次循环的后续代码，而继续执行下一次循环操作
    s=s+i
    i=i+1
print('1-100偶数和',s)
print('----------------------')
s=0
for i in range(1,101):
    if i%2==1:
        continue#跳过本次循环的后续代码，而继续执行下一次循环操作
    s=s+i
print('1-100偶数和',s)