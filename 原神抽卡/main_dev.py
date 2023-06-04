import random
from random import choice

"""卡池内容（未设置四星up角色）"""
up = '枫原万叶'
up_3 = ['云锦', '久岐忍', '柯莱']
lst5 = ['刻晴', '莫娜', '七七', '迪卢克', '琴', '提纳里', '迪希雅']
lst4 = ['安柏', '丽莎', '凯亚', '芭芭拉', '雷泽', '菲谢尔', '班尼特', 
         '诺艾尔', '菲谢尔', '砂糖', '迪奥娜', '北斗', '凝光', '香菱', 
         '行秋', '重云', '辛焱', '罗莎莉亚', '烟绯', '早柚', '托马', 
         '九条裟罗', '五郎', '云锦', '久岐忍', '柯莱', '多莉', '坎蒂丝', 
         '莱依拉','珐露珊', '瑶瑶', '米卡', '卡维', '绮良良']
cha_4 = lst4
st5 = [up]*len(lst5) + lst5
for i in cha_4:
    if i in up_3:
        cha_4.remove(i)
weapon_4 = ['弓藏', '祭礼弓', '绝弦', '西风猎弓', '昭心', '祭礼残章',
            '流浪乐章','西风秘典', '西风长枪','雨裁', '匣里灭辰', 
            '祭礼大剑', '钟剑', '西风大剑', '匣里龙吟', '祭礼剑', '笛剑',
            '西风剑']
st4 = weapon_4 + cha_4
get = []
have = []


class Stats:
    """跟踪游戏统计信息"""
    def __init__(self):
        self.total = 0
        self.up_num = 0
        self.num_4 = 0
        self.num4_flag = False
        self.num5_flag = False
        self.num_5 = 0
        self.stone = 20000


def single():
    """不保底时的抽奖"""
    print("不保底")
    i = random.randint(1, 10000)
    if i in range(1, 60):
        a = random.randint(0, 6)
        star = st5[a]
        stat.num_5 = 0
    elif i in range(60, 570):
        if stat.num4_flag == True:
            star = choice(up_3)
            stat.num4_flag = False
        else:
            i = random.randint(1, 2)
            if i == 1:
                print(i,"up角色")
                star = choice(up_3)
                stat.num4_flag = False
            else:
                star = choice(st4)
                stat.num4_flag = True
        stat.num_4 = 0
    elif i in range(570, 10000):
        star = '三星'
    else:
        return None
    if star == up:
        stat.num_5 = 0
        stat.up_num = 0
    add(star)


def add(star):
    """每次抽卡完毕的常规操作"""
    record(star)
    get.append(star)
    have.append(star)
    stat.total += 1


def check_up():
    """检查保底"""
    if stat.up_num < 160:
        if stat.num_5 < 80:
            if stat.num_4 < 9:
                single()
            else:
                if stat.num4_flag == True:
                    star = choice(up_3)
                    stat.num4_flag = False
                else:
                    i = random.randint(1, 2)
                    if i == 1:
                        star = choice(up_3)
                        stat.num4_flag = False
                    else:
                        star = choice(st4)
                        stat.num4_flag = True
                add(star)
                stat.num_4 = 0
        else:
            if stat.num5_flag == True:
                star = up
                stat.num5_flag = False
            else:
                star = choice(st5)
                stat.num5_flag = False if star == up else True
            add(star)
            stat.num_5 = 0
    else:
        star = up
        add(star)
        stat.up_num = 0


def record(star):
    """记录数据变化"""
    if star != up:
        stat.up_num += 1
    if star not in st4:
        stat.num_4 += 1
    if star not in st5:
        stat.num_5 += 1

def extract():
    """单抽"""
    if stat.stone >= 160:
        del get[:]
        check_up()
        stat.stone -= 160
        print(get)
    else:
        print('您的原石不足，请充值！')


def ten():
    """十连函数"""
    if stat.stone >= 1600:
        del get[:]
        for num in range(0, 10):
            check_up()
        stat.stone -= 1600
        print(get)
    else:
        print('您的原石不足，请充值！')


def remember():
    """统计抽卡内容"""
    value_cnt = {}
    for h in have:
        value_cnt[h] = value_cnt.get(h, 0) + 1
    print(value_cnt)


stat = Stats()
