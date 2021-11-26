import QtQuick 2.15
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.15
import "./GeneralViewHttpRequest.js" as GeneralViewHttpRequest

Item {
    property ListModel infoRepeaterModel: ListModel
    {
        ListElement { titleString: qsTr("境外输入"); labelColor: "#FFA352"; total: 0; increase: 0;}
        ListElement { titleString: qsTr("无症状感染者"); labelColor: "#791618"; total: 0; increase: 0;}
        ListElement { titleString: qsTr("现有确诊"); labelColor: "#E44A3D"; total: 0; increase: 0;}
        ListElement { titleString: qsTr("累计确诊"); labelColor: "#A31D13"; total: 0; increase: 0;}
        ListElement { titleString: qsTr("累计死亡"); labelColor: "#333333"; total: 0; increase: 0;}
        ListElement { titleString: qsTr("累计治愈"); labelColor: "#34AA70"; total: 0; increase: 0;}
    }
    GridLayout
    {
        columns: 3 
        columnSpacing :20;
        rowSpacing :20;

        Repeater
        {
            id:infoRepeater;
            model: infoRepeaterModel

            Item
            {
                property int fontSize : 20;
                Layout.minimumWidth: 150;
                Layout.minimumHeight: 120;
                Layout.fillWidth: true;
                Layout.fillHeight: true;
                Layout.alignment: Qt.AlignHCenter;
                ColumnLayout
                {
                    spacing: 6;
                    Label
                    {
                        text: titleString;
                        font.bold: true;
                        font.pixelSize: fontSize;
                        font.family: root.fontFamily;
                        Layout.alignment: Qt.AlignHCenter;
                    }

                    Label
                    {
                        text: total.toString();
                        font.bold: true;
                        font.pixelSize: fontSize + 20;
                        font.family: root.fontFamily;
                        Layout.alignment: Qt.AlignHCenter;
                        color:labelColor;
                    }

                    RowLayout
                    {
                        Layout.alignment: Qt.AlignHCenter;
                        Label
                        {
                            text: qsTr("较昨日");
                            font.pixelSize: fontSize;
                            font.family: root.fontFamily;
                            color:"#9999A6";
                        }

                        Label
                        {
                            text: ((increase >= 0) ? "+" : "")  + increase.toString();
                            font.pixelSize: fontSize;
                            font.family: root.fontFamily;
                            color:labelColor;
                        }
                    }
                }
            }
        }
    }

    Component.onCompleted: {
        //需将js文件加入到资源中，否则找不到infoRepeaterModel
        GeneralViewHttpRequest.request()
    }
}
