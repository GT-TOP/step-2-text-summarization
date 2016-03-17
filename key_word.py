#coding=utf-8
import jieba
import jieba.analyse
import sys
reload(sys)
sys.setdefaultencoding('utf8')

fout = open('all_aspect1.txt','w')

for i in range(1,8):
    fin = open('info_sentence%d.txt'%i,'r')
    content = fin.read()
    fin.close()
    tag1 = jieba.analyse.extract_tags(content,topK=10)   #加上allowPOS=()进行词性筛选的效果并不好,同时增加了时间开销
    print (",".join(tag1))
    fout.write(",".join(tag1))
    fout.write('\n')
    print '\n'
    tag2 = jieba.analyse.textrank(content,topK=10)
    print (",".join(tag2))
    fout.write(",".join(tag2))
    fout.write('\n')
    print '\n'

fout.close()