#长方型
for i in range(1,4):#外层循环，5列
    for j in range(1,5):#内层循环，4列
        print("*",end="")#让*不换行
    print()#换行
print('_______________-------------------')
#直角三角型
for i in range(1,6):
    for j in range(1,1+i):
        print('*',end="")
    print()
print('----------------------------------')
#倒三角型
for i in range(1,6):
    for j in range(i,7-i):
        print('*',end="")
    print()
#等腰三角型
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end="")
    for k in range(1,i*2):
          print('*',end="")
    print()


