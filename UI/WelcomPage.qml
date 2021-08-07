import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Component {
    Rectangle {

        Rectangle {
            anchors.fill: parent

            Image {
                sourceSize: Qt.size(parent.width, parent.height)
                fillMode: Image.PreserveAspectCrop
                anchors.centerIn: parent
                source: "./UsedImages/Welcome.jpg"
            }

        }

        Text {
            anchors.centerIn: parent
            text: username + ", you have been signed in"
            font.pixelSize: 16
            color: "red"
        }

    }
}
