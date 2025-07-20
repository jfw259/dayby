#某公司，账户1W，给20员工发钱
money=10000
for i in range(1,21):
    import random
    score=random.randint(1,10)
    if score<5:
        print('员工',i,'绩效分',score,'不满足,不发工资')
        continue
    if money>=1000:
        money-=1000
        print('员工',i,'满足条件发放工资','公司账户余额：',money)
    else:
        print('余额不足，不发了',money)
        break
