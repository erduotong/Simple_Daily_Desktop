# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName("settings")
        settings.resize(1920, 1080)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        settings.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(settings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(settings)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setStyleSheet("")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.widget_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 243, 868))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.to_program_config = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_program_config.sizePolicy().hasHeightForWidth())
        self.to_program_config.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.to_program_config.setFont(font)
        self.to_program_config.setObjectName("to_program_config")
        self.verticalLayout_4.addWidget(self.to_program_config)
        self.to_daily_config = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_daily_config.sizePolicy().hasHeightForWidth())
        self.to_daily_config.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(15)
        self.to_daily_config.setFont(font)
        self.to_daily_config.setObjectName("to_daily_config")
        self.verticalLayout_4.addWidget(self.to_daily_config)
        self.to_lessons = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_lessons.sizePolicy().hasHeightForWidth())
        self.to_lessons.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.to_lessons.setFont(font)
        self.to_lessons.setObjectName("to_lessons")
        self.verticalLayout_4.addWidget(self.to_lessons)
        self.to_time = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_time.sizePolicy().hasHeightForWidth())
        self.to_time.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.to_time.setFont(font)
        self.to_time.setObjectName("to_time")
        self.verticalLayout_4.addWidget(self.to_time)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setStyleSheet("")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setObjectName("tabWidget")
        self.set_program_config = QtWidgets.QWidget()
        self.set_program_config.setObjectName("set_program_config")
        self.tabWidget.addTab(self.set_program_config, "")
        self.set_daily_config = QtWidgets.QWidget()
        self.set_daily_config.setObjectName("set_daily_config")
        self.tabWidget.addTab(self.set_daily_config, "")
        self.set_lessons = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.set_lessons.setFont(font)
        self.set_lessons.setObjectName("set_lessons")
        self.tabWidget.addTab(self.set_lessons, "")
        self.show_about = QtWidgets.QWidget()
        self.show_about.setObjectName("show_about")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.show_about)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.show_about)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.widget_5 = QtWidgets.QWidget(self.show_about)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.now_version = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.now_version.setFont(font)
        self.now_version.setObjectName("now_version")
        self.verticalLayout_5.addWidget(self.now_version)
        self.label_3 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.verticalLayout_6.addWidget(self.widget_5)
        self.verticalLayout_6.setStretch(0, 3)
        self.verticalLayout_6.setStretch(1, 8)
        self.tabWidget.addTab(self.show_about, "")
        self.set_time = QtWidgets.QWidget()
        self.set_time.setObjectName("set_time")
        self.tabWidget.addTab(self.set_time, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.gridLayout.addWidget(self.widget_4, 1, 1, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_exit = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_exit.sizePolicy().hasHeightForWidth())
        self.save_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.save_exit.setFont(font)
        self.save_exit.setObjectName("save_exit")
        self.horizontalLayout.addWidget(self.save_exit)
        self.not_save_exit = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.not_save_exit.sizePolicy().hasHeightForWidth())
        self.not_save_exit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(17)
        self.not_save_exit.setFont(font)
        self.not_save_exit.setObjectName("not_save_exit")
        self.horizontalLayout.addWidget(self.not_save_exit)
        self.to_about = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to_about.sizePolicy().hasHeightForWidth())
        self.to_about.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        self.to_about.setFont(font)
        self.to_about.setObjectName("to_about")
        self.horizontalLayout.addWidget(self.to_about)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 6)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 13)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(settings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        _translate = QtCore.QCoreApplication.translate
        settings.setWindowTitle(_translate("settings", "Form"))
        self.to_program_config.setText(_translate("settings", "程序基本设置"))
        self.to_daily_config.setText(_translate("settings", "今日配置文件更改"))
        self.to_lessons.setText(_translate("settings", "课表设置"))
        self.to_time.setText(_translate("settings", "课程时间设置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_program_config), _translate("settings", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_daily_config), _translate("settings", "页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_lessons), _translate("settings", "Tab 2"))
        self.label.setText(_translate("settings", "Simple_Class_Information_Display"))
        self.now_version.setText(_translate("settings", "版本号:等待读取"))
        self.label_3.setText(_translate("settings", "项目链接:<a href=\"https://github.com/erduotong/Simple_Class_Information_Display/\">https://github.com/erduotong/Simple_Class_Information_Display/</a>"))
        self.label_4.setText(_translate("settings", "制作:耳朵同\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.show_about), _translate("settings", "页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.set_time), _translate("settings", "页"))
        self.save_exit.setText(_translate("settings", "保存并退出"))
        self.not_save_exit.setText(_translate("settings", "不保存并退出"))
        self.to_about.setText(_translate("settings", "关于"))