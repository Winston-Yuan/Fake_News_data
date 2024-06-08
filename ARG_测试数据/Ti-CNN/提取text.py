import json
new_data = []
with open('Ti-CNN_data_filtered.json','r',encoding='utf-8') as f:
    data = json.load(f)
    for news in data:
        input = news['input']
        text = input.split('text:')[1]
        if text == 'null' :
            continue
        news['text'] = text
        new_data.append(news)
with open('Ti-CNN_data_filtered_text.json','w',encoding='utf-8') as f:
    json.dump(new_data,f,ensure_ascii=False,indent=4)