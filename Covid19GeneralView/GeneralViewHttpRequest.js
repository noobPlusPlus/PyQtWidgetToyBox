function request(){
    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if(xhr.readyState !== XMLHttpRequest.DONE)
            return;

        let jsonObject = JSON.parse(xhr.responseText.toString());
        if(jsonObject.msg !== "成功")
            return;

        infoRepeaterModel.get(0).total = jsonObject.data.chinaTotal.total.input;
        infoRepeaterModel.get(0).increase = jsonObject.data.chinaTotal.today.input;

        infoRepeaterModel.get(1).total = jsonObject.data.chinaTotal.extData.noSymptom;
        infoRepeaterModel.get(1).increase = jsonObject.data.chinaTotal.extData.incrNoSymptom;

        let totalConfirm = jsonObject.data.chinaTotal.total.confirm;
        infoRepeaterModel.get(3).total = totalConfirm;
        infoRepeaterModel.get(3).increase = jsonObject.data.chinaTotal.today.confirm;

        let totalDead = jsonObject.data.chinaTotal.total.dead;
        infoRepeaterModel.get(4).total = totalDead;
        infoRepeaterModel.get(4).increase = jsonObject.data.chinaTotal.today.dead;

        let totalHeal = jsonObject.data.chinaTotal.total.heal;
        infoRepeaterModel.get(5).total = totalHeal;
        infoRepeaterModel.get(5).increase = jsonObject.data.chinaTotal.today.heal;

        infoRepeaterModel.get(2).total = totalConfirm - totalDead - totalHeal;
        infoRepeaterModel.get(2).increase = jsonObject.data.chinaTotal.today.storeConfirm;
    }
    xhr.open("GET", "http://c.m.163.com/ug/api/wuhan/app/data/list-total");
    xhr.send();
}
