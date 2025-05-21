# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mini_page.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from PySide_UI.ui.tools.base.musictimeslider import MusicTimeSlider
import resource_rc

class Ui_mini_page(object):
    def setupUi(self, mini_page):
        if not mini_page.objectName():
            mini_page.setObjectName(u"mini_page")
        mini_page.resize(450, 200)
        mini_page.setMinimumSize(QSize(450, 200))
        mini_page.setMaximumSize(QSize(450, 200))
        mini_page.setStyleSheet(u"QWidget#settings{\n"
"	background-color: rgba(255,228,196, 0.4);\n"
"}\n"
"*{\n"
"	background-color: transparent;\n"
"	color: #fff8ea;\n"
"	border: none;\n"
"	font-size: 16px;\n"
"	font-weight: 700;\n"
"	font-family: ZCOOL KuaiLe;\n"
"}\n"
"\n"
"/*\u6b4c\u8bcd\u6807\u7b7e*/\n"
"#lrc_lab{\n"
"	color: #CF467F;\n"
"	font-size: 21px;\n"
"	font-weight: 800;\n"
"}\n"
"/*\u65f6\u95f4\u6807\u7b7e*/\n"
"[time]{\n"
"	color: #DE76A3;\n"
"	font-size: 16px;\n"
"}\n"
"/*\u6309\u94ae\u6837\u5f0f*/\n"
"QPushButton:hover{\n"
"	color: white;\n"
"	margin: 2px;\n"
"}\n"
"#close_btn{\n"
"	border-image: url(:/title/tools/resource/bg/icon/title/clear.png);\n"
"}\n"
"#play_btn{\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/play.png);\n"
"}\n"
"/*\u8fdb\u5ea6\u6ed1\u52a8\u6761*/\n"
"QSlider#music_time_slider{\n"
"	padding-top: 2px;\n"
"	margin: 3px;\n"
"}\n"
"QSlider#music_time_slider::groove \n"
"{\n"
"	padding-left: -2px;\n"
"	padding-right: -2px; \n"
"	background:white;\n"
"	height:6px;\n"
"	border-radius: 3px;\n"
"}\n"
""
                        "\n"
"QSlider#music_time_slider::sub-page \n"
"{\n"
"	background-color: #5494DE;\n"
"	background-color: #FF75B1;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QSlider#music_time_slider::add-page \n"
"{\n"
"	background-color: #78AAE3;\n"
"	background-color: #F2A7C6;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QSlider#music_time_slider::handle    \n"
"{\n"
"	height: 10px;  \n"
"	width: 10px;\n"
"	border-radius: 5px;\n"
"	background: #5C89BD;\n"
"	background: #E84D90;\n"
"	margin-top: -2px;\n"
"	margin-bottom: -2px;\n"
"}\n"
"QSlider#music_time_slider::handle:hover\n"
"{\n"
"	background: white;\n"
"}")
        self.verticalLayout = QVBoxLayout(mini_page)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 12)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(288, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_btn = QPushButton(mini_page)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(35, 35))
        self.close_btn.setMaximumSize(QSize(35, 35))

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lrc_lab = QLabel(mini_page)
        self.lrc_lab.setObjectName(u"lrc_lab")
        self.lrc_lab.setMinimumSize(QSize(200, 30))
        self.lrc_lab.setMaximumSize(QSize(16777215, 16777215))
        self.lrc_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lrc_lab.setWordWrap(True)

        self.verticalLayout.addWidget(self.lrc_lab)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.play_btn = QPushButton(mini_page)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setMinimumSize(QSize(35, 35))
        self.play_btn.setMaximumSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.play_btn)

        self.music_time_slider = MusicTimeSlider(mini_page)
        self.music_time_slider.setObjectName(u"music_time_slider")
        self.music_time_slider.setMinimumSize(QSize(150, 0))
        self.music_time_slider.setMaximumSize(QSize(16777215, 16777215))
        self.music_time_slider.setStyleSheet(u"")
        self.music_time_slider.setValue(0)
        self.music_time_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.music_time_slider)

        self.now_time_lab = QLabel(mini_page)
        self.now_time_lab.setObjectName(u"now_time_lab")
        self.now_time_lab.setMinimumSize(QSize(70, 30))
        self.now_time_lab.setMaximumSize(QSize(16777215, 30))
        self.now_time_lab.setStyleSheet(u"")
        self.now_time_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.now_time_lab)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(4, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(mini_page)
        self.close_btn.clicked.connect(mini_page.close)

        QMetaObject.connectSlotsByName(mini_page)
    # setupUi

    def retranslateUi(self, mini_page):
        mini_page.setWindowTitle(QCoreApplication.translate("mini_page", u"Form", None))
        self.close_btn.setText("")
        self.lrc_lab.setText(QCoreApplication.translate("mini_page", u"\u97f3\u4e50\u4e0b\u8f7d\u8def\u5f84\uff1a", None))
        self.lrc_lab.setProperty(u"title", QCoreApplication.translate("mini_page", u"-1", None))
        self.play_btn.setText("")
        self.play_btn.setProperty(u"save", QCoreApplication.translate("mini_page", u"-1", None))
        self.now_time_lab.setText(QCoreApplication.translate("mini_page", u"00:00", None))
        self.now_time_lab.setProperty(u"time", QCoreApplication.translate("mini_page", u"-1", None))
    # retranslateUi

