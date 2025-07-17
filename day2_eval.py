s='3.14+3'
print((s),type(s))
x=eval(s)#使用eval函数去掉s旁边的“”
print((x),type(x))
age=eval(input('请输入您的年龄：'))#将年龄转换为int类型
print(type(age),age)
print(eval('x'))#注意eval的作用