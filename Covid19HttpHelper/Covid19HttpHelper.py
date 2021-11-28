# This Python file uses the following encoding: utf-8
from PyQt5 import QtCore
import requests
import json


class Covid19HttpHelper(QtCore.QObject):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__url = "http://c.m.163.com/ug/api/wuhan/app/data/list-total"
        self.__header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64)"}

    def getChartsData(self):
        r = requests.get(self.__url, headers=self.__header)
        jsonObject = r.json()
        msg = jsonObject["msg"]
        if msg != "成功":
            return ""

        chinaDayList = jsonObject["data"]["chinaDayList"]
        todayArray = [["date", "确诊", "疑似", "输入"]]
        totalArray = [["date", "累计确诊", "现有确诊"]]

        for i in range(len(chinaDayList)):
            today = chinaDayList[i]["today"]
            todayInfo = []
            todayInfo.append(chinaDayList[i]["date"])
            todayInfo.append(today["confirm"])
            todayInfo.append(today["suspect"])
            todayInfo.append(today["input"])
            todayArray.append(todayInfo)

            total = chinaDayList[i]["total"]
            totalInfo = []
            totalInfo.append(chinaDayList[i]["date"])
            totalInfo.append(total["confirm"])
            totalInfo.append(total["storeConfirm"])
            totalArray.append(totalInfo)

        updateTime = jsonObject["data"]["lastUpdateTime"]
        return [json.dumps(todayArray), json.dumps(totalArray), updateTime]

    def getMapData(self):
        r = requests.get(self.__url, headers=self.__header)
        jsonObject = r.json()
        msg = jsonObject["msg"]
        if msg != "成功":
            return ""

        areaTree = jsonObject["data"]["areaTree"]
        chinaDailyData = []
        for i in range(len(areaTree)):
            countryObject = areaTree[i]
            if countryObject["name"] != "中国":
                continue
            for j in range(len(countryObject["children"])):
                provinceObject = countryObject["children"][j]
                provinceTotal = provinceObject["total"]
                province = {}
                province["name"] = provinceObject["name"]
                province["value"] = [provinceTotal["confirm"],
                                provinceTotal["suspect"],
                                provinceTotal["heal"],
                                provinceTotal["dead"]]
                chinaDailyData.append(province)

        updateTime = jsonObject["data"]["lastUpdateTime"]
        return [json.dumps(chinaDailyData), updateTime]

    def getGeneralView(self):
        r = requests.get(self.__url, headers=self.__header)
        jsonObject = r.json()
        msg = jsonObject["msg"]
        if msg != "成功":
            return ""

        generalViewDatas = []
        totalObject = jsonObject["data"]["chinaTotal"]["total"]
        todayObject = jsonObject["data"]["chinaTotal"]["today"]

        inputData = (totalObject["input"], todayObject["input"])
        generalViewDatas.append(inputData)

        extDataObject = jsonObject["data"]["chinaTotal"]["extData"]
        noSymptomData = (extDataObject["noSymptom"], extDataObject["incrNoSymptom"])
        generalViewDatas.append(noSymptomData)

        totalConfirm = totalObject["confirm"]
        confirmData = (totalConfirm, todayObject["confirm"])

        totalDead = totalObject["dead"]
        deadData = (totalDead, todayObject["dead"])

        totalHeal = totalObject["heal"]
        healData = (totalHeal, todayObject["heal"])

        storeConfirm = totalConfirm - totalDead - totalHeal
        storeConfirmData = (storeConfirm, todayObject["storeConfirm"])
        generalViewDatas.append(storeConfirmData)
        generalViewDatas.append(confirmData)
        generalViewDatas.append(deadData)
        generalViewDatas.append(healData)

        return generalViewDatas
