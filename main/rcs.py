# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_rcs.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(607, 445)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setWindowTitle("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout_4.addWidget(self.textBrowser_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_5.addWidget(self.textBrowser)
        self.monday = QtWidgets.QRadioButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.monday.setFont(font)
        self.monday.setObjectName("monday")
        self.verticalLayout_5.addWidget(self.monday)
        self.tuesday = QtWidgets.QRadioButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.tuesday.setFont(font)
        self.tuesday.setObjectName("tuesday")
        self.verticalLayout_5.addWidget(self.tuesday)
        self.wednesday = QtWidgets.QRadioButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.wednesday.setFont(font)
        self.wednesday.setObjectName("wednesday")
        self.verticalLayout_5.addWidget(self.wednesday)
        self.thursday = QtWidgets.QRadioButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.thursday.setFont(font)
        self.thursday.setObjectName("thursday")
        self.verticalLayout_5.addWidget(self.thursday)
        self.friday = QtWidgets.QRadioButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.friday.setFont(font)
        self.friday.setObjectName("friday")
        self.verticalLayout_5.addWidget(self.friday)
        self.saturday = QtWidgets.QRadioButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.saturday.setFont(font)
        self.saturday.setObjectName("saturday")
        self.verticalLayout_5.addWidget(self.saturday)
        self.sunday = QtWidgets.QRadioButton(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.sunday.setFont(font)
        self.sunday.setObjectName("sunday")
        self.verticalLayout_5.addWidget(self.sunday)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.widget_3)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 20)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">你似乎在没有课程的日期进行使用,请点击以替换课表</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">要退出请按下面的按钮！否则会出错</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'黑体\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
        self.monday.setText(_translate("Dialog", "周一"))
        self.tuesday.setText(_translate("Dialog", "周二"))
        self.wednesday.setText(_translate("Dialog", "周三"))
        self.thursday.setText(_translate("Dialog", "周四"))
        self.friday.setText(_translate("Dialog", "周五"))
        self.saturday.setText(_translate("Dialog", "周六"))
        self.sunday.setText(_translate("Dialog", "周日"))
        self.pushButton.setText(_translate("Dialog", "更换课表"))
        self.pushButton_2.setText(_translate("Dialog", "按原课表继续"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
