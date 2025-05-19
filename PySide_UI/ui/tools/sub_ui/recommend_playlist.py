# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recommend_playlist.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_recommend_playlist(object):
    def setupUi(self, recommend_playlist):
        if not recommend_playlist.objectName():
            recommend_playlist.setObjectName(u"recommend_playlist")
        recommend_playlist.resize(1076, 484)
        recommend_playlist.setMinimumSize(QSize(1076, 484))
        recommend_playlist.setStyleSheet(u"*{\n"
"	/*background-color: rgba(255, 255, 255, 0.6);*/\n"
"	background-color: transparent;\n"
"	color: #fff8ea;\n"
"	border: 2px solid white;\n"
"	font-size: 16px;\n"
"	font-weight: 700;\n"
"	font-family: ZCOOL KuaiLe;\n"
"}\n"
"/*\u4e0a\u4e00\u9875\u3001\u4e0b\u4e00\u9875\u6309\u94ae*/\n"
"\n"
"QPushButton[page]{\n"
"	border: 2px solid #ca8f00;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton[page]:hover{\n"
"	font-size: 17px;\n"
"	background-color: #ca8f00;\n"
"}\n"
"/*\u4e0a\u4e00\u9875\u3001\u4e0b\u4e00\u9875\u6309\u94ae*/\n"
"\n"
"\n"
"/*\u5782\u76f4\u6eda\u52a8\u6761\u6837\u5f0f*/\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"    width: 0;  /* \u9690\u85cf\u6c34\u5e73\u6eda\u52a8\u6761\u7684\u7bad\u5934 */\n"
"    height: 0; /* \u9690\u85cf\u5782\u76f4\u6eda\u52a8\u6761\u7684\u7bad\u5934 */\n"
"}\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"    background: transparent;\n"
"    /*background: rgba(255, 255, 255, 0.5);*/\n"
"	border: 0px;\n"
"	border-radius: 2px;\n"
"	padding-top: 2px;\n"
"  "
                        "  padding-bottom: 2px;\n"
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
"    background: transparent;  /* \u80cc\u666f\u900f\u660e\uff08\u53ef\u9009\uff09 */\n"
"}\n"
"QScrollArea .QWidget{\n"
"	border: none;\n"
"}\n"
"QScrollArea{\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"}\n"
"\n"
"/*\u5782\u76f4\u6eda\u52a8\u6761\u6837\u5f0f*/\n"
"\n"
"/*\u63a8\u8350\u9875\u9762\u901a\u7528\u6837\u5f0f*/\n"
"[recommend]{\n"
"	font-weight: 700;\n"
"	fo"
                        "nt-size: 30px;\n"
"}\n"
"[day]{\n"
"	font-size: 18px;\n"
"}\n"
"/*\u63a8\u8350\u9875\u9762\u901a\u7528\u6837\u5f0f*/")
        self.verticalLayout = QVBoxLayout(recommend_playlist)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 10, 15, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_18)

        self.recommend_playlist_label = QLabel(recommend_playlist)
        self.recommend_playlist_label.setObjectName(u"recommend_playlist_label")
        self.recommend_playlist_label.setMinimumSize(QSize(200, 40))
        self.recommend_playlist_label.setStyleSheet(u"")
        self.recommend_playlist_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.recommend_playlist_label)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_17)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.recommend_playlist_scroll_area = QScrollArea(recommend_playlist)
        self.recommend_playlist_scroll_area.setObjectName(u"recommend_playlist_scroll_area")
        self.recommend_playlist_scroll_area.setStyleSheet(u"")
        self.recommend_playlist_scroll_area.setFrameShadow(QFrame.Shadow.Sunken)
        self.recommend_playlist_scroll_area.setLineWidth(1)
        self.recommend_playlist_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.recommend_playlist_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1032, 393))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.recommend_playlist_gridLayout = QGridLayout()
        self.recommend_playlist_gridLayout.setObjectName(u"recommend_playlist_gridLayout")
        self.recommend_playlist_gridLayout.setHorizontalSpacing(15)
        self.recommend_playlist_gridLayout.setVerticalSpacing(25)

        self.verticalLayout_14.addLayout(self.recommend_playlist_gridLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 286, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.recommend_playlist_scroll_area.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.recommend_playlist_scroll_area)


        self.retranslateUi(recommend_playlist)

        QMetaObject.connectSlotsByName(recommend_playlist)
    # setupUi

    def retranslateUi(self, recommend_playlist):
        recommend_playlist.setWindowTitle(QCoreApplication.translate("recommend_playlist", u"Form", None))
        self.recommend_playlist_label.setText(QCoreApplication.translate("recommend_playlist", u"\u63a8\u8350\u6b4c\u5355", None))
        self.recommend_playlist_label.setProperty(u"recommend", QCoreApplication.translate("recommend_playlist", u"-1", None))
    # retranslateUi

