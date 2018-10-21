#-*-coding:utf-8-*- 
__author__ = 'Chennull'

import re

week=[' ','周一','周二'	,'周三','周四','周五','周六','周天']
fi = open("result.txt","r",encoding='UTF-8')
fo = open("out.txt",'w+',encoding='UTF-8')
f = fi.readlines()

for line in f:
    # print(line[0])
    if line[0] == '\t' or line[0] == ' ':
        data = re.findall(r"\d+", line)
        for i in range(1,8):
            for j in range(0,24):
                if data[i][j]=='0':
                    fo.write('设备'+data[0]+'-'+place+week[i]+'第'+str(j)+'个采样点故障；\n')
    else:
        place = line[:-1]

# fo.write('123')
fi.close()
fo.close()