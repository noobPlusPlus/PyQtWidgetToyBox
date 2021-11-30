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
        msg = jsonObject.get("msg")
        if msg != "成功":
            return ""

        chinaDayList = jsonObject.get("data").get("chinaDayList")
        todayArray = [["date", "确诊", "疑似", "输入"]]
        totalArray = [["date", "累计确诊", "现有确诊"]]

        for i in range(len(chinaDayList)):
            today = chinaDayList[i].get("today")
            todayInfo = []
            todayInfo.append(chinaDayList[i].get("date"))
            todayInfo.append(today.get("confirm"))
            todayInfo.append(today.get("suspect"))
            todayInfo.append(today.get("input"))
            todayArray.append(todayInfo)

            total = chinaDayList[i].get("total")
            totalInfo = []
            totalInfo.append(chinaDayList[i].get("date"))
            totalInfo.append(total.get("confirm"))
            totalInfo.append(total.get("storeConfirm"))
            totalArray.append(totalInfo)

        updateTime = jsonObject.get("data").get("lastUpdateTime")
        return [json.dumps(todayArray), json.dumps(totalArray), updateTime]

    def getMapData(self):
        r = requests.get(self.__url, headers=self.__header)
        jsonObject = r.json()
        msg = jsonObject.get("msg")
        if msg != "成功":
            return ""

        areaTree = jsonObject.get("data").get("areaTree")
        chinaDailyData = []
        for i in range(len(areaTree)):
            countryObject = areaTree[i]
            if countryObject.get("name") != "中国":
                continue
            for j in range(len(countryObject.get("children"))):
                provinceObject = countryObject.get("children")[j]
                provinceTotal = provinceObject.get("total")
                province = {}
                province["name"] = provinceObject.get("name")
                province["value"] = [provinceTotal.get("confirm"),
                                provinceTotal.get("suspect"),
                                provinceTotal.get("heal"),
                                provinceTotal.get("dead")]
                chinaDailyData.append(province)

        updateTime = jsonObject.get("data").get("lastUpdateTime")
        return [json.dumps(chinaDailyData), updateTime]

    def getGeneralView(self):
        r = requests.get(self.__url, headers=self.__header)
        jsonObject = r.json()
        msg = jsonObject.get("msg")
        if msg != "成功":
            return ""

        generalViewDatas = []
        totalObject = jsonObject.get("data").get("chinaTotal").get("total")
        todayObject = jsonObject.get("data").get("chinaTotal").get("today")

        inputData = (totalObject.get("input", 0), todayObject.get("input", 0))
        generalViewDatas.append(inputData)

        extDataObject = jsonObject.get("data").get("chinaTotal").get("extData")
        noSymptomData = (extDataObject.get("noSymptom", 0), extDataObject.get("incrNoSymptom", 0))
        generalViewDatas.append(noSymptomData)

        totalConfirm = totalObject.get("confirm", 0)
        confirmData = (totalConfirm, todayObject.get("confirm", 0))

        totalDead = totalObject.get("dead", 0)
        deadData = (totalDead, todayObject.get("dead", 0))

        totalHeal = totalObject.get("heal", 0)
        healData = (totalHeal, todayObject.get("heal", 0))

        storeConfirm = totalConfirm - totalDead - totalHeal
        storeConfirmData = (storeConfirm, todayObject.get("storeConfirm", 0))
        generalViewDatas.append(storeConfirmData)
        generalViewDatas.append(confirmData)
        generalViewDatas.append(deadData)
        generalViewDatas.append(healData)

        return generalViewDatas
