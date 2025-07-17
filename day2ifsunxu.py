'''a,b,c,d='room'
print(a,b,c,d)
number1=(eval(input('请您为我们的战队投票')))
if number1==10:
    print('恭喜您，steam被倒了')
if number1==20:
    print('hhh')
x=input('请输入一个字符串')
if x:
    print('x是一个非空字符串')
if not x:
    print('x是一个空字符串')
#双分支结构
number = input("请输入ok")
if number=='ok':
    print("输入的数字符合条件")
else:
    print("输入的数字不符合条件")
numbe=eval(input('到我了'))
nbooe='你的steam被盗了' if numbe==1 else '您未被盗'
print(nbooe)'''
#多分支结构
import ast
score=ast.literal_eval(input('请输入成绩'))
if score<=0 or score>100:
    print('成绩有误')
elif score>=0 and score<60:
    print('您成绩不及格')
elif score>=60 and score<70:
    print('c')
else:
    print('A')