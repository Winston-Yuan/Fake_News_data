import json
import random

read_path = 'D:\学习\毕设\数据\数据整理\CHECKED\原始数据\CHECKED_total_analysis.json'
write_path = 'CHECKED_only_label.json'
total_data = []

with open(read_path,'r',encoding='utf-8') as f:
    data = json.load(f)
    for news in data:
        conversation = {}
        label = news['label']
        answer ='label: ' + label
        if len(news['author']) !=0:
            author = news['author'][0]
        else:
            author = 'null'
        input = 'time: '+news['time'] +' \n '+'author: '+ author +' \n '+'source: ' + news['url'] +' \n '+'text: ' + news['text']
        conversation[
            'instruction'] = "You will be responsible for explaining the veracity of a particular news story. During this process, you will receive a news text material. Your task is to provide the label of the news without any explanation. \nYour answer should follow the following format: Label: real/fake"
        conversation['input'] = input
        conversation['output'] = answer
        total_data.append(conversation)
    random.shuffle(total_data)
with open(write_path,'w',encoding='utf-8') as f:
    json.dump(total_data,f,ensure_ascii=False,indent=4)