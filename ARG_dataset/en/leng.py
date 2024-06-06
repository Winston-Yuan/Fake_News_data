import json
max_len = 0
min_len = 10000
with open('train.json','r',encoding='utf-8') as f:
    data = json.load(f)
    for news in data:
        content = news['content']
        max_len = max(max_len,len(content))
        min_len = min(min_len,len(content))
print(max_len)
print(min_len)