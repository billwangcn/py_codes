import pyautogui as pg
import sys
import time
import random
import pyperclip

INTERVAL = 1
KEYWORD = [u'关注', 'Study in depth']
PVIEW = ["China's opening drive is not a one-man show,Rather,it is an invitation open to all. It is a pursuit not to establish China's own sphere of influence, but to support common development of all countries. It is meant to build not China's own backyard garden, but a garden shared by all countried.",
         "We are greatly encouraged by both the trust all the comrades of the Party have placed on us and the great expectations the people of all ethnic groups in China have of us, and we are keenly aware that this is also an important responsibility for us.",
         "China's reform is about the self-improvement and development of socialism with Chinese characteristics. Reform and opening up are crucial to adhering to and developing socialism with Chinese characteristics.",
         "Reform and opening-up, opened up a path of socialism with Chinese characteristics.Unswervingly insisting in and developing socialism with Chinese characteristics inevitably requires unswervingly strengthening and developing the patriotic United Front. ",
         u'每个人都有理想和追求，都有自己的梦想。现在，大家都在讨论中国梦，我以为，实现中华民族伟大复兴，就是中华民族近代以来最伟大的梦想。国家好，民族好，大家才会好。',
         u'改革开放只有进行时没有完成时。没有改革开放，就没有中国的今天，也就没有中国的明天。改革开放中的矛盾只能用改革开放的办法来解决。',
         u'必须坚决完成各项军事斗争任务。全军要深刻认识军队在国家安全和发展战略全局中的重要地位和作用，坚持把国家主权和安全放在第一位，坚持军事斗争准备的龙头地位不动摇，全面提高信息化条件下威慑和实战能力，坚决维护国家主权、安全、发展利益。全军要坚持把军事训练摆在战略位置，不断提高部队实战化水平。',
         u'要坚持“老虎”“苍蝇”一起打，既坚决查处领导干部违纪违法案件，又切实解决发生在群众身边的不正之风和腐败问题。要坚持党纪国法面前没有例外，不管涉及到谁，都要一查到底，决不姑息。',
         u'空谈误国，实干兴邦。我们这一代共产党人一定要承前启后、继往开来，把我们的党建设好，团结全体中华儿女把我们国家建设好，把我们民族发展好，继续朝着中华民族伟大复兴的目标奋勇前进。']


def mclick(item):  # 移动过去后，停留一秒再CLICK非常有必要。
    pg.moveTo(item[0], item[1])
    time.sleep(INTERVAL)
    pg.click()


def isFlag(item):  # 检测是否有特殊点需要处理
    if item[0] == 0:
        return True
    return False

# 小本上网用
list0101 = [(130, 670),
            (118, 780),
            (0, 0),
            (126, 271),
            (123, 398),
            (122, 520),
            (125, 629),
            (108, 746),
            (0, 0),
            (125, 289),
            (122, 412),
            (125, 536),
            (123, 641)]

# 小本上网用
list0102 = [(242, 215),
            (652, 756),
            (0, 0),
            (473, 37)]
# 发表观点
list0201 = [(300, 121),
            (388, 306),
            (0, 0),
            (882, 410),
            (471, 39)]
#发表动态
list0300 = [[(199, 124),
             (186, 521),
             (224, 223),
             (637, 600),
             (0, 0),
             (473, 39)],

            [(199, 124),
             (186, 603),
             (224, 223),
             (637, 600),
             (0, 0),
             (473, 39)],

            [(199, 124),
             (186, 692),
             (224, 223),
             (637, 600),
             (0, 0),
             (473, 39)],

            [(199, 124),
             (186, 776),
             (224, 223),
             (637, 600),
             (0, 0),
             (473, 39)]]
#学习留言
list0400=[
    (133, 115),
    (134, 364),
    (1036, 497),
    (272, 199),
    (625, 229),
    (0,0),
    (629, 38)
]


def toPrice():
    try:
        for item in list0:
            mclick(item)
            time.sleep(2)
    except KeyboardInterrupt:
        print('/n')


def toWrite():
    for item in list0102:
        if not isFlag(item):
            mclick(item)
            time.sleep(INTERVAL)
        else:
            # pyperclip.copy(KEYWORD[1])  # 先复制
            # pg.hotkey('ctrl', 'v')  # 再粘贴
            pg.typewrite(KEYWORD[1])
            # time.sleep(INTERVAL)
            time.sleep(INTERVAL)
            pg.hotkey('enter')
            time.sleep(INTERVAL)
            pg.hotkey('ctrl', 'enter')
        # time.sleep(INTERVAL)


def toTitle():
    try:
        for item in list0101:
            if not isFlag(item):
                mclick(item)
                toWrite()
            else:
                pg.hotkey('pagedown')
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print('/n')


def toPartyView():
    for item in list0201:
        if not isFlag(item):
            mclick(item)
            time.sleep(INTERVAL)
        else:
            pg.typewrite(PVIEW[random.randint(0, 3)])
            # pyperclip.copy(PVIEW[random.randint(0, 3)])  # 先复制
            # pg.hotkey('ctrl', 'v')  # 再粘贴
            time.sleep(INTERVAL)
            pg.hotkey('ctrl', 'enter')


def toPartyView1():
    for item in list0201:
        if not isFlag(item):
            mclick(item)
        else:
            sstr = str(PVIEW[random.randint(0, 3)])
            # for i in range(len(sstr)):            
            #     pg.typewrite(sstr[i:i+1],=0.1)
            # sstr = str(PVIEW[random.randint(0, 1)]=2)
            # print(sstr)
            #pyperclip.copy(sstr)  # Frist Copy
            # # pyperclip.copy()
            #print(sstr)
            #time.sleep(INTERVAL)
            #pg.hotkey('ctrl', 'v')  # 再粘贴
            # time.sleep(2)
            # pg.typewrite(sstr, interval=0.05)
            pg.typewrite(PVIEW[random.randint(0, 3)])
            pg.hotkey('ctrl', 'enter')
        time.sleep(INTERVAL)


def toTalk(xlist):
    for item in xlist:
        if not isFlag(item):
            mclick(item)
            time.sleep(INTERVAL)
        else:
            pg.typewrite(KEYWORD[1])
            time.sleep(INTERVAL)
            pg.hotkey('enter')
            time.sleep(INTERVAL)
            pg.hotkey('ctrl', 'enter')


def toHeart(xlist):
    for item in xlist:
        if not isFlag(item):
            mclick(item)
            time.sleep(INTERVAL)
        else:
            pg.typewrite(PVIEW[random.randint(0, 3)][:200])
            time.sleep(INTERVAL)
            pg.hotkey('enter')
            time.sleep(INTERVAL)
            pg.hotkey('ctrl', 'enter')
            time.sleep(INTERVAL)
            pg.hotkey('ctrl', 'W')
            time.sleep(INTERVAL)
            pg.hotkey('enter')
            

def toAll():
    for i in range(2):
        pg.hotkey('pageup')

    #toTitle()

    for i in range(3):
        pg.hotkey('pageup')

    for i in range(3):
        #toPartyView1()
        #pass

    #toHeart(list0400)   

    for i in range(3):
        pg.hotkey('pageup')
# 
    for l in list0300:
      toTalk(l)
        #pass


# 
# time.sleep(2)
toAll()


