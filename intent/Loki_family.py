#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for family

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

DEBUG_family = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_book":["哈利波特"],"_cars":["法拉利","藍寶堅尼","BMW","保時捷","賓士","福特","福斯","三菱","TOYOTA","賓利","瑪莎拉蒂"],"_food":["哈根達斯","培根","捲餅","生日蛋糕"],"_game":["上古捲軸","剪刀石頭布","圈圈叉叉","憤怒鳥","線上遊戲","麥塊"],"_name":["小花","麥可喬丹"],"_view":["百慕達三角洲"],"_movie":["少年pi的奇幻漂流","復仇者聯盟","星際大戰","星際效應","終局之戰","阿凡達","哈利波特"],"_place":["菜市場"],"_sport":["大隊接力","接力賽","高空彈跳"],"_career":["VT","VTuber","客服人員","實況主"],"_family":["堂兄弟姊妹","表兄弟姊妹"],"_school":["麻省理工","台灣大學","臺灣大學","師範大學"],"_activity":["室內活動","室外活動","室外運動","野餐行程","野餐計畫"],"_restaurant":["摩斯漢堡","漢堡王","響食天堂","麥當勞"],"_socialMedia":["IG","facebook","fb","instagram","臉書"],"_secretIdentity":["外星人","蝙蝠俠","超人","超級英雄"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_family:
        print("[family] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你][會]和家人分享事情嗎":
        # write your code here
        pass

    if utterance == "[你]和家人住嗎":
        # write your code here
        pass

    if utterance == "[你]和家人關係好嗎":
        # write your code here
        pass

    if utterance == "[你]多[久]回去見[爸媽][一次]":
        # write your code here
        pass

    if utterance == "[你]多[常]和[姐姐]說[一次]話":
        # write your code here
        pass

    if utterance == "[你]多[常]花時間陪伴[你]的[爸媽]":
        # write your code here
        pass

    if utterance == "[你]家人[通常][都]在做什麼":
        # write your code here
        pass

    if utterance == "[你]怎麼稱呼[你]的[爸媽]":
        # write your code here
        pass

    if utterance == "[你]是最大的還是最小的":
        # write your code here
        pass

    if utterance == "[你]最常說話的家人是誰":
        # write your code here
        pass

    if utterance == "[你]有[任何][兄弟][姊妹]嗎":
        # write your code here
        pass

    if utterance == "[你]有小孩嗎":
        # write your code here
        pass

    if utterance == "[你]有幾[個][表兄弟姊妹]":
        # write your code here
        pass

    if utterance == "[你]有幾[個][表弟]":
        # write your code here
        pass

    if utterance == "[你]有幾[個][阿姨]和[舅舅]":
        # write your code here
        pass

    if utterance == "[你]的[爸媽]還在工作嗎":
        # write your code here
        pass

    if utterance == "[我]有[一個][弟弟]":
        # write your code here
        pass

    if utterance == "[我]每[兩週][會]見到[一次]家人":
        # write your code here
        pass

    if utterance == "你[姊姊]叫什麼名字":
        # write your code here
        pass

    if utterance == "你[姐姐]是學生嗎":
        # write your code here
        pass

    if utterance == "你[爸媽][最近]好嗎":
        # write your code here
        pass

    if utterance == "你家假日[都]在做什麼":
        # write your code here
        pass

    if utterance == "你家有幾[個]人":
        # write your code here
        pass

    if utterance == "我家有[五個]人":
        # write your code here
        pass

    return resultDICT