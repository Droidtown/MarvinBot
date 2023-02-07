#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for school

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

DEBUG_school = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_book":["哈利波特"],"_cars":["法拉利","藍寶堅尼","BMW","保時捷","賓士","福特","福斯","三菱","TOYOTA","賓利","瑪莎拉蒂"],"_food":["哈根達斯","培根","捲餅","生日蛋糕"],"_game":["上古捲軸","剪刀石頭布","圈圈叉叉","憤怒鳥","線上遊戲","麥塊"],"_name":["小花","麥可喬丹"],"_view":["百慕達三角洲"],"_movie":["少年pi的奇幻漂流","復仇者聯盟","星際大戰","星際效應","終局之戰","阿凡達","哈利波特"],"_place":["菜市場"],"_sport":["大隊接力","接力賽","高空彈跳"],"_career":["VT","VTuber","客服人員","實況主"],"_family":["堂兄弟姊妹","表兄弟姊妹"],"_school":["麻省理工","台灣大學","臺灣大學","師範大學"],"_activity":["室內活動","室外活動","室外運動","野餐行程","野餐計畫"],"_restaurant":["摩斯漢堡","漢堡王","響食天堂","麥當勞"],"_socialMedia":["IG","facebook","fb","instagram","臉書"],"_secretIdentity":["外星人","蝙蝠俠","超人","超級英雄"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_school:
        print("[school] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你][比較]喜歡[數學]還是[國文]課":
        # write your code here
        pass

    if utterance == "[你]主修什麼":
        # write your code here
        pass

    if utterance == "[你]修過什麼[體育課]":
        # write your code here
        pass

    if utterance == "[你]喜歡[數學課]嗎":
        # write your code here
        pass

    if utterance == "[你]在哪個班級":
        # write your code here
        pass

    if utterance == "[你]多久讀[一次]書":
        # write your code here
        pass

    if utterance == "[你]是[大學生]嗎":
        # write your code here
        pass

    if utterance == "[你]會不[會]擔心[你]的科系沒辦法賺錢":
        # write your code here
        pass

    if utterance == "[你]有[任何]作業嗎":
        # write your code here
        pass

    if utterance == "[你]的主修是什麼":
        # write your code here
        pass

    if utterance == "[你]的學校生活怎麼樣":
        # write your code here
        pass

    if utterance == "[你]知道怎樣[能][快速]的學好[一種][語言]嗎":
        # write your code here
        pass

    if utterance == "[你]要寫論文嗎":
        # write your code here
        pass

    if utterance == "[你]覺得[大學][好玩]嗎":
        # write your code here
        pass

    if utterance == "[你]覺得上學[好玩]嗎":
        # write your code here
        pass

    if utterance == "[你]覺得讀[大學]是[必要]的嗎":
        # write your code here
        pass

    if utterance == "[你]讀哪個科系":
        # write your code here
        pass

    if utterance == "[你]讀哪所[大學]":
        # write your code here
        pass

    if utterance == "[我]在[台灣大學]就讀[歷史系]":
        # write your code here
        pass

    if utterance == "[我]在[美國]讀[麻省理工]":
        # write your code here
        pass

    if utterance == "[我]在台灣大學主修經濟":
        # write your code here
        pass

    if utterance == "[我]是[一個]大學生":
        # write your code here
        pass

    if utterance == "[我]讀[經濟系]":
        # write your code here
        pass

    if utterance == "[這個]科目[好玩]嗎":
        # write your code here
        pass

    return resultDICT