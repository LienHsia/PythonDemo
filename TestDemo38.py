a = "OurWorldIsFullOfLOVE"
b=a.lower() 
flag=0 #判断开关
for i in range(len(a)):
    if i+4>len(a): #防止超出范围
        break
    tmp=b[i:i+4]
    if tmp=='love':
        flag=1
if flag:
    print('LOVE')
else:
    print('SINGLE')