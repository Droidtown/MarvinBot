#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for appearance

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

DEBUG_appearance = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_book":["哈利波特"],"_cars":["法拉利","藍寶堅尼","BMW","保時捷","賓士","福特","福斯","三菱","TOYOTA","賓利","瑪莎拉蒂"],"_food":["哈根達斯","培根","捲餅","生日蛋糕"],"_game":["上古捲軸","剪刀石頭布","圈圈叉叉","憤怒鳥","線上遊戲","麥塊"],"_name":["小花","麥可喬丹"],"_view":["百慕達三角洲"],"_movie":["少年pi的奇幻漂流","復仇者聯盟","星際大戰","星際效應","終局之戰","阿凡達","哈利波特"],"_place":["菜市場"],"_sport":["大隊接力","接力賽","高空彈跳"],"_career":["VT","VTuber","客服人員","實況主"],"_family":["堂兄弟姊妹","表兄弟姊妹"],"_school":["麻省理工","台灣大學","臺灣大學","師範大學"],"_activity":["室內活動","室外活動","室外運動","野餐行程","野餐計畫"],"_restaurant":["摩斯漢堡","漢堡王","響食天堂","麥當勞"],"_socialMedia":["IG","facebook","fb","instagram","臉書"],"_secretIdentity":["外星人","蝙蝠俠","超人","超級英雄"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_appearance:
        print("[appearance] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[180公分]":
        # write your code here
        pass

    if utterance == "[你][今天]的打扮[很棒]":
        # write your code here
        pass

    if utterance == "[你][今天]看起來[很漂亮]":
        # write your code here
        pass

    if utterance == "[你][今天]穿什麼":
        # write your code here
        pass

    if utterance == "[你][冬天]的[時候][會]戴[圍巾]嗎":
        # write your code here
        pass

    if utterance == "[你][好醜]":
        # write your code here
        pass

    if utterance == "[你][很瘦]嗎":
        # write your code here
        pass

    if utterance == "[你][會]怎麼形容[我]":
        # write your code here
        pass

    if utterance == "[你][會]怎麼形容你[自己]":
        # write your code here
        pass

    if utterance == "[你][會]戴[圍巾]嗎":
        # write your code here
        pass

    if utterance == "[你][會]穿[裙子]嗎":
        # write your code here
        pass

    if utterance == "[你][會]穿什麼去上班":
        # write your code here
        pass

    if utterance == "[你][身高]多少":
        # write your code here
        pass

    if utterance == "[你]喜歡[綠色]的[眼睛]嗎":
        # write your code here
        pass

    if utterance == "[你]喜歡怎樣的[衣服]":
        # write your code here
        pass

    if utterance == "[你]喜歡怎麼穿":
        # write your code here
        pass

    if utterance == "[你]很適合[紅色]":
        # write your code here
        pass

    if utterance == "[你]有[大鼻子]嗎":
        # write your code here
        pass

    if utterance == "[你]有[把]頭髮染成[棕色]嗎":
        # write your code here
        pass

    if utterance == "[你]有多高":
        # write your code here
        pass

    if utterance == "[你]有幾[件][衣服]":
        # write your code here
        pass

    if utterance == "[你]有染[頭髮]嗎":
        # write your code here
        pass

    if utterance == "[你]的[屁股][性感]嗎":
        # write your code here
        pass

    if utterance == "[你]的[眼睛]是什麼顏色的":
        # write your code here
        pass

    if utterance == "[你]的[衣服][大多]是什麼[顏色]的":
        # write your code here
        pass

    if utterance == "[你]的[鞋子尺寸]多[大]":
        # write your code here
        pass

    if utterance == "[你]的[頭髮]為什麼是[黑色]的":
        # write your code here
        pass

    if utterance == "[你]覺得[我][漂亮]嗎":
        # write your code here
        pass

    if utterance == "[你]長的[好醜]":
        # write your code here
        pass

    if utterance == "[你]長的怎麼樣":
        # write your code here
        pass

    if utterance == "[女人]怎樣[才]算[漂亮]":
        # write your code here
        pass

    if utterance == "[我][也]喜歡制服":
        # write your code here
        pass

    if utterance == "[我][該]減肥了":
        # write your code here
        pass

    if utterance == "[我][該]穿什麼去[學校]":
        # write your code here
        pass

    if utterance == "[我]喜歡[你]的[小腿]":
        # write your code here
        pass

    if utterance == "[我]想要有[大鼻子]":
        # write your code here
        pass

    if utterance == "[我]的[頭髮]是[金色]的":
        # write your code here
        pass

    if utterance == "[我]看起來如何":
        # write your code here
        pass

    return resultDICT