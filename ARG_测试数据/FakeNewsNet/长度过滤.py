import json

new_data = []
with open('gossipcop_data.json','r',encoding='utf-8') as f:
    data = json.load(f)
    for news in data:
        if len(news['input'])<2000 and len(news['output'])>100:
            new_data.append(news)
print('old data number:',len(data))
print('new data number:',len(new_data))

with open('gossipcop_data_filtered.json','w',encoding='utf-8') as f:
    json.dump(new_data,f,ensure_ascii=False,indent=4)

