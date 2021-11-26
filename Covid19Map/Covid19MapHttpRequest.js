function request(){
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if(xhr.readyState !== XMLHttpRequest.DONE)
            return;

        let jsonObject = JSON.parse(xhr.responseText.toString());
        if(jsonObject.msg !== "成功")
            return;

        let areaTree = jsonObject.data.areaTree;
        let chinaDailyData = [];
        for(let i = 0,iLength = areaTree.length; i < iLength; i++)
        {
            let countryObject = areaTree[i];
            if(countryObject.name !== "中国")
                continue;

            for(let j = 0, jLength = countryObject.children.length; j < jLength; j++)
            {
                let provinceObject = countryObject.children[j];
                let provinceTotal = provinceObject.total;
                let province = {};
                province.name = provinceObject.name;
                province.value=[provinceTotal.confirm,
                                provinceTotal.suspect,
                                provinceTotal.heal,
                                provinceTotal.dead];
                chinaDailyData.push(province);
            }
        }

        let updateTime = jsonObject.data.lastUpdateTime;
        webObject.setData(JSON.stringify(chinaDailyData), updateTime);
    }
    xhr.open("GET", "http://c.m.163.com/ug/api/wuhan/app/data/list-total");
    xhr.send();
}
