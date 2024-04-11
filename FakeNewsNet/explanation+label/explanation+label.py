import json
import random

read_path = 'D:\学习\毕设\数据\数据整理\FakeNewsNet\原始数据\gossipcop_total_analysis.json'
write_path = 'gossipcop_explanation_label.json'
total_data = []
a = 0
b = 0
with open(read_path,'r',encoding='utf-8') as f:
    data = json.load(f)
    for news in data:
        conversation = {}
        analysis = news['analysis']
        label = news['label']
        if label == 'real':
            a+=1
        else:
            b+=1
        answer = analysis + '\n\n' + 'label: ' + label
        if len(news['author']) !=0:
            author = news['author'][0]
        else:
            author = 'null'
        input = 'time: '+news['time'] +' \n '+'author: '+ author +' \n '+'source: ' + news['url'] +' \n '+'text: ' + news['text']
        conversation['instruction'] ="You will be responsible for explaining the veracity of a particular news story. During this process, you will receive a news text material. Your task is to provide a detailed analysis of the veracity of the news and a reasonable explanation to clarify the basis for determining whether each report is true or false. \nYour answer should follow the following format:\nLet's think step by step\nSource reliability: XXX\nAuthor background: XXX\nEvidence test: XXX\nLanguage style: XXX\nOther analysis: XXX\nLabel: real/fake \nHere is the news text material:"
        conversation['input'] = input
        conversation['output'] = answer
        total_data.append(conversation)
    random.shuffle(total_data)
with open(write_path,'w',encoding='utf-8') as f:
    json.dump(total_data,f,ensure_ascii=False,indent=4)

print('real:',a,'fake:',b)





