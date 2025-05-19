# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
    QScrollArea, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

from PySide_UI.ui.tools.base.movewidget import MoveWidget
import resource_rc

class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(600, 500)
        settings.setMinimumSize(QSize(600, 500))
        settings.setMaximumSize(QSize(600, 500))
        settings.setStyleSheet(u"QWidget#settings{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #EEAECA, stop: 1 #94BBE9);\n"
"	border: 2px solid white;\n"
"}\n"
"*{\n"
"	background-color: transparent;\n"
"	color: #fff8ea;\n"
"	/*border: 2px solid white;*/\n"
"	font-size: 16px;\n"
"	font-weight: 700;\n"
"	font-family: ZCOOL KuaiLe;\n"
"}\n"
"\n"
"/*\u6807\u9898*/\n"
"#title_lab{\n"
"	font-size: 18px;\n"
"	color: #CF467F;\n"
"	border: none;\n"
"}\n"
"/*\u6807\u9898*/\n"
"\n"
"/*\u8bbe\u7f6e\u533a\u57df*/\n"
"[title]{\n"
"	color: #CF467F;\n"
"	font-size: 20px;\n"
"	font-weight: 800;\n"
"	border: none;\n"
"}\n"
"[content]{\n"
"	padding-left: 15px;\n"
"	border: none;\n"
"}\n"
"#save_path_lab, #github_lab, #move_widget{\n"
"	border-bottom: 2px solid white;\n"
"}\n"
"/*\u8bbe\u7f6e\u533a\u57df*/\n"
"\n"
"/*cookies\u6587\u672c\u7f16\u8f91\u5668\u683c\u5f0f*/\n"
"#cookies_textEdit{\n"
"	padding: 5px;\n"
"	background-color: transparent;\n"
"	color: #fff8ea;\n"
"	border: 2px solid white;\n"
"	font-size: 18px;\n"
"	font-weight: 7"
                        "00;\n"
"	font-family: ZCOOL KuaiLe;\n"
"}\n"
"/*cookies\u6587\u672c\u7f16\u8f91\u5668\u683c\u5f0f*/\n"
"\n"
"/*\u6eda\u52a8\u533a\u57df*/\n"
"QScrollArea{\n"
"	border: 2px solid white;\n"
"}\n"
"/*\u6eda\u52a8\u533a\u57df*/\n"
"\n"
"/**/\n"
"[content_btn]:hover{\n"
"	margin: 2px;\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	border-radius: 5px;\n"
"}\n"
"/**/\n"
"\n"
"#close_btn:hover{\n"
"	color: white;\n"
"	margin: 2px;\n"
"}\n"
"#close_btn{\n"
"	border-image: url(:/title/tools/resource/bg/icon/title/clear.png);\n"
"}\n"
"#icon_btn{\n"
"	border-image: url(:/title/tools/resource/bg/icon/title/settings_3.png);\n"
"}\n"
"#github_btn{\n"
"	border-image: url(:/link/tools/resource/bg/icon/link/github.png);\n"
"}\n"
"#path_btn{\n"
"	border-image: url(:/link/tools/resource/bg/icon/link/folder.png);\n"
"}\n"
"\n"
"\n"
"/*\u4fdd\u5b58\u53d6\u6d88\u6309\u94ae\u6837\u5f0f*/\n"
"[save]{\n"
"	border: 2px solid white;\n"
"	border-radius: 5px;\n"
"}\n"
"[save]:hover{\n"
"	color: #DE76A3;\n"
"	background-color: rgba("
                        "255, 255, 255, 0.3);\n"
"	margin: 2px;\n"
"}\n"
"[save]:pressed{\n"
"	color: white;\n"
"}\n"
"/*\u4fdd\u5b58\u53d6\u6d88\u6309\u94ae\u6837\u5f0f*/\n"
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
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #639AD4, stop: 1 #DE76A3);\n"
"}\n"
"QScrollBar::handle:hover{\n"
"	/*back"
                        "ground-color: #75ACEB;*/\n"
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
"/*\u5782\u76f4\u6eda\u52a8\u6761\u6837\u5f0f*/")
        self.verticalLayout_2 = QVBoxLayout(settings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.move_widget = MoveWidget(settings)
        self.move_widget.setObjectName(u"move_widget")
        self.move_widget.setMinimumSize(QSize(0, 50))
        self.move_widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.move_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, -1, -1)
        self.icon_btn = QPushButton(self.move_widget)
        self.icon_btn.setObjectName(u"icon_btn")
        self.icon_btn.setMinimumSize(QSize(30, 30))
        self.icon_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.icon_btn)

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
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.scrollArea = QScrollArea(settings)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 566, 705))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 20, 20, -1)
        self.save_path_title_lab = QLabel(self.scrollAreaWidgetContents)
        self.save_path_title_lab.setObjectName(u"save_path_title_lab")
        self.save_path_title_lab.setMinimumSize(QSize(0, 30))
        self.save_path_title_lab.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.save_path_title_lab)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.save_path_lab = QLabel(self.scrollAreaWidgetContents)
        self.save_path_lab.setObjectName(u"save_path_lab")
        self.save_path_lab.setMinimumSize(QSize(0, 35))
        self.save_path_lab.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.save_path_lab)

        self.path_btn = QPushButton(self.scrollAreaWidgetContents)
        self.path_btn.setObjectName(u"path_btn")
        self.path_btn.setMinimumSize(QSize(30, 30))
        self.path_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.path_btn)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_3.setStretch(0, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.cookies_title_lab = QLabel(self.scrollAreaWidgetContents)
        self.cookies_title_lab.setObjectName(u"cookies_title_lab")
        self.cookies_title_lab.setMinimumSize(QSize(0, 30))
        self.cookies_title_lab.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.cookies_title_lab)

        self.cookies_textEdit = QTextEdit(self.scrollAreaWidgetContents)
        self.cookies_textEdit.setObjectName(u"cookies_textEdit")
        self.cookies_textEdit.setMinimumSize(QSize(0, 200))
        self.cookies_textEdit.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.cookies_textEdit)

        self.material_citation_title_lab = QLabel(self.scrollAreaWidgetContents)
        self.material_citation_title_lab.setObjectName(u"material_citation_title_lab")
        self.material_citation_title_lab.setMinimumSize(QSize(0, 30))
        self.material_citation_title_lab.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.material_citation_title_lab)

        self.citation_lab_1 = QLabel(self.scrollAreaWidgetContents)
        self.citation_lab_1.setObjectName(u"citation_lab_1")
        self.citation_lab_1.setMinimumSize(QSize(0, 35))
        self.citation_lab_1.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.citation_lab_1)

        self.citation_lab_2 = QLabel(self.scrollAreaWidgetContents)
        self.citation_lab_2.setObjectName(u"citation_lab_2")
        self.citation_lab_2.setMinimumSize(QSize(0, 35))
        self.citation_lab_2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.citation_lab_2)

        self.save_path_title_lab_4 = QLabel(self.scrollAreaWidgetContents)
        self.save_path_title_lab_4.setObjectName(u"save_path_title_lab_4")
        self.save_path_title_lab_4.setMinimumSize(QSize(0, 30))
        self.save_path_title_lab_4.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.save_path_title_lab_4)

        self.citation_lab_3 = QLabel(self.scrollAreaWidgetContents)
        self.citation_lab_3.setObjectName(u"citation_lab_3")
        self.citation_lab_3.setMinimumSize(QSize(0, 35))
        self.citation_lab_3.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.citation_lab_3)

        self.citation_lab_4 = QLabel(self.scrollAreaWidgetContents)
        self.citation_lab_4.setObjectName(u"citation_lab_4")
        self.citation_lab_4.setMinimumSize(QSize(0, 35))
        self.citation_lab_4.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.citation_lab_4)

        self.github_title_lab = QLabel(self.scrollAreaWidgetContents)
        self.github_title_lab.setObjectName(u"github_title_lab")
        self.github_title_lab.setMinimumSize(QSize(0, 30))
        self.github_title_lab.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.github_title_lab)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.github_lab = QLabel(self.scrollAreaWidgetContents)
        self.github_lab.setObjectName(u"github_lab")
        self.github_lab.setMinimumSize(QSize(0, 35))
        self.github_lab.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.github_lab)

        self.github_btn = QPushButton(self.scrollAreaWidgetContents)
        self.github_btn.setObjectName(u"github_btn")
        self.github_btn.setMinimumSize(QSize(30, 30))
        self.github_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.github_btn)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_4.setStretch(0, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(40)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.save_btn = QPushButton(settings)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(60, 30))
        self.save_btn.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_2.addWidget(self.save_btn)

        self.cancal_btn = QPushButton(settings)
        self.cancal_btn.setObjectName(u"cancal_btn")
        self.cancal_btn.setMinimumSize(QSize(60, 30))
        self.cancal_btn.setMaximumSize(QSize(60, 30))

        self.horizontalLayout_2.addWidget(self.cancal_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalLayout.setStretch(3, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(settings)
        self.close_btn.clicked.connect(settings.close)
        self.cancal_btn.clicked.connect(settings.close)

        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"Form", None))
        self.icon_btn.setText("")
        self.title_lab.setText(QCoreApplication.translate("settings", u"\u8bbe\u7f6e", None))
        self.close_btn.setText("")
        self.save_path_title_lab.setText(QCoreApplication.translate("settings", u"\u97f3\u4e50\u4e0b\u8f7d\u8def\u5f84\uff1a", None))
        self.save_path_title_lab.setProperty(u"title", QCoreApplication.translate("settings", u"-1", None))
        self.save_path_lab.setText(QCoreApplication.translate("settings", u"C:/", None))
        self.save_path_lab.setProperty(u"content", QCoreApplication.translate("settings", u"-1", None))
        self.path_btn.setText("")
        self.path_btn.setProperty(u"content_btn", QCoreApplication.translate("settings", u"-1", None))
        self.cookies_title_lab.setText(QCoreApplication.translate("settings", u"Cookies\uff1a", None))
        self.cookies_title_lab.setProperty(u"title", QCoreApplication.translate("settings", u"-1", None))
        self.cookies_textEdit.setHtml(QCoreApplication.translate("settings", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'ZCOOL KuaiLe'; font-size:18px; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.material_citation_title_lab.setText(QCoreApplication.translate("settings", u"\u7d20\u6750\u5f15\u7528\uff1a", None))
        self.material_citation_title_lab.setProperty(u"title", QCoreApplication.translate("settings", u"-1", None))
        self.citation_lab_1.setText(QCoreApplication.translate("settings", u"\u97f3\u4e50\uff1ahttps://music.163.com/", None))
        self.citation_lab_1.setProperty(u"content", QCoreApplication.translate("settings", u"-1", None))
        self.citation_lab_2.setText(QCoreApplication.translate("settings", u"\u56fe\u6807\uff1ahttps://www.iconfont.cn/", None))
        self.citation_lab_2.setProperty(u"content", QCoreApplication.translate("settings", u"-1", None))
        self.save_path_title_lab_4.setText(QCoreApplication.translate("settings", u"\u7b2c\u4e09\u65b9\u6a21\u5757\u5f15\u7528\uff1a", None))
        self.save_path_title_lab_4.setProperty(u"title", QCoreApplication.translate("settings", u"-1", None))
        self.citation_lab_3.setText(QCoreApplication.translate("settings", u"PySide6\uff1ahttps://pypi.org/project/PySide6/", None))
        self.citation_lab_3.setProperty(u"content", QCoreApplication.translate("settings", u"-1", None))
        self.citation_lab_4.setText(QCoreApplication.translate("settings", u"httpx\uff1ahttps://www.python-httpx.org/", None))
        self.citation_lab_4.setProperty(u"content", QCoreApplication.translate("settings", u"-1", None))
        self.github_title_lab.setText(QCoreApplication.translate("settings", u"github", None))
        self.github_title_lab.setProperty(u"title", QCoreApplication.translate("settings", u"-1", None))
        self.github_lab.setText(QCoreApplication.translate("settings", u"github\uff1ahttps://github.com/chisteryg", None))
        self.github_lab.setProperty(u"content", QCoreApplication.translate("settings", u"-1", None))
        self.github_btn.setText("")
        self.github_btn.setProperty(u"content_btn", QCoreApplication.translate("settings", u"-1", None))
        self.save_btn.setText(QCoreApplication.translate("settings", u"\u4fdd\u5b58", None))
        self.save_btn.setProperty(u"save", QCoreApplication.translate("settings", u"-1", None))
        self.cancal_btn.setText(QCoreApplication.translate("settings", u"\u53d6\u6d88", None))
        self.cancal_btn.setProperty(u"save", QCoreApplication.translate("settings", u"-1", None))
    # retranslateUi

