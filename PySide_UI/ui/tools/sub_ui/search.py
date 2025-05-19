# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_search(object):
    def setupUi(self, search):
        if not search.objectName():
            search.setObjectName(u"search")
        search.resize(1076, 484)
        search.setMinimumSize(QSize(1076, 484))
        search.setMaximumSize(QSize(16777215, 16777215))
        search.setStyleSheet(u"*{\n"
"	/*background-color: rgba(255, 255, 255, 0.6);*/\n"
"	background-color: transparent;\n"
"	color: #fff8ea;\n"
"	border: 2px solid white;\n"
"	font-size: 16px;\n"
"	font-weight: 700;\n"
"	font-family: ZCOOL KuaiLe;\n"
"}\n"
"/*\u641c\u7d22\u6846*/\n"
"#search_lineEdit{\n"
"	font-size: 20px;\n"
"	font-weight: 800;\n"
"	background: transparent;\n"
"	border: 2px solid white;\n"
"	border-radius: 6px;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"}\n"
"#search_lineEdit:focus{\n"
"	border: 2px solid #E3629A;\n"
"	background: rgba(255, 255, 255, 0.2);\n"
"}\n"
"/*\u641c\u7d22\u6309\u94ae*/\n"
"#sub_search_btn{\n"
"	border-radius: 5px;\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/search_1.png)\uff1b\n"
"}\n"
"#sub_search_btn:hover{\n"
"	/*border-radius: 5px;\n"
"	background-color: rgba(255, 255, 255, 0.4);*/\n"
"	margin: 2px;\n"
"}\n"
"/*\u641c\u7d22\u6309\u94ae*/\n"
"\n"
"\n"
"\n"
"/*\u5782\u76f4\u6eda\u52a8\u6761\u6837\u5f0f*/\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    width:"
                        " 0;  /* \u9690\u85cf\u6c34\u5e73\u6eda\u52a8\u6761\u7684\u7bad\u5934 */\n"
"    height: 0; /* \u9690\u85cf\u5782\u76f4\u6eda\u52a8\u6761\u7684\u7bad\u5934 */\n"
"}\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: transparent;\n"
"    /*background: rgba(255, 255, 255, 0.5);*/\n"
"	border: 0px;\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"    padding-bottom: 2px;\n"
"}\n"
"QScrollBar{\n"
"    width: 10px;\n"
"    border: 0px;\n"
"    border-radius: 5px;\n"
"	padding: 2px;\n"
"}\n"
"QScrollBar::handle{\n"
"	width: 4px;\n"
"	border-radius: 2px;\n"
"	/*background-color: #84ACD9;*/\n"
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #639AD4, stop: 1 #DE76A3);\n"
"}\n"
"QScrollBar::handle:hover{\n"
"	/*background-color: #75ACEB;*/\n"
"	background-color: qlineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #639AD4, stop: 1 #DE76A3);\n"
"}\n"
"QScrollBar:vertical {\n"
"    border: none;          /* \u53bb\u9664\u6eda\u52a8\u6761\u6574\u4f53\u8fb9\u6846 */\n"
"    backgro"
                        "und: transparent;  /* \u80cc\u666f\u900f\u660e\uff08\u53ef\u9009\uff09 */\n"
"}\n"
"QScrollArea .QWidget{\n"
"	border: none;\n"
"}\n"
"QScrollArea{\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"/*\u5782\u76f4\u6eda\u52a8\u6761\u6837\u5f0f*/\n"
"\n"
"/*\u63a8\u8350\u9875\u9762\u901a\u7528\u6837\u5f0f*/\n"
"[recommend]{\n"
"	font-weight: 700;\n"
"	font-size: 30px;\n"
"}\n"
"[day]{\n"
"	font-size: 18px;\n"
"}\n"
"/*\u63a8\u8350\u9875\u9762\u901a\u7528\u6837\u5f0f*/")
        self.verticalLayout = QVBoxLayout(search)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(15)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_36)

        self.search_lineEdit = QLineEdit(search)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setMinimumSize(QSize(250, 30))
        self.search_lineEdit.setMaximumSize(QSize(250, 30))

        self.horizontalLayout_25.addWidget(self.search_lineEdit)

        self.sub_search_btn = QPushButton(search)
        self.sub_search_btn.setObjectName(u"sub_search_btn")
        self.sub_search_btn.setMinimumSize(QSize(30, 30))
        self.sub_search_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_25.addWidget(self.sub_search_btn)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_37)


        self.verticalLayout.addLayout(self.horizontalLayout_25)

        self.search_music_scrollArea = QScrollArea(search)
        self.search_music_scrollArea.setObjectName(u"search_music_scrollArea")
        self.search_music_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 1032, 393))
        self.verticalLayout_29 = QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(10, 10, 10, 10)
        self.search_music_verticalLayout = QVBoxLayout()
        self.search_music_verticalLayout.setObjectName(u"search_music_verticalLayout")

        self.verticalLayout_29.addLayout(self.search_music_verticalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 313, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_29.addItem(self.verticalSpacer_4)

        self.search_music_scrollArea.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout.addWidget(self.search_music_scrollArea)


        self.retranslateUi(search)

        QMetaObject.connectSlotsByName(search)
    # setupUi

    def retranslateUi(self, search):
        search.setWindowTitle(QCoreApplication.translate("search", u"Form", None))
        self.sub_search_btn.setText("")
    # retranslateUi

