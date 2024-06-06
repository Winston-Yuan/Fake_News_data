import json
from collections import defaultdict

# 加载数据集
with open('gossipcop_title.json', 'r',encoding='utf-8') as f:
    gossipcop_data = json.load(f)

with open('Ti-CNN_title.json', 'r',encoding='utf-8') as f:
    Ti_CNN_data = json.load(f)

# 文本预处理函数
def preprocess_title(title):
    # 转换为小写
    title = title.lower()
    # 移除标点符号
    title = ''.join([c for c in title if c.isalnum() or c.isspace()])
    # 移除多余空格，只保留一个
    title = ' '.join(title.split())
    return title

# 预处理新闻标题并存储在集合中
gossipcop_titles = set(preprocess_title(title) for title in gossipcop_data.values())
Ti_CNN_titles = set(preprocess_title(title) for title in Ti_CNN_data.values())

# 比较新闻标题并找出重复的
duplicate_titles = gossipcop_titles.intersection(Ti_CNN_titles)

# 输出结果
print("重复的新闻标题:")
for title in duplicate_titles:
    print(title)