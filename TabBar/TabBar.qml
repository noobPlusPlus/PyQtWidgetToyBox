import QtQuick 2.0
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Item
{
    signal changeTab(string qmlName)

    required property ListModel tabBarlistModel;

    ListView
    {
        id : listView
        anchors.fill: parent
        anchors.margins: 20
        clip: true
        model: tabBarlistModel;
        delegate: numberDelegate
        spacing: 0
        focus: true

        ScrollBar.vertical: ScrollBar{
            width:6;
        }
    }

    Component
    {
        id: numberDelegate

        Rectangle
        {
            width: ListView.view.width
            height: 40
            color: ListView.isCurrentItem | isHoverd ? "#EFEFEF" : "#FFFFFF"
            border.color: Qt.lighter(color, 1.1)
            property bool isHoverd: false;
            Text
            {
                anchors.centerIn: parent
                font.pixelSize: 16
                text: tabTitle
            }

            MouseArea
            {
                anchors.fill: parent
                onClicked:
                {
                    listView.currentIndex = index  //实现item切换
                    changeTab(tabName);
                }
                hoverEnabled: true;
                onEntered: isHoverd = true;
                onExited: isHoverd = false;
            }
        }
    }
}
