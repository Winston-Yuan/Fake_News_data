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
        max_tokens=400,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return respones


num = 0
news = []
file_path = r"gossipcop_total_5000.json"
write_path = r'gossipcop_total_with4GPT_2.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    random.shuffle(data)
    for json_contents in data:
        label_text = json_contents['news_content']
        system_prompt = ("Assume the role of a fake news detection expert. Your task is to analyze the "
                         "authenticity of a news article by examining Source Reliability, Author Background, "
                         "Evidence, and Language style. You will receive a piece of news content, and you are "
                         "asked to analyze its authenticity according to the following format:"
                         "\nSource Reliability: XXX"
                         "\nAuthor Background: XXX"
                         "\nEvidence: XXX"
                         "\nLanguage style: XXX"
                         "\nIn conclusion, the news is more likely to be true/false."
                         "Here is an example of the answer: Source Reliability: People's Daily is one of the "
                         "most authoritative newspapers in China, directly under the supervision of the Chinese "
                         "Communist Party.   It is generally considered a reliable and official source of news "
                         "in China.  \n\nAuthor Background: The author is listed as null, which is unusual as "
                         "most news articles would attribute an author.   However, given that this news was "
                         "posted on the official Weibo (microblogging) account of People's Daily, "
                         "it can be assumed that the article was published by a journalist or editor affiliated "
                         "with the newspaper.  \n\nEvidence: The news provides specific details about the "
                         "landslide incident that occurred in Lishui City, Zhejiang Province, China.   It "
                         "mentions the exact time of the incident, the location, the number of people missing, "
                         "rescued, confirmed dead, and those still missing.   The information seems to be based "
                         "on official reports, likely from government sources or rescue authorities.  "
                         "\n\nLanguage style: The language used in the news article is straightforward and "
                         "factual, typical of news reports from official sources.   There are no "
                         "sensationalized elements or speculative language present.  \n\nIn conclusion, "
                         "the news is more likely to be true.")
        system_prompt_0 = ("You will receive an evaluation of the news from a fake news expert. Please classify the "
                           "news based on the expert's evaluation. Your answer should be either '1' if the news is real"
                           "or '0' if the news is fake, do not give any explanation of your answer,your answer should only be 1 or 0."
                           # "Here is an example: Evaluation: Source Reliability: TMZ is known for its celebrity news "
                           # "coverage and paparazzi-style reporting. While it often breaks celebrity-related stories, "
                           # "its reliability can vary, and it's not considered a highly authoritative or credible "
                           # "source for news.\n\nAuthor Background: The author of the article is not specified, "
                           # "which is common in tabloid-style reporting. The information seems to be based on "
                           # "eyewitness accounts and possibly video footage obtained by TMZ's reporters.\n\nEvidence: "
                           # "The article provides details of an incident involving Shia LaBeouf at Pinz bowling alley "
                           # "in Studio City, Los Angeles. It describes his behavior, including verbal altercations and "
                           # "being asked to leave the premises. Video footage is mentioned as additional evidence of "
                           # "the incident.\n\nLanguage style: The language used in the article is sensationalized and "
                           # "tabloid-like, typical of TMZ's style. Phrases like \"freaking out\" and \"got rowdy\" "
                           # "contribute to the sensational tone.\n\nIn conclusion, while the article provides some "
                           # "evidence of the incident, its reliability is limited due to TMZ's reputation for "
                           # "tabloid-style reporting and lack of specific authorship. The sensational language also "
                           # "raises questions about the objectivity of the reporting."
                           # "Your answer: 0"
                           # "Baseed on the example, give your answer of the Evaluation:")
                           "Here is the evaluation of the expert:")
        start_time = time.time()
        i = 0
        while (i < 10):
            try:
                response_0 = Ask_GPT(system_prompt, label_text)
                answer_content_0 = response_0.choices[0].message.content
                json_contents['GPT_analysis_2'] = answer_content_0
                j = 0
                while (j < 10):
                    try:
                        response_1 = Ask_GPT(system_prompt_0, answer_content_0)
                        print(answer_content_0)
                        answer_content_1 = response_1.choices[0].message.content
                        json_contents['GPT_analysis_2_answer'] = answer_content_1
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
        print('{} : file has been processed\nTime uesd:{}'.format(num, run_time))
        if num >= 500:
            break
