# -*- coding: utf-8 -*-

import jieba

text = '中央疫情指揮中心陳時中23日在記者會中宣布，全台7/27起至到8/9，防疫等級降到二級，並指示除飲食之外，外出全程戴口罩、超商賣場可內用、開放婚宴公祭等措施，不過部分縣市「逆時中」，和中央採取的措施不同。陳時中表示，7/27起至8/9調降疫情警戒標準至第二級，除飲食外，外出全程佩戴口罩，落實實聯制、保持社交安全距離，室內空間至少人與人保持1.5公尺，室外空間人與人至少保持1公尺，集會活動人數上限為室內50人，室外100人，另婚宴、公祭可開放，但公祭遵守內政部相關防疫規定處理，婚宴遵守每一隔間室內50人、室外100人上限。由於各縣市政府可依疫情需要和管理強度，做出不同指引，因此並非全台都「順時中」，像是台北市長柯文哲就表示，因為雙北社區仍有潛伏感染例，和新北市長侯友宜討論後，決定群聚吃飯放最後，「別想脫口罩吃東西。」'

jieba.load_userdict('userdict.txt')

# print(list(jieba.cut(text, cut_all=True)))

print(list(jieba.cut(text, cut_all=False)))

print(list(jieba.tokenize(text)))