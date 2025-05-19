# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_playlist.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QVBoxLayout, QWidget)

from PySide_UI.ui.tools.base.idbutton import IdButton
from PySide_UI.ui.tools.base.idlabel import IdLabel

class Ui_playlist(object):
    def setupUi(self, playlist):
        if not playlist.objectName():
            playlist.setObjectName(u"playlist")
        playlist.resize(150, 220)
        playlist.setMinimumSize(QSize(150, 220))
        playlist.setMaximumSize(QSize(150, 16777215))
        playlist.setStyleSheet(u"*{\n"
"	border: none;\n"
"}\n"
"QPushButton[listid], QLabel[listid]{\n"
"	font-size: 18px;\n"
"	border: none;\n"
"}\n"
"QWidget[playlist]:hover{\n"
"	background-color: rgba(255, 255, 255, 0.2);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"/*\u6b4c\u5355\u540d\u79f0*/\n"
"QLabel{\n"
"	font-size: 18px;\n"
"}\n"
"QLabel:hover{\n"
"	color: #DE76A3;\n"
"	font-size: 18px;\n"
"}\n"
"/*\u6b4c\u5355\u56fe\u7247\u6309\u94ae*/\n"
"QPushButton[listid] {\n"
"	/* border: 2px solid white; */\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton[listid]:hover {\n"
"	margin: 3px;\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton[listid]:pressed {\n"
"	margin: 1px;\n"
"	border-radius: 10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(playlist)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.list_img_btn = IdButton(playlist)
        self.list_img_btn.setObjectName(u"list_img_btn")
        self.list_img_btn.setMinimumSize(QSize(120, 120))
        self.list_img_btn.setMaximumSize(QSize(120, 120))
        self.list_img_btn.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.list_img_btn)

        self.list_name_lab = IdLabel(playlist)
        self.list_name_lab.setObjectName(u"list_name_lab")
        self.list_name_lab.setMinimumSize(QSize(120, 40))
        self.list_name_lab.setMaximumSize(QSize(120, 16777215))
        self.list_name_lab.setStyleSheet(u"")
        self.list_name_lab.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.list_name_lab.setWordWrap(True)

        self.verticalLayout.addWidget(self.list_name_lab)


        self.retranslateUi(playlist)

        QMetaObject.connectSlotsByName(playlist)
    # setupUi

    def retranslateUi(self, playlist):
        playlist.setWindowTitle(QCoreApplication.translate("playlist", u"Form", None))
        playlist.setProperty(u"playlist", QCoreApplication.translate("playlist", u"-1", None))
        self.list_img_btn.setText("")
        self.list_img_btn.setProperty(u"listid", QCoreApplication.translate("playlist", u"-1", None))
        self.list_name_lab.setText("")
        self.list_name_lab.setProperty(u"listid", QCoreApplication.translate("playlist", u"-1", None))
    # retranslateUi

