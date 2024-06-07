import random

random.seed(41)


with open('data.txt','r',encoding='utf-8') as f:
    data = f.read()
    data_list = data.split('\n')
    random.shuffle(data_list)
with open('dev.txt','w',encoding='utf-8') as f:
    for i in range(0,int(len(data_list)/10)):
        f.write(data_list[i]+'\n')
with open('test.txt','w',encoding='utf-8') as f:
    for i in range(int(len(data_list)/10),int(2*len(data_list)/10)):
        f.write(data_list[i]+'\n')
with open('train.txt','w',encoding='utf-8') as f:
    for i in range(int(2*len(data_list)/10),len(data_list)):
        f.write(data_list[i]+'\n')