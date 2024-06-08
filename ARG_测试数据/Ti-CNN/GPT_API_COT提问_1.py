from openai import OpenAI
import httpx
import time
import json
import random
random.seed(41)
client = OpenAI(
    base_url="https://oneapi.xty.app/v1",
    api_key="sk-z5esLCcsb4v8r6LEC9AbA72fA59d49608453B91c4eA0468b",
    # 3.5:sk-z5esLCcsb4v8r6LEC9AbA72fA59d49608453B91c4eA0468b#4.0:sk-p6gFyC9GDkXO1do8F63cF43183Ae433f8fE32dFfDf872cBd
    http_client=httpx.Client(
        base_url="https://api.xty.app",
        follow_redirects=True,
    ),
)


def Ask_GPT(system_prompt, user_prompt):
    respones = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",  # gpt-4-0125-preview #gpt-3.5-turbo-0125
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return respones


num = 0
news = []
file_path = r"Ti-CNN_data_filtered_text.json"
write_path = r'Ti-CNN_data_filtered_GPT_Commonsense.json'
start = 0
end = 500
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    random.shuffle(data)
    # start = 0
    # end = len(data)

    count = 0

    for k in range(start,end):
        json_contents = data[k]
        label_text = json_contents['text']
        print(label_text)
        system_prompt = ("You are a fake news detection expert, please analyze whether the following news "
                         "from the perspective of Commonsense.For Example:"
                         "News Content: April the giraffe with her new baby calf shortly after she gave birth last year. ( Photo : USA TODAY ) After months of questions and rumors, Animal Adventure Park owner Jordan Patch announced Wednesday the news millions of worldwide giraffe fans have been waiting to hear : April the giraffe is pregnant again. Last month, the park announced it was sending 30 days worth of fecal samples to another zoo's laboratory for progesterone testing to confirm the pregnancy, 14 months after April gave birth to her calf, Tajiri on site at the park. Keeper Allysa Swilley had collected a fecal sample from April's stall over the course of a month. The samples were secured in plastic bags, labeled and dated before being put in freezer storage. April is months into her pregnancy"
                         "Analysis: Plausibility: It is plausible that a giraffe in a zoo could become pregnant again after giving birth, so this aspect of the message is believable.\n\nVerifiability: The message mentions that the park sent fecal samples to another zoo's laboratory for testing, which suggests that there is some scientific evidence to support the claim. However, we do not have access to the results of the testing, so we cannot fully verify the claim.\n\nSource credibility: The message comes from a news article published by USA Today, which is a reputable news source. Additionally, the article quotes the owner of the Animal Adventure Park, which suggests that the information is coming from a credible source."
                         "News Content: 7 of 7 The actress is trying to re - build her life after announcing her split with Theroux just two months ago after it became apparent the air were no longer living together. We pay for juicy info! Do you have a story for RadarOnline. com? Email us at tips @ radaronline. com, or call us at ( 866 ) ON - RADAR ( 667 - 2327 ) any time, day or night. Photo credit : BACKGRID"
                         "Analysis: Plausibility: The message seems plausible as it is common for people to try to rebuild their lives after a breakup.\n\nVerifiability: The message does not provide any verifiable information or sources to support the claim.\n\nSource credibility: The message is from RadarOnline.com, which is a celebrity gossip website. The credibility of the source is questionable as they are known for publishing sensationalized stories.\n\nBased on the analysis, "
                         "Here is the news content: \n")
        system_prompt_0 = ("You will receive an evaluation of the news from a fake news expert. Please classify the "
                           "news based on the expert's evaluation. Your answer should be either '1' if the news is real"
                           "or '0' if the news is fake, do not give any explanation of your answer,your answer should "
                           "only be 1 or 0.\n"
                           "Here is the evaluation of the expert:")
        start_time = time.time()
        i = 0
        while (i < 10):
            try:
                response_0 = Ask_GPT(system_prompt, label_text)
                answer_content_0 = response_0.choices[0].message.content
                json_contents['GPT_analysis_Commonsense'] = answer_content_0
                j = 0
                while (j < 10):
                    try:
                        response_1 = Ask_GPT(system_prompt_0, answer_content_0)
                        print(answer_content_0)
                        answer_content_1 = response_1.choices[0].message.content
                        json_contents['GPT_analysis_Commonsense_answer'] = answer_content_1
                        news.append(json_contents)
                        with open(write_path, 'w', encoding='utf-8') as f:
                            json.dump(news, f, ensure_ascii=False, indent=4)
                        break
                    except Exception as e:
                        print(e)
                        print("Retrying...")
                        time.sleep(3)
                        i += 1
                        continue

                break
            except Exception as e:
                print(e)
                print("Retrying...")
                time.sleep(3)
                i += 1
                continue

        end_time = time.time()
        run_time = end_time - start_time
        num += 1
        print('{} : file has been processed\nTime used:{}'.format(num, run_time))
