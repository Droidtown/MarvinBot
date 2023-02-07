#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for location

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

DEBUG_location = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_book":["哈利波特"],"_cars":["法拉利","藍寶堅尼","BMW","保時捷","賓士","福特","福斯","三菱","TOYOTA","賓利","瑪莎拉蒂"],"_food":["哈根達斯","培根","捲餅","生日蛋糕"],"_game":["上古捲軸","剪刀石頭布","圈圈叉叉","憤怒鳥","線上遊戲","麥塊"],"_name":["小花","麥可喬丹"],"_view":["百慕達三角洲"],"_movie":["少年pi的奇幻漂流","復仇者聯盟","星際大戰","星際效應","終局之戰","阿凡達","哈利波特"],"_place":["菜市場"],"_sport":["大隊接力","接力賽","高空彈跳"],"_career":["VT","VTuber","客服人員","實況主"],"_family":["堂兄弟姊妹","表兄弟姊妹"],"_school":["麻省理工","台灣大學","臺灣大學","師範大學"],"_activity":["室內活動","室外活動","室外運動","野餐行程","野餐計畫"],"_restaurant":["摩斯漢堡","漢堡王","響食天堂","麥當勞"],"_socialMedia":["IG","facebook","fb","instagram","臉書"],"_secretIdentity":["外星人","蝙蝠俠","超人","超級英雄"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_location:
        print("[location] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你][現在]在哪裡":
        # write your code here
        pass

    if utterance == "[你][現在]在家嗎":
        # write your code here
        pass

    if utterance == "[你]住在哪裡":
        # write your code here
        pass

    if utterance == "[你]來自哪裡":
        # write your code here
        pass

    if utterance == "[你]在哪裡":
        # write your code here
        pass

    if utterance == "[你]想去哪個國家玩":
        # write your code here
        pass

    if utterance == "[你]是哪裡人":
        # write your code here
        pass

    if utterance == "[你]的學校在哪裡":
        # write your code here
        pass

    if utterance == "[你]覺得[蒙特婁][好玩]嗎":
        # write your code here
        pass

    if utterance == "[我]住在[義大利]":
        # write your code here
        pass

    if utterance == "[我]來自[加拿大]的蒙特婁":
        # write your code here
        pass

    if utterance == "[我]來自[印度]":
        # write your code here
        pass

    if utterance == "[我]喜歡去[日本]玩":
        # write your code here
        pass

    if utterance == "[我]是[日本]人":
        # write your code here
        pass

    if utterance == "[方便]告訴[我][你]是哪裡人嗎":
        # write your code here
        pass

    if utterance == "[方便]問[你]住在哪裡嗎":
        # write your code here
        pass

    if utterance == "[日本][適合]居住嗎":
        # write your code here
        pass

    if utterance == "[蒙特婁]怎麼樣啊":
        # write your code here
        pass

    if utterance == "[蒙特婁]是[個][適合]居住的[城市]嗎":
        # write your code here
        pass

    if utterance == "[蒙特婁]是哪個國家的":
        # write your code here
        pass

    if utterance == "在哪裡啊":
        # write your code here
        pass

    if utterance == "那裡的環境怎麼樣":
        # write your code here
        pass

    return resultDICT