import json

read_path = 'Weibo_total_data_GPT.json'
write_path = 'Weibo_total_data_analysis.json'
total_data = []
with open(read_path,'r',encoding='utf-8') as f:
    data = json.load(f)
    for news in data:
        GPT_analysis = news['GPT_analysis_0']
        try :
            news['analysis'] = 'Source reliability:' + GPT_analysis.split('Source reliability:')[1]
            total_data.append(news)
        except:continue


with open(write_path,'w',encoding='utf-8') as f:
    json.dump(total_data,f,ensure_ascii=False,indent=4)






