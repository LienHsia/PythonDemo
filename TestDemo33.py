class pig:
    def __init__(self, dict, n):
        self.dict = dict
        self.n = n
 
    def sort(self):
        for j in range(self.n):
            index = 0
            for i in range(len(self.dict)):
                # 只接受2-4岁的小猪，
                if 2 <= self.dict[i][0] <= 4:
                    index += self.dict[i][1] * 2
            # 将今年出生的小猪添加进去
            self.dict.append([0, index])
            # 如果小猪大于4岁,将其数组中的值销毁,这个数组销毁困扰了小编很久,最后只能记入下表值,然后将其反转,从后面向前删除数组中的值
            sums = []
            for i in range(len(self.dict)):
                # 一年过去了,小猪生完崽，给小猪加一岁
                self.dict[i][0] += 1
                if self.dict[i][0] > 4:
                    sums.append(i)
            sums = sums[::-1]
            # 删除
            for i in sums:
                del self.dict[i]
                
            # 显示当前猪圈猪的数量
            for i in range(len(self.dict)):
                print("岁数%d,数量%d" % (self.dict[i][0], self.dict[i][1]))
            print("第%d年猪的数量：%s" % (j + 1, sum(map(lambda x: x[1], self.dict))))
            print()
 
p = pig([[2, 2]], 10)
p.sort()
input()