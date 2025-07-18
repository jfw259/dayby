#break退出循环结构
s=0#存储
i=1
while i<11:
    s=s+i
    if s>20:
        print('累加和大于20的当前数i是：',i)
        break
    i=i+1
i=0
while i<3:
    user_name=input('name')
    pwa=input('password')
    if user_name=='123' and pwa=='321':
        print('登入中')
        break
    else:
        if i<2:
           print('不正确你还有',2-i,'次机会')
    i=i+1
else:
    print('封号斗罗')
