import time

pin = 0
while True:
   ips = []
   fr = open('assce.log')
   fr.seek(pin)
   for line in fr:
       ip = line.split()[0]  # 因为日志文件中每行的首个字符串是ip，与后面字符之间的分割是符号空格，所以用split（）分割后，返回的list中第一个值就是ip地址，取【0】
       ips.append(ip)
   new_ips = set(ips)  # 转换为集合
   for new_ip in new_ips:
       if ips.count(new_ip) > 200:
           print('加入黑名单的ip是：%s' % new_ip)
   pin = fr.tell()  # 记录读完的指针位置
   time.sleep(60)