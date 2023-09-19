from math import *  ＃所有导入的数学函数
Ç，ħ  =  50，30

C,H = 50,30

def calc(D):
    D = int(D)
    return str(int(sqrt((2*C*D)/H)))

D = input().split(',')
D = list(map(calc,D))    ＃在D上应用calc函数并存储为列表
print(",".join(D))
from math import sqrt
C, H = 50, 30
mylist = input().split(',')
print(*(round(sqrt(2*C*int(D)/H)) for D in mylist), sep=",")
my_list = [int(x) for x in input('').split(',')]
C, H, x = 50, 30, []

for D in my_list:
    Q = ((2*C*D)/H)**(1/2)
    x.append(round(Q))

print(','.join(map(str, x)))