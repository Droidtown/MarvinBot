#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for experience

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

DEBUG_experience = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_book":["哈利波特"],"_cars":["法拉利","藍寶堅尼","BMW","保時捷","賓士","福特","福斯","三菱","TOYOTA","賓利","瑪莎拉蒂"],"_food":["哈根達斯","培根","捲餅","生日蛋糕"],"_game":["上古捲軸","剪刀石頭布","圈圈叉叉","憤怒鳥","線上遊戲","麥塊"],"_name":["小花","麥可喬丹"],"_view":["百慕達三角洲"],"_movie":["少年pi的奇幻漂流","復仇者聯盟","星際大戰","星際效應","終局之戰","阿凡達","哈利波特"],"_place":["菜市場"],"_sport":["大隊接力","接力賽","高空彈跳"],"_career":["VT","VTuber","客服人員","實況主"],"_family":["堂兄弟姊妹","表兄弟姊妹"],"_school":["麻省理工","台灣大學","臺灣大學","師範大學"],"_activity":["室內活動","室外活動","室外運動","野餐行程","野餐計畫"],"_restaurant":["摩斯漢堡","漢堡王","響食天堂","麥當勞"],"_socialMedia":["IG","facebook","fb","instagram","臉書"],"_secretIdentity":["外星人","蝙蝠俠","超人","超級英雄"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_experience:
        print("[experience] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你][上][過多][少課]":
        # write your code here
        pass

    if utterance == "[你][最]喜歡的記憶是什麼":
        # write your code here
        pass

    if utterance == "[你][會][每天]去[健身房]嗎":
        # write your code here
        pass

    if utterance == "[你][通常][都]怎麼旅遊":
        # write your code here
        pass

    if utterance == "[你]出去玩是坐船還是坐[飛機]":
        # write your code here
        pass

    if utterance == "[你]印象最深刻的記憶是什麼":
        # write your code here
        pass

    if utterance == "[你]去[台灣]旅遊過嗎":
        # write your code here
        pass

    if utterance == "[你]去過[葡萄牙]嗎":
        # write your code here
        pass

    if utterance == "[你]去過幾[個][國家]":
        # write your code here
        pass

    if utterance == "[你]參加過[球賽]嗎":
        # write your code here
        pass

    if utterance == "[你]吃過[哈根達斯]嗎":
        # write your code here
        pass

    if utterance == "[你]坐過[船]嗎":
        # write your code here
        pass

    if utterance == "[你]多常去[一次][健身房]":
        # write your code here
        pass

    if utterance == "[你]想去[澳洲]玩玩看嗎":
        # write your code here
        pass

    if utterance == "[你]打過[球賽]嗎":
        # write your code here
        pass

    if utterance == "[你]搭過[飛機]嗎":
        # write your code here
        pass

    if utterance == "[你]曾經在[任何]公司工作過嗎":
        # write your code here
        pass

    if utterance == "[你]曾經接吻過嗎":
        # write your code here
        pass

    if utterance == "[你]曾經騎過[馬]嗎":
        # write your code here
        pass

    if utterance == "[你]有去過[百慕達三角洲]嗎":
        # write your code here
        pass

    if utterance == "[你]有參加過[大隊接力]嗎":
        # write your code here
        pass

    if utterance == "[你]有在[美國]住過嗎":
        # write your code here
        pass

    if utterance == "[你]有浮潛過嗎":
        # write your code here
        pass

    if utterance == "[你]有玩過[高空彈跳]嗎":
        # write your code here
        pass

    if utterance == "[你]看過[中醫]嗎":
        # write your code here
        pass

    if utterance == "[你]跑過接力嗎":
        # write your code here
        pass

    if utterance == "[你]跟[女生]接吻過嗎":
        # write your code here
        pass

    if utterance == "[我][三天][前]收到[一個][完美]的[禮物]":
        # write your code here
        pass

    if utterance == "[我][上週]去[義大利]旅行":
        # write your code here
        pass

    if utterance == "[我][上週]去[義大利]玩":
        # write your code here
        pass

    if utterance == "[我][剛剛]和[我]的[家人]去看[電影]":
        # write your code here
        pass

    if utterance == "[我][去年]換了[兩個]工作":
        # write your code here
        pass

    if utterance == "[我][四年][前]養過[一條][狗]":
        # write your code here
        pass

    if utterance == "[我][常常]去吃[泰式料理]":
        # write your code here
        pass

    if utterance == "[我][昨天]吃了[一個][超大]的[生日蛋糕]":
        # write your code here
        pass

    if utterance == "[我]和[家人][常常]去吃[印尼菜]":
        # write your code here
        pass

    if utterance == "[我]想去[日本]玩":
        # write your code here
        pass

    if utterance == "[我]想帶[你]去[海邊]玩":
        # write your code here
        pass

    if utterance == "[我]曾經去[非洲]玩過":
        # write your code here
        pass

    if utterance == "[我]養過[一隻][貓]":
        # write your code here
        pass

    return resultDICT