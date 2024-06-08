from typing import Union, List
def check_input_type(text: Union[str, List[str], List[List[str]]]) -> bool:
    # 检查是否为单个字符串
    if isinstance(text, str):
        return True
    # 检查是否为字符串列表（包括预分词的例子）
    elif isinstance(text, list) and text and all(isinstance(item, str) for item in text):
        return True
    # 检查是否为字符串列表的列表（预分词例子的批量）
    elif isinstance(text, list) and text and all(isinstance(sublist, list) and all(isinstance(item, str) for item in sublist) for sublist in text):
        return True
    else:
        return False

with open('train.txt','r',encoding='utf-8') as f:
    total_data = []
    data = f.read()
    data_list = data.split('\n')
    for item in data_list:
        item = item.split('\t')
        total_data.append(item)
for item in total_data:
    if check_input_type(item[0]) == False:
        print(item)