# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playlist.ui'
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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_playlist(object):
    def setupUi(self, playlist):
        if not playlist.objectName():
            playlist.setObjectName(u"playlist")
        playlist.resize(1076, 484)
        playlist.setMinimumSize(QSize(1076, 484))
        playlist.setStyleSheet(u"*{\n"
"	/*background-color: rgba(255, 255, 255, 0.6);*/\n"
"	background-color: transparent;\n"
"	color: #fff8ea;\n"
"	border: 2px solid white;\n"
"	font-size: 16px;\n"
"	font-weight: 700;\n"
"	font-family: ZCOOL KuaiLe;\n"
"}\n"
"/*\u6b4c\u5355\u56fe\u7247*/\n"
"#list_img_btn{\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"/*\u4e0a\u4e00\u9875\u3001\u4e0b\u4e00\u9875\u6309\u94ae*/\n"
"QPushButton[page]{\n"
"	border: 2px solid #ca8f00;\n"
"	border-radius: 15px;\n"
"}\n"
"QPushButton[page]:hover{\n"
"	font-size: 17px;\n"
"	background-color: #ca8f00;\n"
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
"	padding-"
                        "top: 2px;\n"
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
"	font-weight: 7"
                        "00;\n"
"	font-size: 30px;\n"
"}\n"
"[day]{\n"
"	font-size: 18px;\n"
"}\n"
"/*\u63a8\u8350\u9875\u9762\u901a\u7528\u6837\u5f0f*/\n"
"\n"
"\n"
"#play_list_btn{\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/play.png);\n"
"}\n"
"#collect_playlist_btn{\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/folder_add.png);\n"
"}\n"
"QPushButton[playlist]:hover{\n"
"	margin: 2px;\n"
"	border-radius: 5px;\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"}")
        self.verticalLayout = QVBoxLayout(playlist)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(25)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)

        self.list_img_btn = QPushButton(playlist)
        self.list_img_btn.setObjectName(u"list_img_btn")
        self.list_img_btn.setMinimumSize(QSize(80, 80))
        self.list_img_btn.setMaximumSize(QSize(80, 80))
        self.list_img_btn.setStyleSheet(u"")

        self.horizontalLayout_14.addWidget(self.list_img_btn)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.list_name_lab = QLabel(playlist)
        self.list_name_lab.setObjectName(u"list_name_lab")
        self.list_name_lab.setMinimumSize(QSize(130, 30))
        self.list_name_lab.setStyleSheet(u"")
        self.list_name_lab.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.list_name_lab.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.list_name_lab)


        self.horizontalLayout_14.addLayout(self.verticalLayout_10)


        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.playlist_scroll_area = QScrollArea(playlist)
        self.playlist_scroll_area.setObjectName(u"playlist_scroll_area")
        self.playlist_scroll_area.setStyleSheet(u"")
        self.playlist_scroll_area.setFrameShadow(QFrame.Shadow.Sunken)
        self.playlist_scroll_area.setLineWidth(1)
        self.playlist_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.playlist_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 1032, 343))
        self.verticalLayout_24 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.playlist_verticalLayout = QVBoxLayout()
        self.playlist_verticalLayout.setSpacing(10)
        self.playlist_verticalLayout.setObjectName(u"playlist_verticalLayout")
        self.playlist_verticalLayout.setContentsMargins(-1, 10, -1, 10)
        self.verticalSpacer_5 = QSpacerItem(20, 289, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.playlist_verticalLayout.addItem(self.verticalSpacer_5)


        self.verticalLayout_24.addLayout(self.playlist_verticalLayout)

        self.playlist_scroll_area.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.playlist_scroll_area)


        self.retranslateUi(playlist)

        QMetaObject.connectSlotsByName(playlist)
    # setupUi

    def retranslateUi(self, playlist):
        playlist.setWindowTitle(QCoreApplication.translate("playlist", u"Form", None))
        self.list_img_btn.setText("")
        self.list_name_lab.setText(QCoreApplication.translate("playlist", u"\u672a\u52a0\u8f7d\u6b4c\u5355\uff08x\u9996\uff09", None))
        self.list_name_lab.setProperty(u"recommend", QCoreApplication.translate("playlist", u"-1", None))
    # retranslateUi

