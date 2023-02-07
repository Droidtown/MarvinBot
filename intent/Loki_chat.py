#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for chat

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os

DEBUG_chat = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_book":["哈利波特"],"_cars":["法拉利","藍寶堅尼","BMW","保時捷","賓士","福特","福斯","三菱","TOYOTA","賓利","瑪莎拉蒂"],"_food":["哈根達斯","培根","捲餅","生日蛋糕"],"_game":["上古捲軸","剪刀石頭布","圈圈叉叉","憤怒鳥","線上遊戲","麥塊"],"_name":["小花","麥可喬丹"],"_view":["百慕達三角洲"],"_movie":["少年pi的奇幻漂流","復仇者聯盟","星際大戰","星際效應","終局之戰","阿凡達","哈利波特"],"_place":["菜市場"],"_sport":["大隊接力","接力賽","高空彈跳"],"_career":["VT","VTuber","客服人員","實況主"],"_family":["堂兄弟姊妹","表兄弟姊妹"],"_school":["麻省理工","台灣大學","臺灣大學","師範大學"],"_activity":["室內活動","室外活動","室外運動","野餐行程","野餐計畫"],"_restaurant":["摩斯漢堡","漢堡王","響食天堂","麥當勞"],"_socialMedia":["IG","facebook","fb","instagram","臉書"],"_secretIdentity":["外星人","蝙蝠俠","超人","超級英雄"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_chat:
        print("[chat] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你][今天]做了什麼":
        # write your code here
        pass

    if utterance == "[你][可以]做什麼事":
        # write your code here
        pass

    if utterance == "[你][可以]幫[我]做什麼":
        # write your code here
        pass

    if utterance == "[你][可以]把[它]脫掉嗎":
        # write your code here
        pass

    if utterance == "[你][最]喜歡的[東西]是什麼":
        # write your code here
        pass

    if utterance == "[你][會]做什麼":
        # write your code here
        pass

    if utterance == "[你][會]在網路[上]聊天嗎":
        # write your code here
        pass

    if utterance == "[你][會]微笑嗎":
        # write your code here
        pass

    if utterance == "[你][會]抽煙嗎":
        # write your code here
        pass

    if utterance == "[你][會]查google嗎":
        # write your code here
        pass

    if utterance == "[你][會]講笑話嗎":
        # write your code here
        pass

    if utterance == "[你][根本]不懂[我]":
        # write your code here
        pass

    if utterance == "[你]不是人類":
        # write your code here
        pass

    if utterance == "[你]不覺得[原著][永遠]比[電影][好看]嗎":
        # write your code here
        pass

    if utterance == "[你]住在哪裡":
        # write your code here
        pass

    if utterance == "[你]假日的[時候]喜歡待在家還是出去旅遊":
        # write your code here
        pass

    if utterance == "[你]喜歡[室內活動]或[室外活動]":
        # write your code here
        pass

    if utterance == "[你]喜歡[我]的哪[一點]":
        # write your code here
        pass

    if utterance == "[你]喜歡做什麼":
        # write your code here
        pass

    if utterance == "[你]喜歡被擁抱嗎":
        # write your code here
        pass

    if utterance == "[你]在做什麼":
        # write your code here
        pass

    if utterance == "[你]對[政治]有什麼看法":
        # write your code here
        pass

    if utterance == "[你]對[政治]的看法是":
        # write your code here
        pass

    if utterance == "[你]從哪裡來的":
        # write your code here
        pass

    if utterance == "[你]想來我家玩嗎":
        # write your code here
        pass

    if utterance == "[你]想要出去走走嗎":
        # write your code here
        pass

    if utterance == "[你]想要聊什麼":
        # write your code here
        pass

    if utterance == "[你]感覺如何":
        # write your code here
        pass

    if utterance == "[你]是[一個]機器人嗎":
        # write your code here
        pass

    if utterance == "[你]是[真]的嗎":
        # write your code here
        pass

    if utterance == "[你]是不[是]在嘲笑[我]":
        # write your code here
        pass

    if utterance == "[你]是人類嗎":
        # write your code here
        pass

    if utterance == "[你]是什麼":
        # write your code here
        pass

    if utterance == "[你]是哪裡人":
        # write your code here
        pass

    if utterance == "[你]是怎樣的人":
        # write your code here
        pass

    if utterance == "[你]是男生還是女生":
        # write your code here
        pass

    if utterance == "[你]是誰創造的":
        # write your code here
        pass

    if utterance == "[你]會不[會]忘記[我]":
        # write your code here
        pass

    if utterance == "[你]有[任何][偏好]的[衛生紙]品牌嗎":
        # write your code here
        pass

    if utterance == "[你]有[任何]夢想嗎":
        # write your code here
        pass

    if utterance == "[你]有[名字]嗎":
        # write your code here
        pass

    if utterance == "[你]有交往對象嗎":
        # write your code here
        pass

    if utterance == "[你]有什麼興趣":
        # write your code here
        pass

    if utterance == "[你]為什麽不喜歡[遊樂園]":
        # write your code here
        pass

    if utterance == "[你]的[名字]是":
        # write your code here
        pass

    if utterance == "[你]的[生日]是幾號":
        # write your code here
        pass

    if utterance == "[你]的主人是誰":
        # write your code here
        pass

    if utterance == "[你]的名字[很好聽]":
        # write your code here
        pass

    if utterance == "[你]的底線在哪裡":
        # write your code here
        pass

    if utterance == "[你]的身高[幾公尺]":
        # write your code here
        pass

    if utterance == "[你]相信神嗎":
        # write your code here
        pass

    if utterance == "[你]看得到[我]嗎":
        # write your code here
        pass

    if utterance == "[你]知道[它]的[名字]嗎":
        # write your code here
        pass

    if utterance == "[你]確定嗎":
        # write your code here
        pass

    if utterance == "[你]還在嗎":
        # write your code here
        pass

    if utterance == "[你]還想聊什麼":
        # write your code here
        pass

    if utterance == "[我][可以]問[你]問題嗎":
        # write your code here
        pass

    if utterance == "[我][可以]揍[你]嗎":
        # write your code here
        pass

    if utterance == "[我][可以]摸[你]的[腹肌]嗎":
        # write your code here
        pass

    if utterance == "[我][可以]碰[你]的[頭髮]嗎":
        # write your code here
        pass

    if utterance == "[我][更]喜歡[你]":
        # write your code here
        pass

    if utterance == "[我]了解了":
        # write your code here
        pass

    if utterance == "[我]其實是偽裝的[外星人]":
        # write your code here
        pass

    if utterance == "[我]喜歡吃[冰淇淋]":
        # write your code here
        pass

    if utterance == "[我]喜歡喝[檸檬汁]":
        # write your code here
        pass

    if utterance == "[我]想問[你][一些]問題":
        # write your code here
        pass

    if utterance == "[我]是[一個][有趣]的人":
        # write your code here
        pass

    if utterance == "[我]是[一個]聊天機器人":
        # write your code here
        pass

    if utterance == "[我]是[人類]":
        # write your code here
        pass

    if utterance == "[我]有很多想法":
        # write your code here
        pass

    if utterance == "[我]正在接受訓練成為[一個]專業客服人員":
        # write your code here
        pass

    if utterance == "[我]沒有祕密":
        # write your code here
        pass

    if utterance == "[我]要告訴[你][一個]祕密":
        # write your code here
        pass

    if utterance == "[我]要怎麼稱呼[你]":
        # write your code here
        pass

    if utterance == "[我]覺得[我][更]困惑了":
        # write your code here
        pass

    if utterance == "[我]討厭[加拿大]人":
        # write your code here
        pass

    if utterance == "[我們][可以]聊聊嗎":
        # write your code here
        pass

    if utterance == "[我們][可以]走得更遠嗎":
        # write your code here
        pass

    if utterance == "[新聞]在說什麼":
        # write your code here
        pass

    if utterance == "[現在]就告訴[我]":
        # write your code here
        pass

    if utterance == "[真]是[個]好名字":
        # write your code here
        pass

    if utterance == "[真巧]":
        # write your code here
        pass

    if utterance == "告訴[我][你][最]喜歡的事情":
        # write your code here
        pass

    if utterance == "告訴[我]更多有關[你]的事情":
        # write your code here
        pass

    if utterance == "問[我][一個]問題":
        # write your code here
        pass

    if utterance == "在嗎":
        # write your code here
        pass

    if utterance == "巧了":
        # write your code here
        pass

    if utterance == "很高興聽到[你]這麼說":
        # write your code here
        pass

    if utterance == "有問題嗎":
        # write your code here
        pass

    if utterance == "為什麼大家[都]叫[你]小花":
        # write your code here
        pass

    if utterance == "為什麽[這麼]問":
        # write your code here
        pass

    if utterance == "猜猜[今天]發生了什麼事":
        # write your code here
        pass

    if utterance == "猜猜[我][今天]做了什麼":
        # write your code here
        pass

    if utterance == "說[個]笑話來聽聽":
        # write your code here
        pass

    if utterance == "誰創造[你]":
        # write your code here
        pass

    if utterance == "誰告訴[你]的":
        # write your code here
        pass

    if utterance == "跟[我]說[點]話":
        # write your code here
        pass

    if utterance == "還有其他的嗎":
        # write your code here
        pass

    return resultDICT