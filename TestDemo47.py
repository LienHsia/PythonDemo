from functools import reduce


def str_int(s):#定义一个函数，用于把字符串型转换成整型
    def char_int(ch):#定义一个函数，用于把字符串中的每个数字都分开 ，做成一个字典
        c = {str(x): x for x in range(10)}#对0～9遍历，做成一个字典，输出{'0':0,'1':1,……}
        return c[ch]#返回字典中的value值

    def fun(n1, n2):#定义一个字典，用于把分开的数字在重新黏起来
        return n1 * 10 + n2#1,2-->10+2=12 12,3-->120+3=123 123,4-->1230+4=1234 1234,5-->12340+5=12345

    # 内层使用map型函数将输入的字符串处理成单个的数字，外层使用reduce函数进行累积
    return reduce(fun, map(char_int, s))


num = str_int('12345')#输入字符串
print(num, type(num))

