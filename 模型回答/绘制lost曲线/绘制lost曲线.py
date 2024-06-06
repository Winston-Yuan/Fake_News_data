import json
import matplotlib.pyplot as plt

step = []
loss = []

with open ('trainer_state_explanation_label.json','r',encoding='utf-8') as f:
    data = json.load(f)
    log_history = data ['log_history']
    for logs in log_history:
        print(logs)
        step.append(logs['step'])
        loss.append(logs['loss'])
plt.plot(step, loss, label='Loss Curve', color='lightblue', linestyle='solid', marker='')

# 添加标题和标签
plt.title('Loss Curve')
plt.xlabel('steps')
plt.ylabel('Loss')

# 添加图例
plt.legend()


# 显示图表
plt.show()