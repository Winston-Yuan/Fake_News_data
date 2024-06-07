import json
import re  # 导入正则表达式模块

# 从文件中读取data
with open('CHECKED_only_label.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


# 定义一个函数来清理ZWSP和NBSP字符
def remove_unwanted_spaces(text):
    # 使用正则表达式替换ZWSP和NBSP字符
    cleaned_text = re.sub(r'[\u200B\u00A0]+', ' ', text)
    # 替换多个空格为一个空格，并去除字符串首尾的空格
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text


# 将数据集转换为train.txt格式的文件
with open('data.txt', 'w', encoding='utf-8') as f:
    for item in data:
        # 提取文本和标签
        text = item["input"].replace("\n", " ")  # 替换换行符
        text = text.split('text: ')[1]
        text = remove_unwanted_spaces(text)  # 清理ZWSP和NBSP字符

        label = item["output"].split(': ')[1]  # 分割并获取标签
        label = '1' if label == 'real' else '0'
        if len(text) < 500:
            # 按照制表符分隔的格式写入文件
            f.write(text + '\t' + label + '\n')
        else:
            continue
