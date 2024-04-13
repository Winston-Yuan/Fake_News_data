import json
true = 0  # 判断正确
false = 0  # 判断错误
wrong = 0  # 没给出判断
total = 0

TP = 0
FP = 0
FN = 0
TN = 0

false_ID = []
wrong_ID = []
with open('answer_CHECKED_only_label.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for news_key in data:
        news = data[news_key]
        model_answer = news['model_answer']
        model_answer_list = model_answer.split('label: ')
        output = news['output']
        output_list = output.split('label: ')
        print(news_key, output_list[-1], model_answer_list[-1])
        if (model_answer_list[-1] == 'real') & (output_list[-1] == 'real'):
            TP += 1
        elif (model_answer_list[-1] == 'real') & (output_list[-1] == 'fake'):
            FP += 1
            false_ID.append(news_key)
        elif (model_answer_list[-1] == 'fake') & (output_list[-1] == 'fake'):
            TN += 1
        elif (model_answer_list[-1] == 'fake') & (output_list[-1] == 'real'):
            FN += 1
            false_ID.append(news_key)
        else:
            wrong += 1
            wrong_ID.append(news_key)
        total += 1

precision = TP / (TP + FP)
recall = TP / (TP + FN)
Accuracy = (TP + TN) / (TP + TN + FP + FN)
F1 = 2 * (precision * recall / (precision + recall))

print('Precision:', precision)
print('Recall:', recall)
print('Accuracy:', Accuracy)
print('F1:', F1)

print('false_ID:', false_ID)
print('wrong_ID:', wrong_ID)

