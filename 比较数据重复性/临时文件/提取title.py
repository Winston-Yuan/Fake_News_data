import json
total0 = {}
with open('Ti-CNN_total_data.json','r',encoding='utf-8') as f:
    data = json.load(f)
    for i,news in enumerate(data):
        title= news['title']
        total0[i] = title
with open('Ti-CNN_title.json','w',encoding='utf-8') as f:
    json.dump(total0,f,ensure_ascii=False,indent=4)

total1 = {}
with open('gossipcop_total_f.json','r',encoding='utf-8') as f:
    data = json.load(f)
    for i,news in enumerate(data):
        title= news['title']
        total1[i] = title
with open('gossipcop_title.json','w',encoding='utf-8') as f:
    json.dump(total1,f,ensure_ascii=False,indent=4)