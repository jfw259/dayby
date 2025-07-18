anwser=input('今天打go吗')
while  anwser=='打':
    print('那就打爆魔王s')

    anwser=input('还打吗')
else:
    print('好好学习')
    anwser=input('今天还打吗')
while anwser=='打':
    print('打爆')
    anwser=input('今天还打？')
s=0#累加和
i=1#初始变量
while i<=100:#条件判断
    s=s+i#语句块
    i=i+1#改变变量
print(s)