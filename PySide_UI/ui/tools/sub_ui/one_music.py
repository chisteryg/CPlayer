# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_music.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from PySide_UI.ui.tools.base.idbutton import IdButton
from PySide_UI.ui.tools.base.idlabel import IdLabel
import resource_rc

class Ui_music(object):
    def setupUi(self, music):
        if not music.objectName():
            music.setObjectName(u"music")
        music.resize(946, 50)
        music.setMinimumSize(QSize(800, 50))
        music.setStyleSheet(u"*{\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	font-size: 16px;\n"
"	font-weight: 700;\n"
"	font-family: \u6977\u4f53;\n"
"	border: none;\n"
"}\n"
"QWidget[music]:hover{\n"
"	background-color: rgba(255, 255, 255, 0.2);\n"
"}\n"
"/*\u5e8f\u53f7\u6807\u7b7e*/\n"
"#cound_lab{\n"
"	font-size: 18px;\n"
"}\n"
"/*\u97f3\u4e50\u540d\u79f0*/\n"
"#music_name_lab{\n"
"	font-size: 20px;\n"
"}\n"
"#music_name_lab:hover{\n"
"	color: #DE76A3;\n"
"}\n"
"/*\u65f6\u957f\u6807\u7b7e*/\n"
"#duration_lab{\n"
"	font-size: 18px;\n"
"}\n"
"/*\u64ad\u653e\u6309\u94ae*/\n"
"#play_music_btn{\n"
"	border-radius: 10px;\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/play.png);\n"
"}\n"
"/*vip\u6309\u94ae*/\n"
"#vip_btn{\n"
"	border-image: url(:/vip/tools/resource/bg/icon/vip/vip_no.png);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
"	border: 2px solid white;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton[music]:hover {\n"
"	margin: 2px;\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(music)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 2, 20, 2)
        self.count_lab = QLabel(music)
        self.count_lab.setObjectName(u"count_lab")
        self.count_lab.setMinimumSize(QSize(50, 30))
        self.count_lab.setMaximumSize(QSize(16777215, 30))
        self.count_lab.setStyleSheet(u"font-size: 18px;")
        self.count_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.count_lab)

        self.vip_btn = QPushButton(music)
        self.vip_btn.setObjectName(u"vip_btn")
        self.vip_btn.setMinimumSize(QSize(25, 25))
        self.vip_btn.setMaximumSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.vip_btn)

        self.img_btn = IdButton(music)
        self.img_btn.setObjectName(u"img_btn")
        self.img_btn.setMinimumSize(QSize(35, 35))
        self.img_btn.setMaximumSize(QSize(35, 35))
        self.img_btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.img_btn)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.music_name_lab = IdLabel(music)
        self.music_name_lab.setObjectName(u"music_name_lab")
        self.music_name_lab.setMinimumSize(QSize(250, 25))
        self.music_name_lab.setStyleSheet(u"")
        self.music_name_lab.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.music_name_lab)

        self.singer_lab = QLabel(music)
        self.singer_lab.setObjectName(u"singer_lab")
        self.singer_lab.setMinimumSize(QSize(250, 20))
        self.singer_lab.setStyleSheet(u"")
        self.singer_lab.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.singer_lab)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(137, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.duration_lab = QLabel(music)
        self.duration_lab.setObjectName(u"duration_lab")
        self.duration_lab.setMinimumSize(QSize(100, 30))
        self.duration_lab.setMaximumSize(QSize(16777215, 30))
        self.duration_lab.setStyleSheet(u"")
        self.duration_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.duration_lab)

        self.horizontalSpacer_2 = QSpacerItem(140, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.play_music_btn = IdButton(music)
        self.play_music_btn.setObjectName(u"play_music_btn")
        self.play_music_btn.setMinimumSize(QSize(35, 35))
        self.play_music_btn.setMaximumSize(QSize(35, 35))
        self.play_music_btn.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.play_music_btn)


        self.retranslateUi(music)

        QMetaObject.connectSlotsByName(music)
    # setupUi

    def retranslateUi(self, music):
        music.setWindowTitle(QCoreApplication.translate("music", u"Form", None))
        music.setProperty(u"musicid", QCoreApplication.translate("music", u"-1", None))
        music.setProperty(u"music", QCoreApplication.translate("music", u"-1", None))
        self.count_lab.setText(QCoreApplication.translate("music", u"01", None))
        self.vip_btn.setText("")
        self.img_btn.setText("")
        self.img_btn.setProperty(u"musicid", QCoreApplication.translate("music", u"-1", None))
        self.music_name_lab.setText(QCoreApplication.translate("music", u"0", None))
        self.singer_lab.setText(QCoreApplication.translate("music", u"0", None))
        self.duration_lab.setText(QCoreApplication.translate("music", u"0", None))
        self.play_music_btn.setText("")
        self.play_music_btn.setProperty(u"musicid", QCoreApplication.translate("music", u"-1", None))
        self.play_music_btn.setProperty(u"music", QCoreApplication.translate("music", u"-1", None))
    # retranslateUi

