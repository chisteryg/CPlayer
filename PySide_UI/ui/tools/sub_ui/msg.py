# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'msg.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from PySide_UI.ui.tools.base.movewidget import MoveWidget
import resource_rc

class Ui_msg(object):
    def setupUi(self, msg):
        if not msg.objectName():
            msg.setObjectName(u"msg")
        msg.resize(480, 370)
        msg.setMinimumSize(QSize(480, 370))
        msg.setMaximumSize(QSize(480, 370))
        msg.setStyleSheet(u"QWidget#msg{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #EEAECA, stop: 1 #94BBE9);\n"
"	background-color: #A3BCE6;\n"
"}\n"
"*{\n"
"	background-color: transparent;\n"
"	color: #fff8ea;\n"
"	/*border: 2px solid white;*/\n"
"	font-size: 16px;\n"
"	font-weight: 700;\n"
"	font-family: ZCOOL KuaiLe;\n"
"}\n"
"#move_widget{\n"
"	border-bottom: 2px solid white;\n"
"}\n"
"#title_lab{\n"
"	padding-left: 5px;\n"
"	font-size: 23px;\n"
"	color: #CF467F;\n"
"	border: none;\n"
"}\n"
"#msg_lab{\n"
"	font-size: 20px;\n"
"	color: #CF467F;\n"
"	border: none;\n"
"}\n"
"\n"
"#close_btn:hover{\n"
"	color: white;\n"
"	margin: 2px;\n"
"}\n"
"#close_btn{\n"
"	border-image: url(:/title/tools/resource/bg/icon/title/clear.png);\n"
"}\n"
"\n"
"#ok_btn{\n"
"	border: 2px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"#ok_btn:hover{\n"
"	color: #DE76A3;\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"	margin: 2px;\n"
"}\n"
"#ok_btn:pressed{\n"
"	color: white;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(msg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.move_widget = MoveWidget(msg)
        self.move_widget.setObjectName(u"move_widget")
        self.move_widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout = QHBoxLayout(self.move_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title_lab = QLabel(self.move_widget)
        self.title_lab.setObjectName(u"title_lab")

        self.horizontalLayout.addWidget(self.title_lab)

        self.horizontalSpacer = QSpacerItem(288, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(self.move_widget)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(30, 30))
        self.close_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout_2.addWidget(self.move_widget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 10, 20, 10)
        self.msg_lab = QLabel(msg)
        self.msg_lab.setObjectName(u"msg_lab")
        self.msg_lab.setMinimumSize(QSize(0, 170))
        self.msg_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.msg_lab.setWordWrap(True)

        self.verticalLayout.addWidget(self.msg_lab)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.ok_btn = QPushButton(msg)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setMinimumSize(QSize(60, 30))
        self.ok_btn.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_2.addWidget(self.ok_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(17, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(msg)
        self.ok_btn.clicked.connect(msg.close)
        self.close_btn.clicked.connect(msg.close)

        QMetaObject.connectSlotsByName(msg)
    # setupUi

    def retranslateUi(self, msg):
        msg.setWindowTitle(QCoreApplication.translate("msg", u"Form", None))
        self.title_lab.setText(QCoreApplication.translate("msg", u"msg_title", None))
        self.close_btn.setText("")
        self.msg_lab.setText(QCoreApplication.translate("msg", u"msg", None))
        self.ok_btn.setText(QCoreApplication.translate("msg", u"\u786e\u5b9a", None))
    # retranslateUi

