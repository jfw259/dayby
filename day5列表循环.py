"""
演示使用while和for循环遍历列表
"""



def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return: None
    """
    mylist = ["传智教育", "黑马程序员", "Python"]
    # 循环控制变量：通过下标索引来控制，默认0
    # 每一次循环将下标引变量+1
    #循环条件：下标索引变量<列表元素数量
    index = 0     #初始值为0
    while index<len(mylist):
        element = mylist[index]
        print('列表的元素：',element)
        index=index+1

list_while_func()



def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:
    """
    my_list=[1,2,3,4,5]
    #for 临时变量 in 数据容器：
    for element in my_list:
        print('列表元素有',element)
list_for_func()