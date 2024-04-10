import json

filepath = 'gossipcop_total.json'
total_data = []

with open(filepath,'r',encoding='utf-8') as f:
    data = json.load(f)
    for news in data:
        text = news['text']
        if len(text)<12000:
            total_data.append(news)
        else:
            continue
with open('gossipcop_total_f.json','w',encoding='utf-8') as f:
    json.dump(total_data,f,ensure_ascii=False,indent=4)
