import json

file_path='D:\学习\毕设\数据\数据整理\Weibo\原始数据\Weibo_total_data.json'

data0 = []
data1 = []
data2 = []
data3 = []

with open(file_path,'r',encoding='utf-8') as f:
    data = json.load(f)
    lenth = len(data)
    for i,news in enumerate(data):
        if i <lenth*1/4:
            data0.append(news)
        elif i <lenth*2/4:
            data1.append(news)
        elif i <lenth*3/4:
            data2.append(news)
        else:
            data3.append(news)
with open('data0.json','w',encoding='utf-8') as f:
    json.dump(data0,f,ensure_ascii=False,indent=4)
with open('data1.json','w',encoding='utf-8') as f:
    json.dump(data1,f,ensure_ascii=False,indent=4)
with open('data2.json','w',encoding='utf-8') as f:
    json.dump(data2,f,ensure_ascii=False,indent=4)
with open('data3.json','w',encoding='utf-8') as f:
    json.dump(data3,f,ensure_ascii=False,indent=4)