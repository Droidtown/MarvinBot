#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for disagree

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

DEBUG_disagree = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_book":["哈利波特"],"_cars":["法拉利","藍寶堅尼","BMW","保時捷","賓士","福特","福斯","三菱","TOYOTA","賓利","瑪莎拉蒂"],"_food":["哈根達斯","培根","捲餅","生日蛋糕"],"_game":["上古捲軸","剪刀石頭布","圈圈叉叉","憤怒鳥","線上遊戲","麥塊"],"_name":["小花","麥可喬丹"],"_view":["百慕達三角洲"],"_movie":["少年pi的奇幻漂流","復仇者聯盟","星際大戰","星際效應","終局之戰","阿凡達","哈利波特"],"_place":["菜市場"],"_sport":["大隊接力","接力賽","高空彈跳"],"_career":["VT","VTuber","客服人員","實況主"],"_family":["堂兄弟姊妹","表兄弟姊妹"],"_school":["麻省理工","台灣大學","臺灣大學","師範大學"],"_activity":["室內活動","室外活動","室外運動","野餐行程","野餐計畫"],"_restaurant":["摩斯漢堡","漢堡王","響食天堂","麥當勞"],"_socialMedia":["IG","facebook","fb","instagram","臉書"],"_secretIdentity":["外星人","蝙蝠俠","超人","超級英雄"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_disagree:
        print("[disagree] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[我]不想":
        # write your code here
        pass

    if utterance == "[我]不確定":
        # write your code here
        pass

    if utterance == "[沒事]":
        # write your code here
        pass

    if utterance == "不[重要]":
        # write your code here
        pass

    if utterance == "沒[什麼]":
        # write your code here
        pass

    if utterance == "與[你][無關]":
        # write your code here
        pass

    if utterance == "跟[你]沒有關係":
        # write your code here
        pass

    if utterance == "那不是[真]的":
        # write your code here
        pass

    return resultDICT