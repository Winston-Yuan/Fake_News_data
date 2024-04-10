import json

true = 0  # 判断正确
false = 0  # 判断错误
wrong = 0  # 没给出判断
total = 0
false_ID = []
wrong_ID = []
with open('answer_gossipcop_explanation_label.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for news_key in data:
        news = data[news_key]
        model_answer = news['model_answer']
        model_answer_list = model_answer.split('label: ')
        output = news['output']
        output_list = output.split('label: ')
        print(news_key,output_list[-1],model_answer_list[-1])
        if model_answer_list[-1] == output_list[-1]:
            print(1)
            true += 1
        elif (model_answer_list[-1] != 'fake')&(model_answer_list[-1] != 'real'):
            print(2)
            wrong += 1
            wrong_ID.append(news_key)
        elif model_answer_list[-1] != output_list[-1]:
            print(0)
            false += 1
            false_ID.append(news_key)


        total += 1
print(true / (total-wrong))#打印剔除了偏答的答案后的准确率
print(true / total)#打印未剔除偏答的答案后的准确率
print('false_ID',false_ID)
print('wrong_ID',wrong_ID)

