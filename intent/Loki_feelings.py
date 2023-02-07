#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for feelings

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

DEBUG_feelings = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_book":["哈利波特"],"_cars":["法拉利","藍寶堅尼","BMW","保時捷","賓士","福特","福斯","三菱","TOYOTA","賓利","瑪莎拉蒂"],"_food":["哈根達斯","培根","捲餅","生日蛋糕"],"_game":["上古捲軸","剪刀石頭布","圈圈叉叉","憤怒鳥","線上遊戲","麥塊"],"_name":["小花","麥可喬丹"],"_view":["百慕達三角洲"],"_movie":["少年pi的奇幻漂流","復仇者聯盟","星際大戰","星際效應","終局之戰","阿凡達","哈利波特"],"_place":["菜市場"],"_sport":["大隊接力","接力賽","高空彈跳"],"_career":["VT","VTuber","客服人員","實況主"],"_family":["堂兄弟姊妹","表兄弟姊妹"],"_school":["麻省理工","台灣大學","臺灣大學","師範大學"],"_activity":["室內活動","室外活動","室外運動","野餐行程","野餐計畫"],"_restaurant":["摩斯漢堡","漢堡王","響食天堂","麥當勞"],"_socialMedia":["IG","facebook","fb","instagram","臉書"],"_secretIdentity":["外星人","蝙蝠俠","超人","超級英雄"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_feelings:
        print("[feelings] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你][剛剛]是在羞辱[我]嗎":
        # write your code here
        pass

    if utterance == "[你][最近]過得好嗎":
        # write your code here
        pass

    if utterance == "[你][會]笑嗎":
        # write your code here
        pass

    if utterance == "[你]傷害到[我]了":
        # write your code here
        pass

    if utterance == "[你]愛[你]的家人嗎":
        # write your code here
        pass

    if utterance == "[你]相信愛情嗎":
        # write your code here
        pass

    if utterance == "[你]還好嗎":
        # write your code here
        pass

    if utterance == "[我][今天]過得[很糟]":
        # write your code here
        pass

    if utterance == "[我][今天]過得[糟透]了":
        # write your code here
        pass

    if utterance == "[我][很]失望":
        # write your code here
        pass

    if utterance == "[我][很好]":
        # write your code here
        pass

    if utterance == "[我][沒事]":
        # write your code here
        pass

    if utterance == "[我]不喜歡[你]":
        # write your code here
        pass

    if utterance == "[我]不喜歡[你][剛剛]對[我]做的事":
        # write your code here
        pass

    if utterance == "[我]不喜歡[這句]話":
        # write your code here
        pass

    if utterance == "[我]不想要當[你]的朋友":
        # write your code here
        pass

    if utterance == "[我]對[你][太]失望了":
        # write your code here
        pass

    if utterance == "[我]想[你]了":
        # write your code here
        pass

    if utterance == "[我]愛[你]":
        # write your code here
        pass

    if utterance == "[我]感到[很]傷心":
        # write your code here
        pass

    if utterance == "[我]覺得[很難過]":
        # write your code here
        pass

    if utterance == "[我]討厭[你]":
        # write your code here
        pass

    if utterance == "[我]討厭[你][這樣]對[我]":
        # write your code here
        pass

    if utterance == "[我]需要有人跟[我]說說話":
        # write your code here
        pass

    if utterance == "[酷]喔":
        # write your code here
        pass

    if utterance == "不要讓[我]失望":
        # write your code here
        pass

    if utterance == "人們[總是]讓[我]頭痛":
        # write your code here
        pass

    if utterance == "別讓[我]難過":
        # write your code here
        pass

    if utterance == "告訴[我][你]愛[我]":
        # write your code here
        pass

    if utterance == "太酷了吧":
        # write your code here
        pass

    if utterance == "好喔":
        # write your code here
        pass

    if utterance == "怎樣[才]算愛[一個]人":
        # write your code here
        pass

    if utterance == "愛[你]":
        # write your code here
        pass

    if utterance == "笑死":
        # write your code here
        pass

    if utterance == "說[你]愛[我]":
        # write your code here
        pass

    return resultDICT