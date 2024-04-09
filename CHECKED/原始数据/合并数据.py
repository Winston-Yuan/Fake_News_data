import json
import os

file_fake = r'D:\学习\毕设\数据\筛选可用的数据\清洗后的数据\整理对齐的数据\CHECKED-clean\fake_news'
file_real = r'D:\学习\毕设\数据\筛选可用的数据\清洗后的数据\整理对齐的数据\CHECKED-clean\real_news'
total_data = []

file_list_fake = os.listdir(file_fake)
for filename in file_list_fake:
    filepath = os.path.join(file_fake,filename)
    with open(filepath,'r',encoding='utf-8') as f:
        data = json.load(f)
        for keys in data:
            if data[keys] == '':
                data[keys] = 'null'
        total_data.append(data)

file_list_real = os.listdir(file_real)
for filename in file_list_real:
    filepath = os.path.join(file_real,filename)
    with open(filepath,'r',encoding='utf-8') as f:
        data = json.load(f)
        for keys in data:
            if data[keys] == '':
                data[keys] = 'null'
        total_data.append(data)

with open('CHECKED_total.json','w',encoding='utf-8') as f:
    json.dump(total_data,f,ensure_ascii=False,indent=4)