# -*- coding: utf-8 -*-

import collections
import itertools
import munch
import re

import jieba

articles = [
    '中央疫情指揮中心昨宣布，全國疫情警戒自27日起至8月9日降為二級，指揮中心也公布相關鬆綁措施指引。政院官員今（24日）表示，政府會以14天為周期觀察，疫情狀況決定鬆綁條件，「疫情控制愈好，進一步鬆綁等都有可能」。《中央社》報導，行政院政院官員表示，疫情警戒降級仍是以14天為周期做觀察，疫情控制好壞決定了鬆綁條件，疫情控制越好，回復正常生活機率就越高，若疫情嚴峻，當然就會受比較強的管制。官員表示，過去公布的二級管制措施，集會活動室內可100人、室外500人，不過目前僅開放室內50人、室外100人；也就是說，若疫情持續趨緩、受控，只剩零星感染，管制措施就有更加鬆綁的空間。《中央社》報導，官員也強調，通則仍持續戴口罩。對於基隆市長林右昌質疑降級設期限，恐導致民眾猛爆性出遊、餐敘、消費。官員說明，目前疫情宣布降級或升級都以兩週為周期，這是參考疫情潛伏期而定，過去雖出現超過14天的周期，是為了配合國定假期所做的些微調整。（政治中心／台北報導）',
    '中央疫情指揮中心陳時中23日在記者會中宣布，全台7/27起至到8/9，防疫等級降到二級，並指示除飲食之外，外出全程戴口罩、超商賣場可內用、開放婚宴公祭等措施，不過部分縣市「逆時中」，和中央採取的措施不同。陳時中表示，7/27起至8/9調降疫情警戒標準至第二級，除飲食外，外出全程佩戴口罩，落實實聯制、保持社交安全距離，室內空間至少人與人保持1.5公尺，室外空間人與人至少保持1公尺，集會活動人數上限為室內50人，室外100人，另婚宴、公祭可開放，但公祭遵守內政部相關防疫規定處理，婚宴遵守每一隔間室內50人、室外100人上限。由於各縣市政府可依疫情需要和管理強度，做出不同指引，因此並非全台都「順時中」，像是台北市長柯文哲就表示，因為雙北社區仍有潛伏感染例，和新北市長侯友宜討論後，決定群聚吃飯放最後，「別想脫口罩吃東西。」',
    '中颱烟花為北台灣帶來豪雨，桃園市復興區、新竹縣尖石、五峰鄉今天停止上班上課，苗栗泰安今早也宣布10點起停班課，苗栗縣南庄鄉公所接著宣布今日下午停止上班上課。《蘋果新聞網》持續為您整理各地停班課資訊。桃園市、新竹縣今早發大豪雨特報。台中以北、宜蘭地區及南投山區易出現局部大雨或豪雨，北部山區有局部豪雨以上等級降雨發生的機率，其他地區偶有局部短暫陣雨或雷雨。今晨至白天是烟花影響台灣最劇烈的時刻，台北市山區從凌晨0時至清晨6時已降下170毫米雨量。中央氣象局預報員陳伊秀指出，烟花目前中心位置在台北的北北東方約450公里之海面上，以每小時16公里速度，向北北西進行，其暴風圈正逐漸進入台灣北部海面，清晨至白天影響最劇烈。（即時新聞中心／綜合整理）'
]

jieba.load_userdict('userdict.txt')

ignores = [
    '，', '。', '：', '；', '、', '！', '？', '」', '「', '（', '）', '／', '《', '》',
    '的', '也', '與', '有', '你', '我', '你', '妳', '他', '她'
]

analysis = []
for index, article in enumerate(articles):
    tokens = jieba.cut(article, cut_all=False)
    tokens = list(tokens)
    tokens = [
        token
        for token in tokens
        if token not in ignores and len(token) > 1 and re.match(r'^\d+$', token) is None
    ]
    # print(tokens)
    counts = collections.Counter(tokens)
    # print(counts)
    counts = counts.most_common(10)
    # print(counts)
    analysis.append({
        'index': index + 1,
        'tokens': tokens,
        'counts': counts
    })
# print(analysis)
analysis = munch.munchify(analysis)

pairs = itertools.combinations(analysis, 2)
for pair in pairs:
    print(f'{pair[0].index}-{pair[1].index}')
    article0 = pair[0]
    article1 = pair[1]
    article0_words = [
        count[0]
        for count in article0.counts
    ]
    article1_words = [
        count[0]
        for count in article1.counts
    ]
    same_words = set(article0_words).intersection(set(article1_words))
    # print(same_words)
    total_words = set(article0_words).union(set(article1_words))
