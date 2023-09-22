# -*- coding: GBK -*-
import time
import itertools

"""
本题的思路：
    将所有可能的组合通过全排列的形式穷举出来
    然后根据已有的条件依次匹配
    若全部通过则为正确答案
    否则为错误方案
"""


# **********************匹配函数******************************

def handle(data):
    # 英国人住红色房子
    index = data[0].index('红色')
    if data[1][index] != '英国':
        return -1

    # 瑞典人养狗
    index = data[4].index('狗')
    if data[1][index] != '瑞典':
        return -2

    # 丹麦人喝茶
    index = data[2].index('茶')
    if data[1][index] != '丹麦':
        return -3

    # 抽Pall Mall香烟的人养鸟
    index = data[3].index('Pall Mall')
    if data[4][index] != '鸟':
        return -6

    # 黄色房子主人抽Dunhill香烟
    index = data[3].index('Dunhill')
    if data[0][index] != '黄色':
        return -7

    # 抽Blue Master的人喝啤酒
    index = data[3].index('BlueMaster')
    if data[2][index] != '啤酒':
        return -12

    # 德国人抽Prince香烟
    index = data[3].index('Prince')
    if data[1][index] != '德国':
        return -13

    # 绿色房子在白色房子左面
    index = data[0].index('绿色')
    if index == 4:  # 绿色房子在最后
        return -4
    if data[0][index + 1] != '白色':
        return -4

    # 绿色房子主人喝咖啡
    if data[2][index] != '咖啡':
        return -5

    # 抽Blends香烟的人住在养猫的人隔壁
    index = data[3].index('Blends')
    cat_index = data[4].index('猫')
    if cat_index - index != 1 and cat_index - index != -1:
        return -10

    # 养马的人住抽Dunhill香烟的人隔壁
    index = data[3].index('Dunhill')
    horse_index = data[4].index('马')
    if horse_index - index != 1 and horse_index - index != -1:
        return -11

    # 抽Blends香烟的人有一个喝水的邻居
    index = data[3].index('Blends')
    water_index = data[2].index('水')
    if water_index - index != 1 and water_index - index != -1:
        return -15

    print('找到答案:')
    for d_item in data:
        print(d_item)
    return 0


# **********************全排列列表******************************


# itertools.permutations 返回可迭代对象的所有数学全排列方式
# 以下是所有元素的全排列构成的列表
colour_list_all = list(itertools.permutations(['红色', '黄色', '蓝色', '白色', '绿色'], 5))
country_list_all = list(itertools.permutations(['英国', '丹麦', '挪威', '德国', '瑞典'], 5))
drinks_list_all = list(itertools.permutations(['茶', '水', '咖啡', '啤酒', '牛奶'], 5))
smoke_list_all = list(itertools.permutations(['Pall Mall', 'Dunhill', 'BlueMaster', 'Blends', 'Prince'], 5))
pet_list_all = list(itertools.permutations(['猫', '马', '鱼', '鸟', '狗'], 5))

# **********************过滤后的全排列列表******************************


# 全排列数量过大以下是过滤后出的列表
colour_list = []
country_list = []
drinks_list = []
smoke_list = []
pet_list = []

for colour in colour_list_all:
    colour = list(colour)
    if colour[1] == '蓝色':
        colour_list.append(colour)

for country in country_list_all:
    country = list(country)
    if country[0] == '挪威':
        country_list.append(country)

for drinks in drinks_list_all:
    drinks = list(drinks)
    if drinks[2] == '牛奶':
        drinks_list.append(drinks)

# 5! = 120
for i in range(len(smoke_list_all)):
    smoke_list.append(list(smoke_list_all[i]))

for i in range(len(pet_list_all)):
    pet_list.append(list(pet_list_all[i]))

# **********************遍历所有可能的方案并进行匹配******************************
# 由于程序采用穷举法，效率较低，故记录时间。
start = time.time()


for country in country_list:
    for drinks in drinks_list:
        for smoke in smoke_list:
            for pet in pet_list:
                for colour in colour_list:
                    data_list = [colour, country, drinks, smoke, pet]
                    # ~ num += 1
                    if handle(data_list) == 0:
                        # ~ print("总运行次数 %d" % num)
                        exit()
        end = time.time()
        print("\r计算用时:%0.4f秒" % (end - start), end="")

