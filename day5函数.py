'''

def 函数名（传入参数）：
    函数体
    返回值

'''
def say_hello():
    print('我是嫩爹')
def add(x,y):
    '''

    :param x:三个点加回车，可以快速进行注释
    :param y:
    :return:
    '''
    result=x+y
    print('结果为：',result)
add(8,9)

'''
def 函数（参数）：
    函数体
    return 返回值

变量=函数（参数）
#注意如果在return后面加代码是不执行的
'''
#None:无实际意义
'''
None:用在函数无返回值上
用在if判断上
在if判断中，None等同于False
一般用于在函数中主动返回None，配合if判断做相关处理

'''
def say():
    print('fku')
kk=say()
print(kk)
def say2():
    print('kun')
    return None
kk=say2()
def check_age(age):
    if age>=18:
        return 'success'
    else:
        return None
result=check_age(16)
if not result:
    #进入if表示result是None值，也就是Fales
    print('未成年禁止进入')

#嵌套函数
def fun_b():
     print('----------1')
def fun_a():
    print('----------2')
    fun_b()
    print('----------3')
fun_a()
#嵌套函数
#局部变量
def test_a():
    num=100
    print(num)
test_a()
#全局变量
num=200
def test_b():
    print(num)
#global 关键字声明a是全局变量,可以让全局变量在函数里修改
def fun_c():
    global num
    num=100
    print(num)
test_b()
fun_c()
print(num)

