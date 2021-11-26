function request(){
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if(xhr.readyState !== XMLHttpRequest.DONE)
            return;

        let jsonObject = JSON.parse(xhr.responseText.toString());
        if(jsonObject.msg !== "成功")
            return;

        let chinaDayList = jsonObject.data.chinaDayList;
        //console.log(chinaDayList);
        let todayArray = [["date", "确诊", "疑似", "输入"]];
        let totalArray = [["date", "累计确诊", "现有确诊"]];
        for(let i = 0,length = chinaDayList.length; i < length; i++)
        {
            let today = chinaDayList[i].today;
            let todayInfo = [];
            todayInfo.push(chinaDayList[i].date);
            todayInfo.push(today.confirm);
            todayInfo.push(today.suspect);
            todayInfo.push(today.input);
            todayArray.push(todayInfo);

            let total = chinaDayList[i].total;
            let totalInfo = [];
            totalInfo.push(chinaDayList[i].date);
            totalInfo.push(total.confirm);
            totalInfo.push(total.storeConfirm);
            totalArray.push(totalInfo);
        }

        let updateTime = jsonObject.data.lastUpdateTime;
        webObject.setData(JSON.stringify(todayArray), JSON.stringify(totalArray), updateTime);
    }
    xhr.open("GET", "http://c.m.163.com/ug/api/wuhan/app/data/list-total");
    xhr.send();
}
