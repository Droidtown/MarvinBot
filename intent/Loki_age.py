#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for age

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

DEBUG_age = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_book":["哈利波特"],"_cars":["法拉利","藍寶堅尼","BMW","保時捷","賓士","福特","福斯","三菱","TOYOTA","賓利","瑪莎拉蒂"],"_food":["哈根達斯","培根","捲餅","生日蛋糕"],"_game":["上古捲軸","剪刀石頭布","圈圈叉叉","憤怒鳥","線上遊戲","麥塊"],"_name":["小花","麥可喬丹"],"_view":["百慕達三角洲"],"_movie":["少年pi的奇幻漂流","復仇者聯盟","星際大戰","星際效應","終局之戰","阿凡達","哈利波特"],"_place":["菜市場"],"_sport":["大隊接力","接力賽","高空彈跳"],"_career":["VT","VTuber","客服人員","實況主"],"_family":["堂兄弟姊妹","表兄弟姊妹"],"_school":["麻省理工","台灣大學","臺灣大學","師範大學"],"_activity":["室內活動","室外活動","室外運動","野餐行程","野餐計畫"],"_restaurant":["摩斯漢堡","漢堡王","響食天堂","麥當勞"],"_socialMedia":["IG","facebook","fb","instagram","臉書"],"_secretIdentity":["外星人","蝙蝠俠","超人","超級英雄"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_age:
        print("[age] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[12]快[13]歲":
        # write your code here
        pass

    if utterance == "[15]歲":
        # write your code here
        pass

    if utterance == "[24]":
        # write your code here
        pass

    if utterance == "[人類]的平均壽命是多少":
        # write your code here
        pass

    if utterance == "[你][今年]多[大]":
        # write your code here
        pass

    if utterance == "[你][第一次][一個]人上學是什麼[時候]":
        # write your code here
        pass

    if utterance == "[你][高中]畢業時幾歲":
        # write your code here
        pass

    if utterance == "[你]幾歲[上][大學]":
        # write your code here
        pass

    if utterance == "[你]幾歲進入[高中]":
        # write your code here
        pass

    if utterance == "[你]很年輕":
        # write your code here
        pass

    if utterance == "[你]是[姐姐]還是[妹妹]":
        # write your code here
        pass

    if utterance == "[你]的年齡是":
        # write your code here
        pass

    if utterance == "[你]知道孩子[應該]在什麼年齡上學嗎":
        # write your code here
        pass

    if utterance == "[你]覺得幾歲算老":
        # write your code here
        pass

    if utterance == "[我][14]歲":
        # write your code here
        pass

    if utterance == "[我][18]歲[你]幾歲":
        # write your code here
        pass

    if utterance == "[我][也]是[22]歲":
        # write your code here
        pass

    if utterance == "[我]幾歲":
        # write your code here
        pass

    if utterance == "你[姐姐]幾歲":
        # write your code here
        pass

    if utterance == "孩子[小學]畢業幾歲":
        # write your code here
        pass

    return resultDICT