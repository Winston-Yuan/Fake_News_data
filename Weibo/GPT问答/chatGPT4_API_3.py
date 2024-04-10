from openai import OpenAI
import httpx
import os
import json
import time as times

file_path = r"data3.json"
write_path = r'Weibo_total_data_withGPT3.json'

client = OpenAI(
    base_url="https://oneapi.xty.app/v1",
    api_key="sk-z5esLCcsb4v8r6LEC9AbA72fA59d49608453B91c4eA0468b",#3.5:sk-z5esLCcsb4v8r6LEC9AbA72fA59d49608453B91c4eA0468b#4.0:sk-p6gFyC9GDkXO1do8F63cF43183Ae433f8fE32dFfDf872cBd
    http_client=httpx.Client(
        base_url="https://api.xty.app",
        follow_redirects=True,
    ),
)

# text = "MADISON, Wis. -- More than 700 million adults and children worldwide are obese, according to a 2017 study that called the growing number and weight-related health problems a \"rising pandemic.\"\n\nNew battery-free, easily implantable weight-loss devices developed by engineers at the University of Wisconsin-Madison could offer a promising new weapon for battling the bulge.\n\nIn laboratory testing, the devices helped rats shed almost 40 percent of their body weight. Results of the study were published today (Dec. 17, 2018) in the journal Nature Communications.\n\nMeasuring less than 1 centimeter across, or about a third of the area of a U.S. penny, the tiny devices -- which are safe for use in the body and implantable via a minimally invasive procedure -- generate gentle electric pulses from the stomach's natural churning motions and deliver them to the vagus nerve, which links the brain and the stomach.\n\nThat gentle stimulation dupes the brain into thinking that the stomach is full after only a few nibbles of food.\n\n\"The pulses correlate with the stomach's motions, enhancing a natural response to help control food intake,\" says Xudong Wang, a UW-Madison professor of materials science and engineering.\n\nUnlike gastric bypass, which permanently alters the capacity of the stomach, the effects of the new devices also are reversible. When Wang and his collaborators removed the devices after 12 weeks, the study's rats resumed their normal eating patterns and weight bounced right back on.\n\nWang's device has several advantages over an existing unit that stimulates the vagus nerve for weight loss. That existing unit, \"Maestro,\" approved by the Food and Drug Administration in 2015, administers high-frequency zaps to the vagus nerve to shut down all communication between the brain and stomach. It requires a complicated control unit and bulky batteries which frequently must be recharged.\n\nThat ongoing maintenance can be a big barrier to use, says Luke Funk, a surgery professor in UW-Madison's Division of Minimally Invasive, Foregut and Bariatric Surgery. \"One potential advantage of the new device over existing vagus nerve stimulators is that it does not require external battery charging, which is a significant advantage when you consider the inconvenience that patients experience when having to charge a battery multiple times a week for an hour or so.\"\n\nIn fact, Wang's device contains no batteries, no electronics, and no complicated wiring. It relies instead on the undulations of the stomach walls to power its internal generators.\n\nThat means the device only stimulates the vagus nerve when the stomach moves.\n\n\"It's automatically responsive to our body function, producing stimulation when needed,\" says Wang. \"Our body knows best.\"\n\nWang is a world expert in wearable and implantable capacitive electricity-generating devices, having previously created implantable nanogenerators that harvest energy from people's beating hearts and breathing, a motion-powered bandage for wound healing, and other such devices.\n\nHe and his collaborators patented the weight-loss device through the Wisconsin Alumni Research Foundation and are moving forward with testing in larger animal models. If successful, they hope to move toward human trials.\n\n\"Our expectation is that the device will be more effective and convenient to use than other technologies,\" says Wang.\n\n###\n\nUW-Madison radiology professor Weibo Cai is also a senior author on the study.\n\nThis research was supported by grants from the National Institutes of Health (R01EB021336 and P30CA014520).\n\nSam Million-Weaver, (608) 263-5988, millionweave@wisc.edu"
# text = "They stood in line at Trump Tower, sometimes up to half an hour, handing over their cash for mementos of the president-elect: mini, gold-wrapped chocolate bricks stamped <U+201C>Trump.<U+201D> Trump monogrammed sweaters, towels and glassware. Trump cologne. <U+201C>I bought it for my two sons,<U+201D> said Shanon Loggins, 47, of Lufkin, Tex., showing off a golden shopping bag embossed with the Trump crest that carried two bottles of Success by Trump, a fragrance for men. <U+201C>They need to be successful,<U+201D> she explained. Business is good for Donald J. Trump . People are flocking to his Midtown Manhattan skyscraper, dining in his restaurants and buying his wares. Reporters are fastidiously chronicling the comings and goings of his transition team , his self-branded properties providing the backdrop for television live shots. Mr. Trump has taken the staid task of preparing to assume the presidency and turned it into an exercise in conspicuous self-promotion and carefully choreographed branding. But as the president-elect makes use of his vast real estate holdings, he is also raising questions about whether he is exploiting the high profile and stature of the office to conduct what could be seen as a promotional tour for the Trump Organization. The venues he has picked to conduct his official transition planning attest to his success as a real estate developer: Trump Tower, the Manhattan skyscraper where he lives and works amid Trump-themed eateries and boutiques; Mar-a-Lago, the upscale, private Palm Beach, Fla., club where he has chosen to hold meetings over Thanksgiving; and the Trump National Golf Club in Bedminster, N.J. Mr. Trump especially liked the Bedminster setting, he told his aides, because the images of him receiving potential cabinet appointees at the front door of the clubhouse resembled 10 Downing Street in London. In planning future transition meetings, Mr. Trump and his team are considering other properties of his that might fit his desire for rich, regal symbolism. <U+201C>It stinks,<U+201D> said Norman Eisen , who was the chief White House ethics lawyer for President Obama from 2009 to 2011. Because there is no specific law prohibiting public officeholders from financially beneficial self-promotion, what Mr. Trump is doing is probably not illegal, Mr. Eisen added. <U+201C>But that doesn<U+2019>t make it right,<U+201D> he said. <U+201C>It<U+2019>s part and parcel of the unsavory marketing of his brands that he also did during the campaign.<U+201D> Unsavory or not, it is all part of the stagecraft and spectacle that Mr. Trump has directed from his 26th-floor office in Trump Tower <U+2014> all of which is being ravenously consumed by the news media and his loyal followers. Most days since Mr. Trump became the president-elect, the lobby of Trump Tower has been a public staging area for aspects of the transition that Mr. Trump most wants people to see. Potential cabinet appointees march across its buffed marble floors, past the cameras that stream the scene live to C-Span, and into the gold mirrored elevators. This week there were people like Gov. Mary Fallin of Oklahoma and Rick Perry, the former Texas governor, who disparaged Mr. Trump as <U+201C>a cancer on conservatism<U+201D> when they were battling for the Republican nomination. Mr. Trump and his staff have even devised a proper greeting protocol for arriving guests. As Mr. Perry made his way through the lobby on Monday, a young woman looped her arm around his and escorted him past the cameras. The same woman was also on hand over the weekend to accompany visiting guests when Mr. Trump moved the meetings to Bedminster. The golf club was even more of a display of munificence, with Mr. Trump turning to the cameras to embrace Mitt Romney, who just months ago condemned Mr. Trump as a <U+201C>phony<U+201D> and a <U+201C>fraud.<U+201D> He is now a leading candidate for secretary of state. There were more ethnically diverse potential cabinet candidates there, as well, like T. W. Shannon, the first African-American speaker of the Oklahoma House, and Michelle Rhee, a former schools chancellor in Washington, who is Asian-American. When Mr. Trump was done interviewing them, he would see them off outside and, once again, banter with the news media. <U+201C>Tremendous talent <U+2014> we<U+2019>re seeing tremendous talent,<U+201D> Mr. Trump said on Saturday . <U+201C>People that, as I say, we will <U+2018>make America great again.<U+2019> These are really great people. These are really, really talented people.<U+201D> As the cameras rolled during the weekend at Bedminster, temperatures dropped sharply, sending journalists into the gift shop, where the only cold-weather attire they could find was a winter hat with Trump embroidered on it. The market for anything stamped Trump has been bustling. At the gift kiosk on the lower level of Trump Tower <U+2014> between the Trump Ice Cream Parlor and the Trump Grill, with its $25 prix fixe lunch <U+2014> the line on Monday morning was about two dozen people deep. Cashiers were doing their civic diligence, asking anyone purchasing Trump campaign gear like the <U+201C>Make America Great Again<U+201D> hats ($25) whether they were American citizens. (Law prohibits foreigners from giving money to campaigns.) Marilyn Bryan, 70, of Terre Haute, Ind., was sitting at a table outside the kiosk with her daughter Trisha. In May, Ms. Bryan was at a Trump rally in her hometown when someone passed out next to her, knocked her down and broke her femur. That might have been enough Trump for anyone else. But she decided that as long as she was visiting New York this week, she might as well stop by the tower to take in the scene. <U+201C>What<U+2019>d we spend? $200?<U+201D> she asked her daughter. Inside her shopping bag were a hat, the golden Trump chocolate bars and some other Trump knickknacks she planned to give to her relatives. The chocolate, they were somewhat disappointed to learn, was actually made in Fort Wayne, Ind. Standing nearby were Paul and Lea Foster of Hidden Hills, Calif. After purchasing two hats and two T-shirts, Ms. Foster, 62, marveled at Mr. Trump<U+2019>s ability to cash in on his name. <U+201C>He<U+2019>s sure figured out how to make money,<U+201D> she said. Her husband nodded. <U+201C>He<U+2019>s a businessman, a promoter,<U+201D> said Mr. Foster, 81. <U+201C>Let<U+2019>s hope he knows how to run the country.<U+201D> Michael S. Schmidt contributed reporting. Get politics news updates via Facebook , Twitter and the Morning Briefing newsletter . A version of this article appears in print on November 23, 2016, on Page A17 of the New York edition with the headline: At Trump<U+2019>s Properties, a Showcase for a Brand and a President-Elect. Order Reprints | Today's Paper | Subscribe"
# text = "NTEB Ads Privacy Policy Donald Trump, Bible Prophecy, And The Coming Global Shaking That Will Shock The World Listen to me, America, the time is growing ever shorter. Get your eyes off of red vs. blue and conservative vs. liberal, you will never see the truth that way. The God of Abraham, Isaac and Jacob is getting ready to insert Himself into our world in a very visible and tangible way. These are the days of prophecy. by Geoffrey Grider October 30, 2016 Join us as we apply Paul<U+2019>s command found in 2 Timothy 2:15 to <U+2018>rightly divide<U+2019> our Bible and put everything in it<U+2019>s proper perspective and place. \n<U+201C>And I will shake all nations, and the desire of all nations shall come: and I will fill this house with glory, saith the LORD of hosts.<U+201D> Haggai 2:7 (KJV) \nCLICK HERE TO LISTEN LIVE when the show starts Sunday night at 9:00PM EST! \nListen to me, America, the time is growing ever shorter. Get your eyes off of red vs. blue and conservative vs. liberal, you will never see the truth that way. The God of Abraham, Isaac and Jacob is getting ready to insert Himself into our world in a very visible and tangible way. These are the days of prophecy. CLICK IMAGE SUNDAY NIGHT AT 9:00 PM EST TO LISTEN LIVE TO THIS BIBLE STUDY \nOn this episode of Rightly Dividing , we look at the 2016 presidential election, just a little over one week away, and the coming implications it will have on the fulfillment of Bible prophecy right here and right now. We are living in exciting times, and they are about to go into end times overdrive. \nCLICK HERE TO LISTEN LIVE when the show starts Sunday night at 9:00PM EST! SHARE THIS ARTICLE Geoffrey Grider NTEB is run by end times author and editor-in-chief Geoffrey Grider. Geoffrey runs a successful web design company, and is a full-time minister of the gospel of the Lord Jesus Christ. In addition to running NOW THE END BEGINS, he has a dynamic street preaching outreach and tract ministry team in Saint Augustine, FL. NTEB #TRENDING"
# text = "俄罗斯确诊超过一万，一怒之下驱赶了上百万中国人！这些大多是在那里留学、工作和做生意的人。美国确诊40多万，还没有驱赶过一个守法的中国人。有人说，这就是文明与野蛮的差距！ O网页链接 ​俄罗斯对待这些中国人的做法，过分了！规定根本没有考虑到我入境公民的实际情况，很多中国公民刚到俄罗斯，住所中没有食物储备，如何隔离14天？有的人仅仅是下楼去超市采购生活必需品就被抓个现行，被警察带到“皇村”的“察里津诺残疾人康复中心”进行集中强制隔离。原创 ：补刀客 补壹刀执笔：吴大辉据媒体报道，有80名中国公民因违反俄方在防控新冠肺炎期间的相关隔离规定，将被俄罗斯遣返，并规定5年内不得入境。现在这80个人仍然被隔离在察里津诺残疾人康复中心，一些中国公民（含留学人员）对判决结果提出了上诉，但被莫斯科市法院二审驳回。俄罗斯对这些中国公民的重罚有没有道理？合不合适？通过与部分当事人的交流，笔者认为有以下几点值得商榷，并且必须加以厘清。01被勒令签署的《莫斯科首席国家卫生官指令》并不规范我公民入境时被俄方勒令签署《莫斯科首席国家卫生官指令》，但这个指令本身并不规范，俄方也未对其内容做出详细解释。该文件只有俄语版，而很多入境的我公民并不精通俄语，甚至根本不懂俄语，莫斯科机场的医务工作人员更不懂中文与英语。很多入境的中国公民都想当然地以为这不过是普通的例行的健康表，所以在被要求签名处随手签字。据了解，被遣返的80人中，只有10人称能听懂俄语或者明白了所签字文件的含义。这就导致多数中国公民被警察带去强制隔离时都不知道发生了什么，更不知道自己将被剥夺工作或学习签证，并被遣返出境且5年不得入境。《莫斯科首席国家卫生官指令》《莫斯科首席国家卫生官指令》笔者阅读了《莫斯科首席国家卫生官指令》，发现这是一份极不规范的文件，甚至“新冠病毒”的“病毒”一词出现了字母拼写错误（Коронавирусный的第六个字母“а”被写成了“о”）。一项严肃的法规竟出现如此粗糙的错误，让人难以想象。02《莫斯科首席国家卫生官指令》规定不符合实际情况《莫斯科首席国家卫生官指令》中的规定根本没有考虑到我入境公民的实际情况。文件规定，我入境公民要在自己住所隔离，不能去单位、学校、商店、药店及其他公共场所，不能使用公共交通工具，每天测两次体温、每天电话通报健康情况等。但是很多中国公民刚到俄罗斯，住所中没有食物储备，如何隔离14天？有的人仅仅是下楼去超市采购生活必需品就被抓个现行，被警察带到“皇村”的“察里津诺残疾人康复中心”进行集中强制隔离。察里津诺残疾人康复中心察里津诺残疾人康复中心当然，我们也不否认，这80人当中可能有明知故犯、故意违反莫斯科市政当局的疫情管控规定的人。俄罗斯新闻网4日指出，在80名被遣返回国的中国公民中，有若干人正面临新的刑事指控，他们被指在2日22日之前，违反俄罗斯的法律法规，来往于中俄两国之间，倒运医用口罩，非法牟取暴利，并涉嫌非法使用巨额现金和逃税等罪名。03法院遣返判决的庭审程序不规范由于多数人拒绝签署遣返同意书，因此当事人签字环节被取消，改为直接视频审判。据当事人讲述，视频庭审现场只有一名法官和一名翻译，法官上来就当庭宣判遣返令。整个过程只有几分钟，完全不给当事人聘请翻译进行辩护的机会。按规定，不服判决可在10天内上诉。但很多当事人仍被强行隔离中，并不具备上诉的充分条件。只能依靠我使馆的领事服务和法律援助。按照莫斯科法院判决书的规定，若不上诉，当事人将面临被强制遣返而不是自行离开，这意味着收到判决书后当事人还需要在专门的收容所等待一段时间，直到走完所有的程序，才能被遣返回中国。04防疫防范的是新冠病毒而不是中国人就像我驻俄罗斯大使馆2月24日给莫斯科市政府的照会中所谈及到的“对来自中国的所有人员进行普遍监控”。“包括美国和其他西方国家在内，当今世界上的任何国家，都没有对中国公民进行特别监视，面对病毒，中方理解莫斯科市政府采取某些措施的必要性，但希望莫斯科方面的措施可以符合预防病毒的实际，且不具备歧视性。”中国驻俄罗斯大使馆给莫斯科市政府的照会中国驻俄罗斯大使馆给莫斯科市政府的照会许多在俄罗斯的中国人感觉到被特别对待。中国驻俄罗斯大使馆3月1日的公告称，“俄方出于疫情防控需要采取的临时防疫措施，应当予以尊重。”“使馆在工作中注意到，俄执法部门对本国公民和其他国家公民也进行了防疫检查，使馆工作人员上街时也曾受到询问。据使馆了解，莫斯科市执法人员总体上执法规范，检查护照确认入境时间超过14天后即予放行。”3月7日，莫斯科市政府出台新的规定，要求两周内到访过意大利、韩国、伊朗、德国、法国和西班牙的人进入俄罗斯境内也必须自我隔离。这再次证明俄罗斯针对的是新冠病毒而非哪一国公民。然而，在俄罗斯疫情防控期间，我们也看到了个别的不利于中俄友好的不和谐之音。“中国人不得入内”堂而皇之地写在了俄罗斯达吉斯坦共和国马哈奇卡拉市一家餐厅和鞑靼斯坦共和国喀山市一家旅馆的大门上。俄罗斯马哈奇卡拉市一家餐馆门上写着“中国人不得入内”俄罗斯马哈奇卡拉市一家餐馆门上写着“中国人不得入内”笔者不免感慨，这种显而易见的歧视，与租借时期上海外滩公园那块臭名昭著的告示牌，究竟有什么区别？中俄两国关系已经走过七十年的风雨历程。我们常说战略协作伙伴关系框架下的中俄两国已成为“搬不走的好邻居，拆不散的真伙伴” “国之交在于民相亲，民相亲在于心相通。”中国疫情爆发时，俄罗斯政府给予我们无私的慷慨援助，这种大义值得我们礼赞与铭记。但当我们两国国内出现了不利于中俄关系发展的个别不和谐之音的时候，我们更应该指出其不当之处。"
# text = "【羊要来了！#蒙古国计划9月起移交30000只捐赠羊#】2020年 7月31日，蒙古国外交部邻国局局长巴特策策格回应“蒙古国总统访华期间向中国捐赠3万只羊”的落实情况时表示，经同中方进行协商，商定在新冠疫情趋于缓和后，#蒙古国捐赠的3万只羊肥壮后分批移交#。蒙方计划，首批活羊将于9月向中方移交。O蒙古国那30000只羊9月开始要来了！待羊群肥壮..."

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
        while attempts < 5:
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo-0125",  # gpt-4-0125-preview #gpt-3.5-turbo-0125
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
            except:
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
