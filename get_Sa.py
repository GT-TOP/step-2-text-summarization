#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#经过关键词抽取之后手动挑选出来的特征
aspectlist = [[u'皇家',u'园林',u'昆明湖',u'长廊',u'佛香阁',u'十七孔桥',u'万寿山',u'苏州街',u'建筑',u'景色'],
              [u'珍宝馆',u'宫殿',u'御花园',u'建筑',u'历史',u'午门',u'天安门',u'景点'],
              [u'烽火台',u'滑车',u'缆车',u'好汉坡',u'德胜门',u'风景'],
              [u'广场',u'升旗',u'城楼',u'毛主席纪念堂'],
              [u'白塔',u'九龙壁',u'荷花',u'划船',u'皇家',u'园林'],
              [u'祈年殿',u'回音壁',u'公园',u'圜丘',u'祭天',u'建筑',u'古树'],
              [u'红叶',u'爬山',u'公园',u'缆车',u'鬼见愁',u'枫叶']]

for j in range(1,8):
    fin = open('info_sentence%d.txt'%j,'r')
    lines = fin.readlines()
    fin.close()
    k = j - 1
    i = 1
    for eachone in aspectlist[k]:    #列表是从0开始的，而循环是从1~8
        fout = open('Sa%d_%d.txt'%(j,i),'w')
        i += 1
        for eachline in lines:
            if eachone in eachline:
                fout.write(eachline)
            else:
                pass
        fout.close()