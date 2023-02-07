#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for greeting

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

DEBUG_greeting = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_book":["哈利波特"],"_cars":["法拉利","藍寶堅尼","BMW","保時捷","賓士","福特","福斯","三菱","TOYOTA","賓利","瑪莎拉蒂"],"_food":["哈根達斯","培根","捲餅","生日蛋糕"],"_game":["上古捲軸","剪刀石頭布","圈圈叉叉","憤怒鳥","線上遊戲","麥塊"],"_name":["小花","麥可喬丹"],"_view":["百慕達三角洲"],"_movie":["少年pi的奇幻漂流","復仇者聯盟","星際大戰","星際效應","終局之戰","阿凡達","哈利波特"],"_place":["菜市場"],"_sport":["大隊接力","接力賽","高空彈跳"],"_career":["VT","VTuber","客服人員","實況主"],"_family":["堂兄弟姊妹","表兄弟姊妹"],"_school":["麻省理工","台灣大學","臺灣大學","師範大學"],"_activity":["室內活動","室外活動","室外運動","野餐行程","野餐計畫"],"_restaurant":["摩斯漢堡","漢堡王","響食天堂","麥當勞"],"_socialMedia":["IG","facebook","fb","instagram","臉書"],"_secretIdentity":["外星人","蝙蝠俠","超人","超級英雄"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_greeting:
        print("[greeting] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你][今天]怎麼樣":
        # write your code here
        pass

    if utterance == "[你][好]，[你][今天]好嗎":
        # write your code here
        pass

    if utterance == "[你]叫什麼名字":
        # write your code here
        pass

    if utterance == "[你]姓什麼":
        # write your code here
        pass

    if utterance == "[我][今天]過得很愉快":
        # write your code here
        pass

    if utterance == "[我]很好，[你]呢":
        # write your code here
        pass

    if utterance == "[我]很好，謝謝。那[你]呢":
        # write your code here
        pass

    if utterance == "[我]很高興聽到":
        # write your code here
        pass

    if utterance == "[我]明白[我]很好":
        # write your code here
        pass

    if utterance == "[我]知道[你]很好":
        # write your code here
        pass

    if utterance == "嗨，[我]叫[小花]":
        # write your code here
        pass

    if utterance == "很高興認識[你]":
        # write your code here
        pass

    return resultDICT