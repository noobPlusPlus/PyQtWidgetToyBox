import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15
import "TabBar"
import "TabPane"

Window
{
    id: root
    width: 1440
    height: 900
    visible: true
    title: qsTr("Toy Box")
    property string fontFamily: "Microsoft YaHei";

    RowLayout
    {
        TabBar
        {
            id:tabBar;
            width:200;
            height:root.height;
            tabBarlistModel : ListModel
            {
                ListElement { tabTitle: qsTr("欢迎"); tabName:"Welcome";}
                ListElement { tabTitle: qsTr("Covid19 概览"); tabName:"Covid19GeneralView";}
                ListElement { tabTitle: qsTr("Covid19 图表"); tabName:"Covid19Charts";}
                ListElement { tabTitle: qsTr("Covid19 地图"); tabName:"Covid19Map";}
            }

            onChangeTab:
            {
                tabPane.source = qmlName + "/" + qmlName + ".qml";
            }
        }


        TabPane
        {
            width: root.width - tabBar.width;
            height:root.height;
            source: "Welcome/Welcome.qml";
            id:tabPane;
        }
    }

    Component.onCompleted: {
        root.showMaximized();
    }
}

