print('---------欢迎来到德莱联盟---------')
x=int(input('按1or2or3键进入自助服务'))
while x>0 and x<4:
       print('---------欢迎来到德莱联盟---------')
       print('1,显示当前余额：')
       print('2,显示当前流量：')
       print('3,显示当前的剩余通话时长：')
       print('0,退出自助查询系统')
       x=int(input('请输入：...'))
       while x>0 and x<4:
            if x==1:
                print('您当前余额为5000刀，建议买把无尽之刃')
                break
            if x==2:
                print('您有9999T流量，畅玩csgo')
                break
            if x==3:
                 print('您通话时长为99999h，法老来了都骂不过您')
                 break
else:
           print('已退出德莱联盟')
           pass



