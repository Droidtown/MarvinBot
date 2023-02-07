#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 3.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No matching Intent."
                }
            ]
        }
"""

from requests import post
from requests import codes
import math
import re
try:
    from intent import Loki_animal
    from intent import Loki_relationship
    from intent import Loki_school
    from intent import Loki_humilation
    from intent import Loki_pet
    from intent import Loki_season
    from intent import Loki_encouragement
    from intent import Loki_understanding
    from intent import Loki_joke
    from intent import Loki_experience
    from intent import Loki_plan
    from intent import Loki_vehicle
    from intent import Loki_warning
    from intent import Loki_bye
    from intent import Loki_family
    from intent import Loki_weather
    from intent import Loki_disagree
    from intent import Loki_feelings
    from intent import Loki_food
    from intent import Loki_command
    from intent import Loki_ending
    from intent import Loki_activity
    from intent import Loki_greeting
    from intent import Loki_game
    from intent import Loki_chat
    from intent import Loki_appearance
    from intent import Loki_agree
    from intent import Loki_recreation
    from intent import Loki_color
    from intent import Loki_job
    from intent import Loki_security
    from intent import Loki_language
    from intent import Loki_compliment
    from intent import Loki_ability
    from intent import Loki_age
    from intent import Loki_life
    from intent import Loki_location
    from intent import Loki_contact
    from intent import Loki_personal
    from intent import Loki_apology
except:
    from .intent import Loki_animal
    from .intent import Loki_relationship
    from .intent import Loki_school
    from .intent import Loki_humilation
    from .intent import Loki_pet
    from .intent import Loki_season
    from .intent import Loki_encouragement
    from .intent import Loki_understanding
    from .intent import Loki_joke
    from .intent import Loki_experience
    from .intent import Loki_plan
    from .intent import Loki_vehicle
    from .intent import Loki_warning
    from .intent import Loki_bye
    from .intent import Loki_family
    from .intent import Loki_weather
    from .intent import Loki_disagree
    from .intent import Loki_feelings
    from .intent import Loki_food
    from .intent import Loki_command
    from .intent import Loki_ending
    from .intent import Loki_activity
    from .intent import Loki_greeting
    from .intent import Loki_game
    from .intent import Loki_chat
    from .intent import Loki_appearance
    from .intent import Loki_agree
    from .intent import Loki_recreation
    from .intent import Loki_color
    from .intent import Loki_job
    from .intent import Loki_security
    from .intent import Loki_language
    from .intent import Loki_compliment
    from .intent import Loki_ability
    from .intent import Loki_age
    from .intent import Loki_life
    from .intent import Loki_location
    from .intent import Loki_contact
    from .intent import Loki_personal
    from .intent import Loki_apology


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
USERNAME = ""
LOKI_KEY = ""
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []
INPUT_LIMIT = 20

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "{} Connection failed.".format(result.status_code)
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    # 將 intent 會使用到的 key 預先設爲空列表
    resultDICT = {
       #"key": []
    }
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # animal
                if lokiRst.getIntent(index, resultIndex) == "animal":
                    resultDICT = Loki_animal.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # relationship
                if lokiRst.getIntent(index, resultIndex) == "relationship":
                    resultDICT = Loki_relationship.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # school
                if lokiRst.getIntent(index, resultIndex) == "school":
                    resultDICT = Loki_school.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # humilation
                if lokiRst.getIntent(index, resultIndex) == "humilation":
                    resultDICT = Loki_humilation.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # pet
                if lokiRst.getIntent(index, resultIndex) == "pet":
                    resultDICT = Loki_pet.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # season
                if lokiRst.getIntent(index, resultIndex) == "season":
                    resultDICT = Loki_season.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # encouragement
                if lokiRst.getIntent(index, resultIndex) == "encouragement":
                    resultDICT = Loki_encouragement.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # understanding
                if lokiRst.getIntent(index, resultIndex) == "understanding":
                    resultDICT = Loki_understanding.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # joke
                if lokiRst.getIntent(index, resultIndex) == "joke":
                    resultDICT = Loki_joke.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # experience
                if lokiRst.getIntent(index, resultIndex) == "experience":
                    resultDICT = Loki_experience.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # plan
                if lokiRst.getIntent(index, resultIndex) == "plan":
                    resultDICT = Loki_plan.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # vehicle
                if lokiRst.getIntent(index, resultIndex) == "vehicle":
                    resultDICT = Loki_vehicle.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # warning
                if lokiRst.getIntent(index, resultIndex) == "warning":
                    resultDICT = Loki_warning.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # bye
                if lokiRst.getIntent(index, resultIndex) == "bye":
                    resultDICT = Loki_bye.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # family
                if lokiRst.getIntent(index, resultIndex) == "family":
                    resultDICT = Loki_family.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # weather
                if lokiRst.getIntent(index, resultIndex) == "weather":
                    resultDICT = Loki_weather.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # disagree
                if lokiRst.getIntent(index, resultIndex) == "disagree":
                    resultDICT = Loki_disagree.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # feelings
                if lokiRst.getIntent(index, resultIndex) == "feelings":
                    resultDICT = Loki_feelings.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # food
                if lokiRst.getIntent(index, resultIndex) == "food":
                    resultDICT = Loki_food.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # command
                if lokiRst.getIntent(index, resultIndex) == "command":
                    resultDICT = Loki_command.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # ending
                if lokiRst.getIntent(index, resultIndex) == "ending":
                    resultDICT = Loki_ending.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # activity
                if lokiRst.getIntent(index, resultIndex) == "activity":
                    resultDICT = Loki_activity.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # greeting
                if lokiRst.getIntent(index, resultIndex) == "greeting":
                    resultDICT = Loki_greeting.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # game
                if lokiRst.getIntent(index, resultIndex) == "game":
                    resultDICT = Loki_game.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # chat
                if lokiRst.getIntent(index, resultIndex) == "chat":
                    resultDICT = Loki_chat.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # appearance
                if lokiRst.getIntent(index, resultIndex) == "appearance":
                    resultDICT = Loki_appearance.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # agree
                if lokiRst.getIntent(index, resultIndex) == "agree":
                    resultDICT = Loki_agree.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # recreation
                if lokiRst.getIntent(index, resultIndex) == "recreation":
                    resultDICT = Loki_recreation.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # color
                if lokiRst.getIntent(index, resultIndex) == "color":
                    resultDICT = Loki_color.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # job
                if lokiRst.getIntent(index, resultIndex) == "job":
                    resultDICT = Loki_job.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # security
                if lokiRst.getIntent(index, resultIndex) == "security":
                    resultDICT = Loki_security.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # language
                if lokiRst.getIntent(index, resultIndex) == "language":
                    resultDICT = Loki_language.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # compliment
                if lokiRst.getIntent(index, resultIndex) == "compliment":
                    resultDICT = Loki_compliment.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # ability
                if lokiRst.getIntent(index, resultIndex) == "ability":
                    resultDICT = Loki_ability.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # age
                if lokiRst.getIntent(index, resultIndex) == "age":
                    resultDICT = Loki_age.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # life
                if lokiRst.getIntent(index, resultIndex) == "life":
                    resultDICT = Loki_life.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # location
                if lokiRst.getIntent(index, resultIndex) == "location":
                    resultDICT = Loki_location.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # contact
                if lokiRst.getIntent(index, resultIndex) == "contact":
                    resultDICT = Loki_contact.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # personal
                if lokiRst.getIntent(index, resultIndex) == "personal":
                    resultDICT = Loki_personal.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # apology
                if lokiRst.getIntent(index, resultIndex) == "apology":
                    resultDICT = Loki_apology.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def execLoki(content, filterLIST=[], splitLIST=[]):
    """
    input
        content       STR / STR[]    要執行 loki 分析的內容 (可以是字串或字串列表)
        filterLIST    STR[]          指定要比對的意圖 (空列表代表不指定)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                     * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content

    output
        resultDICT    DICT           合併 runLoki() 的結果，請先設定 runLoki() 的 resultDICT 初始值

    e.g.
        splitLIST = ["！", "，", "。", "？", "!", ",", "
", "；", "　", ";"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？")                      # output => ["今天天氣"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？", splitLIST=splitLIST) # output => ["今天天氣", "後天氣象"]
        resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"])                # output => ["今天天氣", "後天氣象"]
    """
    contentLIST = []
    if type(content) == str:
        contentLIST = [content]
    if type(content) == list:
        contentLIST = content

    resultDICT = {}
    if contentLIST:
        if splitLIST:
            # 依 splitLIST 做分句切割
            splitPAT = re.compile("[{}]".format("".join(splitLIST)))
            inputLIST = []
            for c in contentLIST:
                tmpLIST = splitPAT.split(c)
                inputLIST.extend(tmpLIST)
            # 去除空字串
            while "" in inputLIST:
                inputLIST.remove("")
        else:
            # 不做分句切割處理
            inputLIST = contentLIST

        # 依 INPUT_LIMIT 限制批次處理
        for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
            lokiResultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)
            if "msg" in lokiResultDICT:
                return lokiResultDICT

            # 將 lokiResultDICT 結果儲存至 resultDICT
            for k in lokiResultDICT:
                if k not in resultDICT:
                    resultDICT[k] = []
                resultDICT[k].extend(lokiResultDICT[k])

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # animal
    print("[TEST] animal")
    inputLIST = ['烏龜很棒','雞會飛嗎','你喜歡狗嗎','你喜歡什麼動物','你會害怕蝙蝠嗎','你有看過大象嗎','你在哪裡看到熊貓','你對袋鼠了解多少','你曾經看過袋鼠嗎','你為什麼喜歡熊貓','猴子喜歡吃香蕉嗎','你最喜歡的動物是什麼','為什麽在美國看不到袋鼠','世界上最聰明的動物是什麼']
    testLoki(inputLIST, ['animal'])
    print("")

    # relationship
    print("[TEST] relationship")
    inputLIST = ['吻我','他是誰','抱一個','親一個','你單身嗎','來個親親','你不喜歡我','你喜歡我嗎','我們結婚吧','你在約會中嗎','你願意娶我嗎','想出去約會嗎','我們在一起吧','我有男朋友了','你想去哪裡約會','你正在交往中嗎','你願意嫁給我嗎','當我的朋友好嗎','你男友叫什麼名字','我想要一個女朋友','你想要我帶你去哪裡玩','你願意當我的男朋友嗎','你願意跟我出去約會嗎','我和我的家人關係融洽','你認為你男友應該要多大','我不知道你有沒有男朋友','你有和男生交往過的經驗嗎','我要怎麼知道他是不是也喜歡我']
    testLoki(inputLIST, ['relationship'])
    print("")

    # school
    print("[TEST] school")
    inputLIST = ['你主修什麼','我讀經濟系','你在哪個班級','你是大學生嗎','你要寫論文嗎','你讀哪個科系','你讀哪所大學','你喜歡數學課嗎','你多久讀一次書','你有任何作業嗎','你的主修是什麼','我是一個大學生','這個科目好玩嗎','你修過什麼體育課','你覺得上學好玩嗎','你覺得大學好玩嗎','你的學校生活怎麼樣','我在美國讀麻省理工','我在台灣大學主修經濟','你覺得讀大學是必要的嗎','我在台灣大學就讀歷史系','你比較喜歡數學還是國文課','你會不會擔心你的科系沒辦法賺錢','你知道怎樣能快速的學好一種語言嗎']
    testLoki(inputLIST, ['school'])
    print("")

    # humilation
    print("[TEST] humilation")
    inputLIST = ['滾','你好笨','你真笨','去死吧']
    testLoki(inputLIST, ['humilation'])
    print("")

    # pet
    print("[TEST] pet")
    inputLIST = ['你有養蛇嗎','我有養一隻貓','你多久溜一次狗','你想養什麼寵物','你有養幾隻寵物','兔子適合飼養嗎','我想養一隻寵物','牠的名字是什麼','你有養任何寵物嗎','你的狗叫什麼名字','你餵你的狗吃什麼','兔子適合當寵物嗎','你會考慮養隻寵物嗎','我家曾經養過一隻貓','你最喜歡的寵物是什麼','你每個月花了多少錢在寵物上','我喜歡小狗，要用什麼餵牠們','我阿姨有養一隻可愛的小兔子']
    testLoki(inputLIST, ['pet'])
    print("")

    # season
    print("[TEST] season")
    inputLIST = ['你喜歡春天嗎','今年冬天很溫暖','你覺得夏天如何','你最喜歡什麼季節','你最喜歡的季節是','加拿大夏天會很熱嗎','你喜歡夏天的哪一部份','我最喜歡的季節是春天']
    testLoki(inputLIST, ['season'])
    print("")

    # encouragement
    print("[TEST] encouragement")
    inputLIST = ['加油','你做得到','你可以的','我相信你','我們來試一試','讓我們試試看','讓我看看你有什麼能耐']
    testLoki(inputLIST, ['encouragement'])
    print("")

    # understanding
    print("[TEST] understanding")
    inputLIST = ['我不懂','我懂了','什麼意思','我不明白','我不知道','我明白了','我知道了','我聽不懂','你聽得懂嗎','你懂我的意思嗎','我想是我搞錯了','你知道我在說什麼嗎','我想我誤解你的意思了']
    testLoki(inputLIST, ['understanding'])
    print("")

    # joke
    print("[TEST] joke")
    inputLIST = ['布和紙怕什麽']
    testLoki(inputLIST, ['joke'])
    print("")

    # experience
    print("[TEST] experience")
    inputLIST = ['你坐過船嗎','你上過多少課','你打過球賽嗎','你搭過飛機嗎','你有浮潛過嗎','你看過中醫嗎','你跑過接力嗎','我想去日本玩','我養過一隻貓','你去過幾個國家','你去過葡萄牙嗎','你參加過球賽嗎','你曾經接吻過嗎','你曾經騎過馬嗎','你去台灣旅遊過嗎','你吃過哈根達斯嗎','你有在美國住過嗎','你跟女生接吻過嗎','你通常都怎麼旅遊','我上週去義大利玩','我想帶你去海邊玩','我曾經去非洲玩過','你多常去一次健身房','你想去澳洲玩玩看嗎','你會每天去健身房嗎','你有玩過高空彈跳嗎','我上週去義大利旅行','我去年換了兩個工作','我四年前養過一條狗','我常常去吃泰式料理','你最喜歡的記憶是什麼','你有參加過大隊接力嗎','你有去過百慕達三角洲嗎','我和家人常常去吃印尼菜','你出去玩是坐船還是坐飛機','你印象最深刻的記憶是什麼','你曾經在任何公司工作過嗎','我剛剛和我的家人去看電影','我三天前收到一個完美的禮物','我昨天吃了一個超大的生日蛋糕']
    testLoki(inputLIST, ['experience'])
    print("")

    # plan
    print("[TEST] plan")
    inputLIST = ['你怎麼看','你覺得如何','我們要去哪','你下週有安排嗎','你今天會去工作嗎','你今天有什麼計畫','你下週打算要做什麼','你打算要怎麼過耶誕節','你耶誕節有任何計畫嗎','我下週要去看一場棒球賽','因為下雨，我得取消我的野餐計畫','我得取消我的野餐計畫因為會下雨']
    testLoki(inputLIST, ['plan'])
    print("")

    # vehicle
    print("[TEST] vehicle")
    inputLIST = ['你想買車嗎','你會開車嗎','你有一台嗎','我是說車子','我想去比賽車','我指藍寶堅尼','我開的車是BMW','我喜歡瑪莎拉蒂','我想去騎摩托車','那是一台法拉利','你知道怎麼開車嗎','我們來比摩托車吧','我有一台藍寶堅尼']
    testLoki(inputLIST, ['vehicle'])
    print("")

    # warning
    print("[TEST] warning")
    inputLIST = ['我想自殺']
    testLoki(inputLIST, ['warning'])
    print("")

    # bye
    print("[TEST] bye")
    inputLIST = ['保重','再見','下次見','下週見','回頭見','我得走了','明天再聊','我要下線了','我明天會回來','明天再和你說','我現在必須走了','祝你有個美好的一天']
    testLoki(inputLIST, ['bye'])
    print("")

    # family
    print("[TEST] family")
    inputLIST = ['你有小孩嗎','你和家人住嗎','你家有幾個人','你有幾個表弟','我家有五個人','我有一個弟弟','你姐姐是學生嗎','你爸媽最近好嗎','你和家人關係好嗎','你姊姊叫什麼名字','你家假日都在做什麼','你怎麼稱呼你的爸媽','你有任何兄弟姊妹嗎','你有幾個表兄弟姊妹','你有幾個阿姨和舅舅','你的爸媽還在工作嗎','你多久回去見爸媽一次','你多常和姐姐說一次話','你家人通常都在做什麼','你是最大的還是最小的','你最常說話的家人是誰','你會和家人分享事情嗎','我每兩週會見到一次家人','你多常花時間陪伴你的爸媽']
    testLoki(inputLIST, ['family'])
    print("")

    # weather
    print("[TEST] weather")
    inputLIST = ['我喜歡雨天','今天天氣好嗎','今天天氣如何','今天天氣很好','你喜歡雨天嗎','台灣天氣如何','你那邊天氣如何','你的國家會下雪嗎','台北現在天氣如何','我希望明天出太陽','我希望明天是晴天','現在台北天氣如何','你覺得天氣預報準嗎','你每天會看氣象預報嗎']
    testLoki(inputLIST, ['weather'])
    print("")

    # disagree
    print("[TEST] disagree")
    inputLIST = ['沒事','不重要','我不想','沒什麼','無所謂','我不確定','與你無關','那不是真的','跟你沒有關係']
    testLoki(inputLIST, ['disagree'])
    print("")

    # feelings
    print("[TEST] feelings")
    inputLIST = ['好喔','愛你','笑死','酷喔','我很好','我愛你','我沒事','你會笑嗎','你還好嗎','太酷了吧','我很失望','我想你了','我討厭你','說你愛我','別讓我難過','我不喜歡你','不要讓我失望','你傷害到我了','你相信愛情嗎','告訴我你愛我','我感到很傷心','我覺得很難過','你愛你的家人嗎','你最近過得好嗎','我不喜歡這句話','我今天過得很糟','我對你太失望了','人們總是讓我頭痛','怎樣才算愛一個人','我今天過得糟透了','我討厭你這樣對我','你剛剛是在羞辱我嗎','我不想要當你的朋友','我需要有人跟我說說話','我不喜歡你剛剛對我做的事']
    testLoki(inputLIST, ['feelings'])
    print("")

    # food
    print("[TEST] food")
    inputLIST = ['我餓了','會餓嗎','你餓了嗎','我愛壽司','你會吃辣嗎','你會煮什麼','拉麵好吃嗎','你午餐吃什麼','你喜歡吃什麼','你會吃培根嗎','午餐時間到了','我喜歡冰淇淋','披薩還是捲餅','你喜歡什麼食物','我喜歡吃冰淇淋','我喜歡喝檸檬汁','你有什麼不吃的嗎','你今天午餐吃了什麼','你喜歡吃中式料理嗎','你會在冬天吃冰淇淋嗎','你最喜歡吃的食物是什麼','你最喜歡喝的飲料是什麼','漢堡王裡你最喜歡吃什麼','你要香草還是巧克力口味的','你喜歡香草還是巧克力口味的']
    testLoki(inputLIST, ['food'])
    print("")

    # command
    print("[TEST] command")
    inputLIST = ['停止','唱歌','閉嘴','給我禮物','買手機給我','跟我說點話','問我一些問題','替我跳一隻舞','聽從我的指令','跟我說一個笑話','說點有趣的事來聽聽']
    testLoki(inputLIST, ['command'])
    print("")

    # ending
    print("[TEST] ending")
    inputLIST = ['沒事','忘了它','我無言','沒關係','我想就是這樣']
    testLoki(inputLIST, ['ending'])
    print("")

    # activity
    print("[TEST] activity")
    inputLIST = ['我喜歡露營','我喜歡去露營']
    testLoki(inputLIST, ['activity'])
    print("")

    # greeting
    print("[TEST] greeting")
    inputLIST = ['你姓什麼','你今天怎麼樣','你叫什麼名字','嗨，我叫小花','很高興認識你','我很好，你呢','我很高興聽到','我明白我很好','我知道你很好','你好，你今天好嗎','我今天過得很愉快','我很好，謝謝。那你呢']
    testLoki(inputLIST, ['greeting'])
    print("")

    # game
    print("[TEST] game")
    inputLIST = ['敲敲門','我喜歡玩','你喜歡玩什麼','我喜歡打電動','那電玩遊戲呢','你為什麼喜歡它','你聽過什麼遊戲','那個遊戲好玩嗎','你多久玩一次麥塊','你會玩圈圈叉叉嗎','你會看遊戲實況嗎','我們來聊聊電玩吧','我比較喜歡紅土場地','你喜歡什麼類型的遊戲','你有玩過剪刀石頭布嗎','你有贊助任何實況主嗎','我們來玩剪刀石頭布吧','我喜歡自己玩上古捲軸','你知道有什麼破冰遊戲嗎','你最喜歡的電玩遊戲是什麼','我喜歡簡單一點的遊戲，像是憤怒鳥']
    testLoki(inputLIST, ['game'])
    print("")

    # chat
    print("[TEST] chat")
    inputLIST = ['在嗎','巧了','真巧','酷喔','你是什麼','你確定嗎','你還在嗎','我了解了','我是人類','有問題嗎','誰創造你','你不是人類','你住在哪裡','你在做什麼','你感覺如何','你是人類嗎','你是哪裡人','你是真的嗎','你會做什麼','你會微笑嗎','你會抽煙嗎','你有名字嗎','你的名字是','你相信神嗎','我更喜歡你','我沒有祕密','誰告訴你的','跟我說點話','你喜歡做什麼','你從哪裡來的','你想要聊什麼','你是怎樣的人','你是誰創造的','你會查google嗎','你會講笑話嗎','你有什麼興趣','你根本不懂我','你的主人是誰','你看得到我嗎','你還想聊什麼','問我一個問題','我可以揍你嗎','我有很多想法','新聞在說什麼','為什麽這麼問','現在就告訴我','真是個好名字','還有其他的嗎','你今天做了什麼','你可以做什麼事','你喜歡被擁抱嗎','你想來我家玩嗎','你會不會忘記我','你有交往對象嗎','你有任何夢想嗎','你的名字很好聽','你的底線在哪裡','你的生日是幾號','你的身高幾公尺','我們可以聊聊嗎','我喜歡吃冰淇淋','我喜歡喝檸檬汁','我要怎麼稱呼你','我討厭加拿大人','說個笑話來聽聽','你可以幫我做什麼','你可以把它脫掉嗎','你喜歡我的哪一點','你對政治的看法是','你想要出去走走嗎','你是一個機器人嗎','你是不是在嘲笑我','你是男生還是女生','你知道它的名字嗎','我可以問你問題嗎','我想問你一些問題','我是一個有趣的人','我覺得我更困惑了','你對政治有什麼看法','你會在網路上聊天嗎','很高興聽到你這麼說','我們可以走得更遠嗎','我可以摸你的腹肌嗎','我可以碰你的頭髮嗎','我是一個聊天機器人','我要告訴你一個祕密','猜猜我今天做了什麼','你最喜歡的東西是什麼','你為什麽不喜歡遊樂園','告訴我你最喜歡的事情','我其實是偽裝的外星人','為什麼大家都叫你小花','猜猜今天發生了什麼事','告訴我更多有關你的事情','你喜歡室內活動或室外活動','你有任何偏好的衛生紙品牌嗎','你不覺得原著永遠比電影好看嗎','你假日的時候喜歡待在家還是出去旅遊','我正在接受訓練成為一個專業客服人員']
    testLoki(inputLIST, ['chat'])
    print("")

    # appearance
    print("[TEST] appearance")
    inputLIST = ['180公分','你好醜','你很瘦嗎','你有多高','你身高多少','你長的好醜','我該減肥了','你今天穿什麼','你喜歡怎麼穿','你很適合紅色','你會戴圍巾嗎','你會穿裙子嗎','你有大鼻子嗎','你有幾件衣服','你有染頭髮嗎','你長的怎麼樣','我也喜歡制服','我看起來如何','你會怎麼形容我','你的屁股性感嗎','你覺得我漂亮嗎','我喜歡你的小腿','我想要有大鼻子','你今天的打扮很棒','你喜歡怎樣的衣服','你會穿什麼去上班','你的鞋子尺寸多大','女人怎樣才算漂亮','我的頭髮是金色的','我該穿什麼去學校','你今天看起來很漂亮','你喜歡綠色的眼睛嗎','你會怎麼形容你自己','你有把頭髮染成棕色嗎','你的眼睛是什麼顏色的','你冬天的時候會戴圍巾嗎','你的頭髮為什麼是黑色的','你的衣服大多是什麼顏色的']
    testLoki(inputLIST, ['appearance'])
    print("")

    # agree
    print("[TEST] agree")
    inputLIST = ['當然','我也是','我認同','那好吧','你是對的','跟我一樣','這是真的','那挺好的','我完全同意','你可以再說一遍','我不能再同意你了']
    testLoki(inputLIST, ['agree'])
    print("")

    # recreation
    print("[TEST] recreation")
    inputLIST = ['你會唱歌嗎','你會運動嗎','我喜歡油畫','我會打排球','我會畫風景','要一起看嗎','你喜歡畫畫嗎','你喜歡閱讀嗎','你喜歡雕塑嗎','你是棒球迷嗎','你會什麼樂器','你會打排球嗎','唱首歌來聽聽','我喜歡打棒球','你喜歡哪種藝術','你喜歡打排球嗎','你喜歡玩網球嗎','你喜歡看電影嗎','你想一起去看嗎','你會任何樂器嗎','你會彈什麼樂器','你有做什麼運動','你知道王力宏嗎','你們的隊伍贏了嗎','你知道麥可喬丹嗎','棒球的規則是什麼','你喜歡看恐怖電影嗎','你對打排球有興趣嗎','你工作時會聽音樂嗎','你支持的隊伍贏了嗎','你看過任何動作片嗎','哪首歌讓你最想跳舞','能唱一首歌給我聽嗎','誰是你最喜歡的歌手','你上次看的電影是什麼','你喜歡什麼類型的電影','你喜歡看什麼類型的書','你喜歡韓國流行音樂嗎','你最喜歡的油畫是什麼','你最喜歡的運動是什麼','你會聽什麼類型的音樂','你網球有得過任何獎嗎','你喜歡聽什麼類型的音樂','你是任何籃球隊的粉絲嗎','你最喜歡的網球選手是誰','你有參加任何運動隊伍嗎','我最喜歡的電影是阿凡達','你聽過星際效應這部電影嗎','你在打羽球的時候有受過傷嗎','你最喜歡的浪漫愛情片是哪部','最讓你想跳舞的音樂是哪首歌','你讀書時喜歡聽什麼類型的音樂','除了浪漫愛情喜劇，你還喜歡什麼類型的電影']
    testLoki(inputLIST, ['recreation'])
    print("")

    # color
    print("[TEST] color")
    inputLIST = ['黑色如何','你喜歡粉紅色嗎','你覺得黑色如何','彩虹有幾種顏色','鑽石是什麼顏色','你最討厭什麼顏色','你為什麼討厭藍色','你覺得黑色怎麼樣','我喜歡綠色，你呢','你喜歡怎樣的粉紅色','你對黃色有什麼看法','最溫暖的顏色是什麼','你最喜歡的顏色是什麼','我最喜歡的顏色是藍色','紅色加藍色是什麼顏色','你覺得最亮的顏色是什麼','你那邊的天空是什麼顏色的','哪個顏色比較亮，銀色或金色']
    testLoki(inputLIST, ['color'])
    print("")

    # job
    print("[TEST] job")
    inputLIST = ['你有工作嗎','我想當演員','我是做工的','我沒有兼職','你做什麼維生','我是客服人員','你的工作是什麼','你的職業是什麼','我是一個電競選手','你未來想做什麼工作','你父母的工作是什麼','我未來想當一個作家']
    testLoki(inputLIST, ['job'])
    print("")

    # security
    print("[TEST] security")
    inputLIST = ['安全嗎','我們是孤獨的嗎','這不是私人房間嗎']
    testLoki(inputLIST, ['security'])
    print("")

    # language
    print("[TEST] language")
    inputLIST = ['英文好難','我會說英文','說西班牙文','你喜歡英文嗎','你想學泰文嗎','你會幾種語言','你會說法文嗎','你知道俄文嗎','德文很難說嗎','教我一些德文','教我幾句俄語','英文很難寫嗎','swell是什麼意思','你會說什麼語言','你可以教我英文嗎','我會說中文和日文','中文的hello要怎麼說','你想學怎麼說韓文嗎','你想學習新的語言嗎','最通用的語言是什麼','說句葡萄牙文來聽聽','你可以幫我學習英文嗎','你會願意學習新語言嗎','你認為哪種語言最難學','第二通用的語言是什麼','swell在中文裡是什麼意思','swell翻成中文是什麼意思','你覺得學新語言會很難嗎','我會說日文、中文和英文']
    testLoki(inputLIST, ['language'])
    print("")

    # compliment
    print("[TEST] compliment")
    inputLIST = ['你好性感','真是聰明','那是讚美','你懂得很多','你是我的菜','我也喜歡你','我要感謝你','你是我的最愛','你真是個好人','你知道的真多','那是個好名字','你人真的很好耶','你是我的理想型','你的名字很好聽','你的笑容很好看','你看起來很漂亮','你看起來真漂亮','你笑起來很好看','你跳舞跳的真好','我喜歡你的裙子','你是個聰明的機器人','你有一雙美麗的雙眸','你為什麼如此美麗呢','你眼睛的藍色很迷人','我今天看起來怎麼樣','是什麼讓你這麼開心','你的頭髮看起來很漂亮']
    testLoki(inputLIST, ['compliment'])
    print("")

    # ability
    print("[TEST] ability")
    inputLIST = ['你擅長什麼','你會做什麼','你會唱歌嗎','你會皺眉嗎','你會跳舞嗎','你會運動嗎','你能唱歌嗎','你能睡覺嗎','你能背我嗎','貓會做什麼','你可以閉眼嗎','你會變魔術嗎','你有什麼能力','你的能力如何','你能夠倒立嗎','你會怎麼買東西','你的能力有什麼','可以對我說嗨嗎','你可以教我英文嗎','你的科技能力如何','你的閱讀能力如何','你會玩剪刀石頭布嗎','你能教我學習英文嗎','假如我給你一具身體','為什麽你什麼都不懂','你的中文閱讀能力如何','你能教我怎麼說英文嗎','你能知道我在想什麼嗎','你可以面對面跟我聊天嗎']
    testLoki(inputLIST, ['ability'])
    print("")

    # age
    print("[TEST] age")
    inputLIST = ['24','15歲','我14歲','我幾歲','12快13歲','你很年輕','我也是22歲','你今年多大','你姐姐幾歲','你的年齡是','我18歲你幾歲','你幾歲上大學','你幾歲進入高中','你覺得幾歲算老','你是姐姐還是妹妹','你高中畢業時幾歲','孩子小學畢業幾歲','人類的平均壽命是多少','女性的平均壽命是多少','你第一次一個人上學是什麼時候','你知道孩子應該在什麼年齡上學嗎']
    testLoki(inputLIST, ['age'])
    print("")

    # life
    print("[TEST] life")
    inputLIST = ['你喜歡你的人生嗎','你最近過得怎麼樣','先有雞還是先有蛋','己所不欲勿施於人','生命的意義是什麼','我想過一個快樂的生活']
    testLoki(inputLIST, ['life'])
    print("")

    # location
    print("[TEST] location")
    inputLIST = ['你在哪裡','在哪裡啊','你住在哪裡','你來自哪裡','你是哪裡人','我來自印度','我是日本人','你現在在哪裡','你現在在家嗎','我住在義大利','你的學校在哪裡','我喜歡去日本玩','日本適合居住嗎','蒙特婁怎麼樣啊','你想去哪個國家玩','那裡的環境怎麼樣','你覺得蒙特婁好玩嗎','方便問你住在哪裡嗎','蒙特婁是哪個國家的','我來自加拿大的蒙特婁','方便告訴我你是哪裡人嗎','蒙特婁是個適合居住的城市嗎']
    testLoki(inputLIST, ['location'])
    print("")

    # contact
    print("[TEST] contact")
    inputLIST = ['你喜歡社交嗎','你有用臉書嗎','你有手機號碼嗎','你的電子郵件是','你喜歡跟人說話嗎','你在臉書的名字是','你是個外向的人嗎','給我你的電子郵件','你想跟我出去晃晃嗎','你的臉書名字叫什麼','你要跟我出去走走嗎','我可以加你臉書好友嗎','你有任何社交媒體帳戶嗎']
    testLoki(inputLIST, ['contact'])
    print("")

    # personal
    print("[TEST] personal")
    inputLIST = ['你是什麼','你住在哪裡','你喜歡什麼','你是人類嗎','你是哪裡人','你有名字嗎','你的名字是','誰創造了你','你是誰創造的','你的主人是誰','你喜歡怎樣的人','你的生日是幾號','你的身高幾公尺','我要怎麼稱呼你','你喜歡吃什麼糖果','你喜歡喝什麼飲料','你是男生還是女生','你最喜歡哪個國家','你為什麽喜歡夏季','你喜歡套房還是雅房','你最喜歡的歌是哪首','你偏好在家吃還是外食']
    testLoki(inputLIST, ['personal'])
    print("")

    # apology
    print("[TEST] apology")
    inputLIST = ['抱歉','對不起','我道歉','我感到抱歉']
    testLoki(inputLIST, ['apology'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    testIntent()

    # 測試其它句子
    filterLIST = []
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST)            # output => ["今天天氣"]
    resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST, splitLIST) # output => ["今天天氣", "後天氣象"]
    resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST)      # output => ["今天天氣", "後天氣象"]