import json

filepath0 = 'D:\学习\毕设\数据\数据整理\Weibo\GPT问答\Weibo_total_data_withGPT0.json'
filepath1 = 'D:\学习\毕设\数据\数据整理\Weibo\GPT问答\Weibo_total_data_withGPT1.json'
filepath2 = 'D:\学习\毕设\数据\数据整理\Weibo\GPT问答\Weibo_total_data_withGPT2.json'
filepath3 = 'D:\学习\毕设\数据\数据整理\Weibo\GPT问答\Weibo_total_data_withGPT3.json'
total_data = []
with open (filepath0,'r',encoding='utf-8') as f:
    data = json.load(f)
    for news in data:
        total_data.append(news)
with open(filepath1, 'r', encoding='utf-8') as f:
    data = json.load(f)
    for news in data:
        total_data.append(news)
with open(filepath2, 'r', encoding='utf-8') as f:
    data = json.load(f)
    for news in data:
        total_data.append(news)
with open(filepath3, 'r', encoding='utf-8') as f:
    data = json.load(f)
    for news in data:
        total_data.append(news)

with open('Weibo_total_data_GPT.json','w',encoding='utf-8') as f:
    json.dump(total_data,f,ensure_ascii=False,indent=4)
