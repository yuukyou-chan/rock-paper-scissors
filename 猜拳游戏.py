import random

# 猜拳小游戏
# Author ：yuukyou
# Time:2021/5/31

count = 0
flag = 0
a = ["石头", "剪刀", "布"]
while count <= 2:

    print("第%s局开始！" % int(count+1))
    shuru = int(input("请输入：石头（0），剪刀（1），布（2）"))
    ran = random.randint(0, 3)
    if shuru == 0 and ran == 1 or shuru == 1 and ran == 2 or shuru == 2 and ran == 0:
        count += 1
        print("我出", a[ran])
        print('你赢了！')
        flag += 1

    if shuru == 0 and ran == 2 or shuru == 1 and ran == 0 or shuru == 2 and ran == 1:
        count += 1
        print("我出", a[ran])
        print('你输了！')

    if shuru == ran:
        print("我也出", a[ran])
        print("我俩出的一样，平局，再来！")

if flag >= 2:
    print("游戏结束***你赢了***:三局两胜你赢了%s局" % flag)
else:
    print("游戏结束***你输了***:三局两胜你赢了%s局" % flag)