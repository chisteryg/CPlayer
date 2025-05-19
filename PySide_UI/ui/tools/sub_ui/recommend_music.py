# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recommend_music.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_recommend_music(object):
    def setupUi(self, recommend_music):
        if not recommend_music.objectName():
            recommend_music.setObjectName(u"recommend_music")
        recommend_music.resize(1076, 484)
        recommend_music.setMinimumSize(QSize(1076, 484))
        recommend_music.setStyleSheet(u"*{\n"
"	/*background-color: rgba(255, 255, 255, 0.6);*/\n"
"	background-color: transparent;\n"
"	color: #fff8ea;\n"
"	border: 2px solid white;\n"
"	font-size: 16px;\n"
"	font-weight: 700;\n"
"	font-family: ZCOOL KuaiLe;\n"
"}\n"
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
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, sto"
                        "p: 0 #639AD4, stop: 1 #DE76A3);\n"
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
        self.verticalLayout = QVBoxLayout(recommend_music)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(recommend_music)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 40))
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label)

        self.day_lab = QLabel(recommend_music)
        self.day_lab.setObjectName(u"day_lab")
        self.day_lab.setMinimumSize(QSize(70, 20))
        self.day_lab.setStyleSheet(u"")
        self.day_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.day_lab)


        self.horizontalLayout_11.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.recommend_music_scroll_area = QScrollArea(recommend_music)
        self.recommend_music_scroll_area.setObjectName(u"recommend_music_scroll_area")
        self.recommend_music_scroll_area.setStyleSheet(u"")
        self.recommend_music_scroll_area.setFrameShadow(QFrame.Shadow.Sunken)
        self.recommend_music_scroll_area.setLineWidth(1)
        self.recommend_music_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.recommend_music_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1032, 340))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.recommend_music_vertical_layout = QVBoxLayout()
        self.recommend_music_vertical_layout.setSpacing(10)
        self.recommend_music_vertical_layout.setObjectName(u"recommend_music_vertical_layout")
        self.recommend_music_vertical_layout.setContentsMargins(-1, 10, -1, 10)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.recommend_music_vertical_layout.addItem(self.verticalSpacer_4)


        self.verticalLayout_15.addLayout(self.recommend_music_vertical_layout)

        self.recommend_music_scroll_area.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.recommend_music_scroll_area)


        self.retranslateUi(recommend_music)

        QMetaObject.connectSlotsByName(recommend_music)
    # setupUi

    def retranslateUi(self, recommend_music):
        recommend_music.setWindowTitle(QCoreApplication.translate("recommend_music", u"Form", None))
        self.label.setText(QCoreApplication.translate("recommend_music", u"\u6bcf\u65e5\u63a8\u8350\u97f3\u4e50", None))
        self.label.setProperty(u"recommend", QCoreApplication.translate("recommend_music", u"-1", None))
        self.day_lab.setText(QCoreApplication.translate("recommend_music", u"2 / 11", None))
        self.day_lab.setProperty(u"day", QCoreApplication.translate("recommend_music", u"-1", None))
    # retranslateUi

