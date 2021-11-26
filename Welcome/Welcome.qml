import QtQuick 2.0
import QtQuick.Controls 2.15

//ScrollView
//{
//    anchors.fill: parent;
//    clip:true;
//    TextArea
//    {
//        anchors.fill: parent
//        //anchors.margins: 20
//        clip: true
//        readOnly: true;
//        textFormat: Text.MarkdownText;
//       // wrapMode: TextEdit.WordWrap;

//        function request() {
//            var xhr = new XMLHttpRequest();
//            xhr.onreadystatechange = function() {
//                if(xhr.readyState === XMLHttpRequest.DONE) {
//                    text = xhr.responseText.toString();
//                }
//            }
//            xhr.open("GET", "../README.md");
//            xhr.send();
//        }

//        Component.onCompleted: {
//            request()
//        }
//    }
//}

Rectangle {
      id: frame
      clip: true
      width: parent.width
      height: parent.height
      anchors.centerIn: parent
      anchors.top: parent.bottom
      anchors.left: parent.left
      focus: true
      Keys.onUpPressed: vbar.decrease()
      Keys.onDownPressed: vbar.increase()

      TextEdit {
          id: textEdit
          font.pointSize: 14
          height: contentHeight
          width: frame.width - vbar.width
          y: -vbar.position * textEdit.height
          wrapMode: TextEdit.Wrap

          textFormat: Text.MarkdownText;

          function request() {
              var xhr = new XMLHttpRequest();
              xhr.onreadystatechange = function() {
                  if(xhr.readyState === XMLHttpRequest.DONE) {
                      text = xhr.responseText.toString();
                  }
              }
              xhr.open("GET", "../README.md");
              xhr.send();
          }

          Component.onCompleted: {
              request()
          }

          MouseArea{
              anchors.fill: parent
              onWheel: {
                  if (wheel.angleDelta.y > 0) {
                      vbar.decrease();
                  }
                  else {
                      vbar.increase();
                  }
              }
          }
      }

      ScrollBar {
          id: vbar
          hoverEnabled: true
          active: hovered || pressed
          orientation: Qt.Vertical
          size: frame.height / textEdit.height
          width: 10
          anchors.top: parent.top
          anchors.right: parent.right
          anchors.bottom: parent.bottom
      }
  }
