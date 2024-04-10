from openai import OpenAI
import httpx
import os
import json
import time as times

file_path = r"data0.json"
write_path = r'Weibo_total_data_withGPT0.json'

client = OpenAI(
    base_url="https://oneapi.xty.app/v1",
    api_key="sk-z5esLCcsb4v8r6LEC9AbA72fA59d49608453B91c4eA0468b",#3.5:sk-z5esLCcsb4v8r6LEC9AbA72fA59d49608453B91c4eA0468b#4.0:sk-p6gFyC9GDkXO1do8F63cF43183Ae433f8fE32dFfDf872cBd
    http_client=httpx.Client(
        base_url="https://api.xty.app",
        follow_redirects=True,
    ),
)


num = 0
news=[]


with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    for json_contents in data:
        text = json_contents['text']
        label = json_contents['label']
        time = json_contents['time']
        if time == '':
            time = 'null'
        author = json_contents['author']
        if author == '':
            author = 'null'
        url = json_contents['url']
        if url == '':
            url = 'null'
        label_text = "label: {}\ndate: {}\nauthor: {}\nurl: {}\ntext: {}".format(label, time, author,url,text)
        print(label_text)
        attempts = 0
        while attempts<5:
            try:#获得GPT的回答
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo-0125",#gpt-4-0125-preview #gpt-3.5-turbo-0125
                    messages=[
                        {
                            "role": "system",
                            "content": "You will be responsible for explaining the authenticity of specific news reports. In this process, you will receive a piece of news text material that comes with a pre-designated label indicating its authenticity or lack thereof. Your task is to conduct a detailed analysis of this label and provide a reasonable explanation to clarify the basis on which each report is determined to be true or false. Please note that the labels for the authenticity of the news are accurate, and you only need to provide an explanation for the labels."
                                       "\nPlease note that you must explain the news according to the label provided, you don't need to label news as true or false again."
                                       "\nYour answer should follow the following format:"
                                       "\nExplanation: The news is {} because these reasons:"
                                       "\nSource reliability: XXX"
                                       "\nAuthor background: XXX"
                                       "\nEvidence test: XXX"
                                       "\nLanguage style: XXX"
                                       "\nOther analysis: XXX".format(label)
                        },
                        {
                            "role": "user",
                            "content": label_text
                        }
                    ],
                    temperature=0,
                    max_tokens=400,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                )
                answer_content = response.choices[0].message.content
                print('问题{}已回答'.format(num))
                break
            except:#如果出错，重试
                print('请求失败')
                times.sleep(2)  # 等待2秒后再次尝试
                attempts += 1  # 增加尝试次数
        else:
            print('超过最大尝试次数，跳过这个问答')
            continue
        #将输出的结果写回文件
        json_contents['GPT_analysis_0'] = answer_content
        news.append(json_contents)
        with open(write_path, 'w', encoding='utf-8') as f:
            json.dump(news, f, ensure_ascii=False, indent=4)
        num += 1

        #用于测试输出结果
        print(answer_content)

        #显示目前的处理进度
        print('{} : file has been processed\n'.format(num))
