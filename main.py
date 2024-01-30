from GetTieba import Tieba
import csv
import os
#调用该文件夹下venv里的python，有包
# 用户输入要爬的吧名即可
tieba=Tieba('航空母舰') #注意不要输入'吧'字

#---------------------------------------------------------#
baseInfo=tieba.getBaseInfo()
print('吧名:',tieba.name)
print('尾页id:',baseInfo['pn']) # pn是页数
print('会员汇总:',baseInfo['nums'])#nums是人数，在关注列表一页有24人，需要用nums/24+1得到末页的值

# 将整个吧的帖子信息写入csv文件
infoDir={'回复数':'',
         '标题':'',
         'Tid':''}
peopleDir={'用户名称': '',
            '注册时长': 'years',
            '发帖数量': 'ties',
            '性别情况': 'sex',
            '用户级别': 'levels'}
#
# if not os.path.exists(tieba.name+'吧.csv'):
#     with open(tieba.name+'吧.csv','a',newline='',encoding='utf-8-sig') as csvfile:
#         w=csv.DictWriter(csvfile,fieldnames=infoDir)
#         w.writeheader()
#         for i in range(0,int(baseInfo['pn'])+50,50): #获取整个吧的信息
#             TieInfo=tieba.getTieInfo(i) #获取每一页的贴子信息
#             for e in TieInfo:
#                 w.writerow({
#                     '回复数':e['reply_num'],
#                     '标题':e['title'],
#                     'Tid':e['tid']
#                 })
#             print('...')
#             w.writerow({})
#             print(i,' 成功写入文件')
# print("已经成功写入所有可读帖子")



# if not os.path.exists(tieba.name+'会员2.csv'):
#     with open(tieba.name + '会员汇总.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
#         wp = csv.DictWriter(csvfile, fieldnames=peopleDir)
#         wp.writeheader()
#         for i in range(1, int(baseInfo['nums'])//24+1 , 1):  # 获取整个吧的信息
#             TieInfo = tieba.getMembersInfo(i)  # 获取每一页的关注者信息
#             for e in TieInfo:
#                 wp.writerow({
#                     '用户id': e['name'],
#                     '注册时间': e['years'],
#                     '发帖数': e['ties'],
#                     '性别': e['sex']
#                 })
#             print('...')
#             wp.writerow({})
#             print("第",i, '页成功写入')

#print("已经成功写入所有关注人")

#写成txt，第一列是贴吧内容，第二列是文字内容
if not os.path.exists(tieba.name+'吧.txt'):
    with open(tieba.name+'吧.txt','a',newline='',encoding='utf-8-sig') as txtfile:
        for i in range(0,5000,50): #获取整个吧的信息
            TieInfo=tieba.getTieInfo(i) #获取每一页的贴子信息
            for e in TieInfo:
                txtfile.write("4， "+e['title'] + '\n')
            print('...')
            print(i, ' 成功写入文件')
        print("已经成功写入所有可读帖子")

