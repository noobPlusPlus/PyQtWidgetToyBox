import QtQuick 2.15
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.15
import QtWebEngine 1.1
import QtWebChannel 1.0

import "./Covid19MapHttpRequest.js" as Covid19MapHttpRequest

Item {
    QtObject {
        id: webObject
        WebChannel.id: "webObject"
        signal setData(string chinaDailyData, string updateTime);
    }

    WebEngineView {
        width:1000;
        anchors.centerIn: parent
        id:webview
        anchors.fill: parent
        url: "map.html"
        webChannel: channel
    }

    WebChannel {
        id: channel
        registeredObjects: [webObject]
    }

    Timer{
        id: timer;
        interval: 1000;
        repeat: false;
        triggeredOnStart: false;

        onTriggered: {
            Covid19MapHttpRequest.request();
        }
    }

    Component.onCompleted: {
       timer.start();
    }
}
