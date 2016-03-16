#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#论文中有一个用来判断句子重要性的阈值没有给出具体的数值
#暂时采用求平均值的方法，高于平均值的认为重要

for j in range(1,8):
    total = 0
    en_list = [ ]
    fin1 = open('sen_entropy%d.txt'%j,'r')
    lines = fin1.readlines()
    fin1.close()
    for eachline in lines:
        en_list.append(float(eachline.split()[1]))
        #print  eachline.split()[1]
        total += float(eachline.split()[1])
    avg = total/len(lines)
    print avg,len(lines)     #大概的验证一下
    index = 0
    sen_list = [ ]
    for i in en_list:
        #print i
        if i >= avg:
            sen_list.append(index)
        else:
            pass
        index += 1

    fin2 = open('output%d.txt'%j,'r')
    fout = open('info_sentence%d.txt'%j,'w')
    content = fin2.readlines()
    fin2.close()
    for i in sen_list:
        fout.write(content[i])

    fout.close()
