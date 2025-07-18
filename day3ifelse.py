answer=input('你喝酒了？')
if answer=='y':
    proof=eval(input('测酒精含量'))
    if proof<20:
        print('ky')
    elif proof<100:
        print('gun')
else:
    print('fine')
user_name=input('请输入您的qq号:')
user_pwd=input('请输入您的密码:')
if user_name== '3464574841' and user_pwd== 'jfwaabbcc123':
    print('登入成功')
else:
    print('登入失败，请重新输入：')
