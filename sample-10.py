import re

text = '超大材積▼每日強檔·瘋殺特賣▼\nJVC 65吋超4KHDR連網LED液晶顯示器T65\n《週末限定★週一10點回價》\n開始：０７／１６(星期五)１８：００\n結束：０７／１９(星期一)１０：００\n．網路價$29999\n．限時價↘$19999\n數量有限 把握機會不要錯過!\n\nT65_4KHDR_經典\n★同尺吋CP值最高\n★★HDR /PS4 PRO支援\n★首創 無邊穿透全面屏'

print(text)
print('')
print(re.sub(r'\s+', '', text))