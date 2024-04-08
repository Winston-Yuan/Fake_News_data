import json
import os
folder_path = 'D:\学习\毕设\数据\筛选可用的数据\清洗后的数据\整理对齐的数据\Ti-CNN训练数据\原始数据'
write_path = 'Ti-CNN_total_data.json'
total_data = []
for i,filename in enumerate(os.listdir(folder_path)):
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if int(data['text_len']) < 50:
            continue
        elif int(data['text_len']) > 8000:
            continue
        if data['time'] != '':
            data['time'] = data['time']
        else:
            data['time'] = 'null'
        if data['author'] != '':
            data['author'] = data['author']
        else:
            data['author'] = 'null'
        if data['url'] != '':
            data['url'] = data['url']
        else:
            data['url'] = 'null'
        total_data.append(data)
with open(write_path,'w',encoding='utf-8') as f:
    json.dump(total_data,f,ensure_ascii=False,indent=4)


