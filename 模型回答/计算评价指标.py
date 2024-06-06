from sklearn.metrics import f1_score, roc_auc_score, recall_score, precision_score, accuracy_score
import json
# 假设y_true是真实标签，y_pred是模型预测的标签
# 真实标签和预测标签应该是二进制数组或多分类问题中的one-hot编码数组

# 真实标签和预测标签示例
wrong = 0
y_true = []
y_pred = []
false_ID = []
wrong_ID = []
#统计true和pred
with open('answer_Ti-CNN_explanation_label.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    for news_key in data:
        news = data[news_key]
        model_answer = news['model_answer']
        model_answer_list = model_answer.split('label: ')
        output = news['output']
        output_list = output.split('label: ')
        if (model_answer_list[-1] == 'real')&(output_list[-1] == 'real'):
            y_true.append(1)
            y_pred.append(1)
        elif (model_answer_list[-1] == 'real')&(output_list[-1] == 'fake'):
            y_true.append(1)
            y_pred.append(0)
            false_ID.append(news_key)
        elif (model_answer_list[-1] == 'fake')&(output_list[-1] == 'fake'):
            y_true.append(0)
            y_pred.append(0)
        elif (model_answer_list[-1] == 'fake')&(output_list[-1] == 'real'):
            y_true.append(0)
            y_pred.append(1)
            false_ID.append(news_key)
        else:
            wrong += 1
            wrong_ID.append(news_key)




# 计算准确率
acc = accuracy_score(y_true, y_pred)

# 计算精确率
precision = precision_score(y_pred, y_pred)

# 计算召回率
recall = recall_score(y_true, y_pred)

# 计算F1分数
f1 = f1_score(y_true, y_pred)

# 如果是二分类问题，计算AUC分数
auc = roc_auc_score(y_true, y_pred)

# 计算针对正类的F1分数
f1_real = f1_score(y_true, y_pred, pos_label=1)

# 计算针对正类的召回率
recall_real = recall_score(y_true, y_pred, pos_label=1)

# 计算针对正类的精确率
precision_real = precision_score(y_true, y_pred, pos_label=1)

# 计算针对正类的F1分数
f1_fake = f1_score(y_true, y_pred, pos_label=0)

# 计算针对正类的召回率
recall_fake = recall_score(y_true, y_pred, pos_label=0)

# 计算针对正类的精确率
precision_fake = precision_score(y_true, y_pred, pos_label=0)


# 打印结果
print(f"AUC: {auc}")
print(f"F1 Score: {f1}")
print(f"Recall: {recall}")
print(f"Precision: {precision}")
print(f"Accuracy: {acc}")
print(f"F1 Score (Real): {f1_real}")
print(f"Recall (Real): {recall_real}")
print(f"Precision (Real): {precision_real}")
print(f"F1 Score (Fake): {f1_fake}")
print(f"Recall (Fake): {recall_fake}")
print(f"Precision (Fake): {precision_fake}")
print(f"Mac F1:{(f1_real + f1_fake) / 2}")