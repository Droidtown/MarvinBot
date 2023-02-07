#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for recreation

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

DEBUG_recreation = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_book":["哈利波特"],"_cars":["法拉利","藍寶堅尼","BMW","保時捷","賓士","福特","福斯","三菱","TOYOTA","賓利","瑪莎拉蒂"],"_food":["哈根達斯","培根","捲餅","生日蛋糕"],"_game":["上古捲軸","剪刀石頭布","圈圈叉叉","憤怒鳥","線上遊戲","麥塊"],"_name":["小花","麥可喬丹"],"_view":["百慕達三角洲"],"_movie":["少年pi的奇幻漂流","復仇者聯盟","星際大戰","星際效應","終局之戰","阿凡達","哈利波特"],"_place":["菜市場"],"_sport":["大隊接力","接力賽","高空彈跳"],"_career":["VT","VTuber","客服人員","實況主"],"_family":["堂兄弟姊妹","表兄弟姊妹"],"_school":["麻省理工","台灣大學","臺灣大學","師範大學"],"_activity":["室內活動","室外活動","室外運動","野餐行程","野餐計畫"],"_restaurant":["摩斯漢堡","漢堡王","響食天堂","麥當勞"],"_socialMedia":["IG","facebook","fb","instagram","臉書"],"_secretIdentity":["外星人","蝙蝠俠","超人","超級英雄"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_recreation:
        print("[recreation] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[你][上次]看的電影是什麼":
        # write your code here
        pass

    if utterance == "[你][最]喜歡的[油畫]是什麼":
        # write your code here
        pass

    if utterance == "[你][最]喜歡的[浪漫][愛情片]是哪部":
        # write your code here
        pass

    if utterance == "[你][最]喜歡的[網球選手]是誰":
        # write your code here
        pass

    if utterance == "[你][最]喜歡的運動是什麼":
        # write your code here
        pass

    if utterance == "[你][會][任何][樂器]嗎":
        # write your code here
        pass

    if utterance == "[你][會]什麼[樂器]":
        # write your code here
        pass

    if utterance == "[你][會]唱歌嗎":
        # write your code here
        pass

    if utterance == "[你][會]彈什麼樂器":
        # write your code here
        pass

    if utterance == "[你][會]打[排球]嗎":
        # write your code here
        pass

    if utterance == "[你][會]聽什麼類型的音樂":
        # write your code here
        pass

    if utterance == "[你][會]運動嗎":
        # write your code here
        pass

    if utterance == "[你][網球]有得過[任何]獎嗎":
        # write your code here
        pass

    if utterance == "[你]喜歡[韓國][流行][音樂]嗎":
        # write your code here
        pass

    if utterance == "[你]喜歡什麼[類型]的[電影]":
        # write your code here
        pass

    if utterance == "[你]喜歡哪種[藝術]":
        # write your code here
        pass

    if utterance == "[你]喜歡打[排球]嗎":
        # write your code here
        pass

    if utterance == "[你]喜歡玩[網球]嗎":
        # write your code here
        pass

    if utterance == "[你]喜歡畫畫嗎":
        # write your code here
        pass

    if utterance == "[你]喜歡看[恐怖][電影]嗎":
        # write your code here
        pass

    if utterance == "[你]喜歡看[電影]嗎":
        # write your code here
        pass

    if utterance == "[你]喜歡看什麼類型的[書]":
        # write your code here
        pass

    if utterance == "[你]喜歡聽什麼類型的音樂":
        # write your code here
        pass

    if utterance == "[你]喜歡閱讀嗎":
        # write your code here
        pass

    if utterance == "[你]喜歡雕塑嗎":
        # write your code here
        pass

    if utterance == "[你]在打羽球的[時候]有受過傷嗎":
        # write your code here
        pass

    if utterance == "[你]對打[排球]有興趣嗎":
        # write your code here
        pass

    if utterance == "[你]工作時[會]聽音樂嗎":
        # write your code here
        pass

    if utterance == "[你]想[一起]去看嗎":
        # write your code here
        pass

    if utterance == "[你]支持的隊伍贏了嗎":
        # write your code here
        pass

    if utterance == "[你]是[任何][籃球隊]的粉絲嗎":
        # write your code here
        pass

    if utterance == "[你]是[棒球迷]嗎":
        # write your code here
        pass

    if utterance == "[你]有做什麼運動":
        # write your code here
        pass

    if utterance == "[你]有參加[任何]運動隊伍嗎":
        # write your code here
        pass

    if utterance == "[你]看過[任何][動作][片]嗎":
        # write your code here
        pass

    if utterance == "[你]知道[王力宏]嗎":
        # write your code here
        pass

    if utterance == "[你]知道[麥可喬丹]嗎":
        # write your code here
        pass

    if utterance == "[你]聽過[星際效應][這部][電影]嗎":
        # write your code here
        pass

    if utterance == "[你]讀書時喜歡聽什麼類型的音樂":
        # write your code here
        pass

    if utterance == "[你們]的隊伍贏了嗎":
        # write your code here
        pass

    if utterance == "[我][最]喜歡的[電影]是[阿凡達]":
        # write your code here
        pass

    if utterance == "[我][會]打[排球]":
        # write your code here
        pass

    if utterance == "[我][會]畫風景":
        # write your code here
        pass

    if utterance == "[我]喜歡[油畫]":
        # write your code here
        pass

    if utterance == "[我]喜歡打[棒球]":
        # write your code here
        pass

    if utterance == "[最]讓[你]想跳舞的音樂是哪首歌":
        # write your code here
        pass

    if utterance == "[棒球]的規則是什麼":
        # write your code here
        pass

    if utterance == "[能]唱[一首]歌給[我]聽嗎":
        # write your code here
        pass

    if utterance == "哪首歌讓[你]最想跳舞":
        # write your code here
        pass

    if utterance == "唱首歌來聽聽":
        # write your code here
        pass

    if utterance == "要[一起]看嗎":
        # write your code here
        pass

    if utterance == "誰是[你][最]喜歡的[歌手]":
        # write your code here
        pass

    if utterance == "除了[浪漫][愛情喜劇]，[你]還喜歡什麼[類型]的[電影]":
        # write your code here
        pass

    return resultDICT