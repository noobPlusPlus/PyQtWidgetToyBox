import QtQuick 2.15
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.15
import QtWebEngine 1.1
import QtWebChannel 1.0

import "./Covid19ChartsHttpRequest.js" as Covid19ChartsHttpRequest

Item {
    QtObject {
        id: webObject
        WebChannel.id: "webObject"
        signal setData(string todayData, string totalData, string updateTime);
    }

    WebChannel {
        id: channel
        registeredObjects: [webObject]
    }

    WebEngineView {
        width:1000;
        anchors.centerIn: parent
        id:webview
        anchors.fill: parent
        url: "charts.html"
        webChannel: channel
    }

    Timer{
        id: timer;
        interval: 1000;
        repeat: false;
        triggeredOnStart: false;

        onTriggered: {
            Covid19ChartsHttpRequest.request();
        }
    }

    Component.onCompleted: {
       timer.start();
    }
}
