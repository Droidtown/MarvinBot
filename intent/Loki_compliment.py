#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for compliment

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

DEBUG_compliment = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_book":["哈利波特"],"_cars":["法拉利","藍寶堅尼","BMW","保時捷","賓士","福特","福斯","三菱","TOYOTA","賓利","瑪莎拉蒂"],"_food":["哈根達斯","培根","捲餅","生日蛋糕"],"_game":["上古捲軸","剪刀石頭布","圈圈叉叉","憤怒鳥","線上遊戲","麥塊"],"_name":["小花","麥可喬丹"],"_view":["百慕達三角洲"],"_movie":["少年pi的奇幻漂流","復仇者聯盟","星際大戰","星際效應","終局之戰","阿凡達","哈利波特"],"_place":["菜市場"],"_sport":["大隊接力","接力賽","高空彈跳"],"_career":["VT","VTuber","客服人員","實況主"],"_family":["堂兄弟姊妹","表兄弟姊妹"],"_school":["麻省理工","台灣大學","臺灣大學","師範大學"],"_activity":["室內活動","室外活動","室外運動","野餐行程","野餐計畫"],"_restaurant":["摩斯漢堡","漢堡王","響食天堂","麥當勞"],"_socialMedia":["IG","facebook","fb","instagram","臉書"],"_secretIdentity":["外星人","蝙蝠俠","超人","超級英雄"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_compliment:
        print("[compliment] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你][好性感]":
        # write your code here
        pass

    if utterance == "[你][真]是[個]好人":
        # write your code here
        pass

    if utterance == "[你][眼睛]的[藍色][很迷人]":
        # write your code here
        pass

    if utterance == "[你]人[真]的很好耶":
        # write your code here
        pass

    if utterance == "[你]懂得很多":
        # write your code here
        pass

    if utterance == "[你]是[個][聰明]的機器人":
        # write your code here
        pass

    if utterance == "[你]是[我]的最愛":
        # write your code here
        pass

    if utterance == "[你]是[我]的理想型":
        # write your code here
        pass

    if utterance == "[你]是[我]的菜":
        # write your code here
        pass

    if utterance == "[你]有[一雙][美麗]的[雙眸]":
        # write your code here
        pass

    if utterance == "[你]為什麼[如此][美麗]呢":
        # write your code here
        pass

    if utterance == "[你]的[笑容][很好看]":
        # write your code here
        pass

    if utterance == "[你]的[頭髮]看起來[很漂亮]":
        # write your code here
        pass

    if utterance == "[你]的名字很好聽":
        # write your code here
        pass

    if utterance == "[你]看起來[很漂亮]":
        # write your code here
        pass

    if utterance == "[你]看起來[真][漂亮]":
        # write your code here
        pass

    if utterance == "[你]知道的[真]多":
        # write your code here
        pass

    if utterance == "[你]笑起來很好看":
        # write your code here
        pass

    if utterance == "[你]跳舞跳的[真好]":
        # write your code here
        pass

    if utterance == "[我][也]喜歡[你]":
        # write your code here
        pass

    if utterance == "[我][今天]看起來怎麼樣":
        # write your code here
        pass

    if utterance == "[我]喜歡[你]的裙子":
        # write your code here
        pass

    if utterance == "[我]要感謝[你]":
        # write your code here
        pass

    if utterance == "[真]是[聰明]":
        # write your code here
        pass

    if utterance == "是什麼讓[你]這麼開心":
        # write your code here
        pass

    if utterance == "那是[個]好名字":
        # write your code here
        pass

    if utterance == "那是讚美":
        # write your code here
        pass

    return resultDICT