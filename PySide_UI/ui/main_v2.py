# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_v2.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

from PySide_UI.ui.tools.base.animatebar import AnimatedBar
from PySide_UI.ui.tools.base.movewidget import MoveWidget
from PySide_UI.ui.tools.base.musictimeslider import MusicTimeSlider
import resource_rc

class Ui_main_music(object):
    def setupUi(self, main_music):
        if not main_music.objectName():
            main_music.setObjectName(u"main_music")
        main_music.resize(1100, 800)
        main_music.setMinimumSize(QSize(1100, 800))
        main_music.setStyleSheet(u"QWidget#main_music{\n"
"	background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #EEAECA, stop: 1 #94BBE9);\n"
"	border-radius: 10px;\n"
"}\n"
"*{\n"
"	background-color: transparent;\n"
"	color: #fff8ea;\n"
"	border: 2px solid white;\n"
"	border: none;\n"
"	font-size: 16px;\n"
"	font-weight: 700;\n"
"	font-family: ZCOOL KuaiLe;\n"
"}\n"
"/*\u6309\u94ae\u52a8\u6548*/\n"
"QPushButton[effect]:hover{\n"
"	color: white;\n"
"	margin: 2px;\n"
"}\n"
"/*\u72b6\u6001\u680f*/\n"
"#move_widget{\n"
"	border: none;\n"
"	border-bottom: 2px solid white;\n"
"}\n"
"\n"
"#username_lab{\n"
"	padding: 3px;\n"
"}\n"
"#user_btn{\n"
"	border-radius: 6px;\n"
"}\n"
"/*\u72b6\u6001\u680f*/\n"
"\n"
"/*\u6b4c\u8bcd\u6eda\u52a8\u754c\u9762*/\n"
"#music_name_lab_3{\n"
"	font-size: 25px;\n"
"	font-weight: 900;\n"
"}\n"
"#artists_lab_3{\n"
"	font-size: 20px;\n"
"	font-weight: 700;\n"
"}\n"
"/*\u6b4c\u8bcd\u6eda\u52a8\u754c\u9762*/\n"
"\n"
"\n"
"/*\u6a21\u5f0f\u6309\u94ae*/\n"
"QPushButton[page]{\n"
"	border: 2px solid white;\n"
"	bord"
                        "er-radius: 15px;\n"
"}\n"
"QPushButton[page]:hover{\n"
"	font-size: 17px;\n"
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #E899BB, stop: 1 #84ACD9);\n"
"	border: none;\n"
"}\n"
"QPushButton[page]:checked{\n"
"	font-size: 17px;\n"
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #E899BB, stop: 1 #84ACD9);\n"
"	border: none;\n"
"}\n"
"/*\u6a21\u5f0f\u6309\u94ae*/\n"
"\n"
"/*tooltop\u63d0\u793a\u6837\u5f0f*/\n"
"QToolTip{\n"
"	border: 1px solid rgb(118, 118, 118);\n"
"	border: none;\n"
"	background-color: #ffffff;\n"
"	background-color: rgba(176, 196, 222, 0.6);\n"
"	border-radius: 4px;\n"
"	color: #E6659D;\n"
"	font-size: 18px;\n"
"}\n"
"\n"
"/*tooltip\u63d0\u793a\u6837\u5f0f*/\n"
"\n"
"/*\u5206\u8d1d\u8fdb\u5ea6\u6761\u6837\u5f0f*/\n"
"QProgressBar{\n"
"	border: none;\n"
"}\n"
"QProgressBar::chunk {\n"
"	border-radius: 3px;\n"
"	background-color: qlineargradient(\n"
"		x1:0, y1:0,\n"
"		x2:0, y2:1,\n"
"		stop:0 rgba(104, 151, 204, 0.2),\n"
"		stop:1 rgba(104, 15"
                        "1, 204, 0.6)\n"
"	);\n"
"\n"
"}\n"
"/*\u5206\u8d1d\u8fdb\u5ea6\u6761\u6837\u5f0f*/\n"
"\n"
"\n"
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
"	background-color: q"
                        "lineargradient(x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #639AD4, stop: 1 #DE76A3);\n"
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
"/*\u63a8\u8350\u9875\u9762\u901a\u7528\u6837\u5f0f*/\n"
"\n"
"\n"
"\n"
"\n"
"/*\u79c1\u4ebafm*/\n"
"#music_name_lab_2{\n"
"	font-size: 25px;\n"
"	font-weight: 900;\n"
"}\n"
"#artists_lab_2{\n"
"	font-size: 18px;\n"
"	font-weight: 700;\n"
"}\n"
"/*\u79c1\u4ebafm*/\n"
"\n"
"/*\u6b4c\u5355\u4fe1\u606f*/\n"
"#list_img_btn{\n"
"	border-radius: 20px;\n"
"}\n"
"#list_count_btn{\n"
"	pa"
                        "dding-left: 10px;\n"
"}\n"
"/*\u6b4c\u5355\u4fe1\u606f*/\n"
"\n"
"/*\u64ad\u653e\u680f*/\n"
"#music_pic_btn{\n"
"	border-radius: 10px;\n"
"}\n"
"#music_name_lab{\n"
"	font-size: 20px;\n"
"}\n"
"#music_name_lab:hover{\n"
"	color: #DE76A3;\n"
"}\n"
"#artists_lab{\n"
"	font-size: 16px;\n"
"	font-weight:700;\n"
"}\n"
"[time]{\n"
"	color: #7BABE3;\n"
"	color: #DE76A3;\n"
"	font-size: 16px;\n"
"}\n"
"/*\u8fdb\u5ea6\u6ed1\u52a8\u6761*/\n"
"QSlider#music_time_slider{\n"
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
""
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
"}\n"
"/*\u97f3\u91cf\u6ed1\u52a8\u6761*/\n"
"QSlider#volume_slider::groove \n"
"{\n"
"	background:white;\n"
"	height:4px;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QSlider#volume_slider::sub-page \n"
"{\n"
"	background-color: #e52d28;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QSlider#volume_slider::add-page \n"
"{\n"
"	background-color: #df9a8d;\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QSlider#volume_slider::handle    \n"
"{\n"
"	height: 8px;  \n"
"	width: 8px;\n"
"	border-radius: 4px;\n"
"	background: #a70000;\n"
"	margin-top: -2px;\n"
"	margin-bottom: -2px;\n"
"}\n"
"QSlider#volume_slider::handle:hover\n"
"{\n"
"	background: white;\n"
"}\n"
"\n"
"/*\u64ad\u653e\u680f*/\n"
"\n"
"\n"
"\n"
"/*\u56fe\u6807*/\n"
"/*\u6807\u9898\u680f*/\n"
"#close_btn{\n"
"	border-image: url(:/title/tools/resource/b"
                        "g/icon/title/clear.png);\n"
"}\n"
"#max_btn{\n"
"	border-image: url(:/title/tools/resource/bg/icon/title/max.png);\n"
"}\n"
"#min_btn{\n"
"	border-image: url(:/title/tools/resource/bg/icon/title/min.png);\n"
"}\n"
"#settings_btn{\n"
"	border-image: url(:/title/tools/resource/bg/icon/title/settings_4.png);\n"
"}\n"
"#like_btn{\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/like_no.png);\n"
"}\n"
"#last_btn{\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/previous.png);\n"
"}\n"
"#play_btn{\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/play.png);\n"
"}\n"
"#next_btn{\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/next.png);\n"
"}\n"
"#order_btn{\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/shuffe_repeat.png);\n"
"}\n"
"#volume_btn{\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/volume_2.png);\n"
"}\n"
"#mini_btn{\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/subpage_1.png);\n"
"}\n"
"#comments_btn{\n"
"	border-image: url(:/play/tools"
                        "/resource/bg/icon/play/comment_1.png);\n"
"}\n"
"#download_btn{\n"
"	border-image: url(:/play/tools/resource/bg/icon/play/download_1.png);\n"
"}\n"
"\n"
"/*\u56fe\u6807*/")
        self.verticalLayout_23 = QVBoxLayout(main_music)
        self.verticalLayout_23.setSpacing(12)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 10)
        self.move_widget = MoveWidget(main_music)
        self.move_widget.setObjectName(u"move_widget")
        self.move_widget.setMinimumSize(QSize(500, 45))
        self.move_widget.setMaximumSize(QSize(16777215, 45))
        self.horizontalLayout = QHBoxLayout(self.move_widget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(15, -1, 15, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.settings_btn = QPushButton(self.move_widget)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(30, 30))
        self.settings_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.settings_btn)

        self.min_btn = QPushButton(self.move_widget)
        self.min_btn.setObjectName(u"min_btn")
        self.min_btn.setMinimumSize(QSize(30, 30))
        self.min_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.min_btn)

        self.max_btn = QPushButton(self.move_widget)
        self.max_btn.setObjectName(u"max_btn")
        self.max_btn.setMinimumSize(QSize(30, 30))
        self.max_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.max_btn)

        self.close_btn = QPushButton(self.move_widget)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMinimumSize(QSize(30, 30))
        self.close_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.close_btn)


        self.verticalLayout_23.addWidget(self.move_widget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.recommend_playlist_btn = QPushButton(main_music)
        self.recommend_playlist_btn.setObjectName(u"recommend_playlist_btn")
        self.recommend_playlist_btn.setMinimumSize(QSize(100, 30))
        self.recommend_playlist_btn.setMaximumSize(QSize(100, 30))
        self.recommend_playlist_btn.setStyleSheet(u"")
        self.recommend_playlist_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.recommend_playlist_btn)

        self.recommend_music_btn = QPushButton(main_music)
        self.recommend_music_btn.setObjectName(u"recommend_music_btn")
        self.recommend_music_btn.setMinimumSize(QSize(100, 30))
        self.recommend_music_btn.setMaximumSize(QSize(100, 30))
        self.recommend_music_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.recommend_music_btn)

        self.search_btn = QPushButton(main_music)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setMinimumSize(QSize(100, 30))
        self.search_btn.setMaximumSize(QSize(100, 30))
        self.search_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.search_btn)

        self.display_playlist_btn = QPushButton(main_music)
        self.display_playlist_btn.setObjectName(u"display_playlist_btn")
        self.display_playlist_btn.setMinimumSize(QSize(100, 30))
        self.display_playlist_btn.setMaximumSize(QSize(100, 30))
        self.display_playlist_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.display_playlist_btn)

        self.play_page_btn = QPushButton(main_music)
        self.play_page_btn.setObjectName(u"play_page_btn")
        self.play_page_btn.setMinimumSize(QSize(100, 30))
        self.play_page_btn.setMaximumSize(QSize(100, 30))
        self.play_page_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.play_page_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_23.addLayout(self.horizontalLayout_3)

        self.main_stacked_widget = QStackedWidget(main_music)
        self.main_stacked_widget.setObjectName(u"main_stacked_widget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.subpage_verticalLayout = QVBoxLayout(self.page)
        self.subpage_verticalLayout.setObjectName(u"subpage_verticalLayout")
        self.recommend_playlist_verticalLayout = QVBoxLayout()
        self.recommend_playlist_verticalLayout.setSpacing(55)
        self.recommend_playlist_verticalLayout.setObjectName(u"recommend_playlist_verticalLayout")

        self.subpage_verticalLayout.addLayout(self.recommend_playlist_verticalLayout)

        self.main_stacked_widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.music_name_lab_2 = QLabel(self.page_2)
        self.music_name_lab_2.setObjectName(u"music_name_lab_2")
        self.music_name_lab_2.setMinimumSize(QSize(0, 40))
        self.music_name_lab_2.setStyleSheet(u"")
        self.music_name_lab_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.music_name_lab_2.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.music_name_lab_2)

        self.artists_lab_2 = QLabel(self.page_2)
        self.artists_lab_2.setObjectName(u"artists_lab_2")
        self.artists_lab_2.setMinimumSize(QSize(100, 30))
        self.artists_lab_2.setMaximumSize(QSize(16777215, 16777215))
        self.artists_lab_2.setStyleSheet(u"")
        self.artists_lab_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.artists_lab_2.setWordWrap(False)

        self.verticalLayout_4.addWidget(self.artists_lab_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.lyric_scroll_area = QScrollArea(self.page_2)
        self.lyric_scroll_area.setObjectName(u"lyric_scroll_area")
        self.lyric_scroll_area.setStyleSheet(u"")
        self.lyric_scroll_area.setFrameShadow(QFrame.Shadow.Sunken)
        self.lyric_scroll_area.setLineWidth(1)
        self.lyric_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.lyric_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1060, 338))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(15, 15, 15, 15)
        self.lyric_vertical_layout = QVBoxLayout()
        self.lyric_vertical_layout.setSpacing(10)
        self.lyric_vertical_layout.setObjectName(u"lyric_vertical_layout")
        self.lyric_vertical_layout.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.lyric_vertical_layout.addItem(self.verticalSpacer_7)


        self.verticalLayout_12.addLayout(self.lyric_vertical_layout)

        self.lyric_scroll_area.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_5.addWidget(self.lyric_scroll_area)

        self.verticalLayout_5.setStretch(1, 1)
        self.main_stacked_widget.addWidget(self.page_2)

        self.verticalLayout_23.addWidget(self.main_stacked_widget)

        self.widget_2 = QWidget(main_music)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(300, 200))
        self.widget_2.setMaximumSize(QSize(16777215, 200))
        self.widget_2.setStyleSheet(u"/*border: 2px solid white;*/")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.db_widget = QWidget(self.widget_2)
        self.db_widget.setObjectName(u"db_widget")
        self.db_widget.setMinimumSize(QSize(0, 60))
        self.horizontalLayout_8 = QHBoxLayout(self.db_widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.db_bar_1 = AnimatedBar(self.db_widget)
        self.db_bar_1.setObjectName(u"db_bar_1")
        self.db_bar_1.setMinimumSize(QSize(8, 0))
        self.db_bar_1.setMaximumSize(QSize(8, 16777215))
        self.db_bar_1.setValue(65)
        self.db_bar_1.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_1)

        self.db_bar_2 = AnimatedBar(self.db_widget)
        self.db_bar_2.setObjectName(u"db_bar_2")
        self.db_bar_2.setMinimumSize(QSize(8, 0))
        self.db_bar_2.setMaximumSize(QSize(8, 16777215))
        self.db_bar_2.setValue(65)
        self.db_bar_2.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_2)

        self.db_bar_3 = AnimatedBar(self.db_widget)
        self.db_bar_3.setObjectName(u"db_bar_3")
        self.db_bar_3.setMinimumSize(QSize(8, 0))
        self.db_bar_3.setMaximumSize(QSize(8, 16777215))
        self.db_bar_3.setValue(65)
        self.db_bar_3.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_3)

        self.db_bar_4 = AnimatedBar(self.db_widget)
        self.db_bar_4.setObjectName(u"db_bar_4")
        self.db_bar_4.setMinimumSize(QSize(8, 0))
        self.db_bar_4.setMaximumSize(QSize(8, 16777215))
        self.db_bar_4.setValue(65)
        self.db_bar_4.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_4)

        self.db_bar_5 = AnimatedBar(self.db_widget)
        self.db_bar_5.setObjectName(u"db_bar_5")
        self.db_bar_5.setMinimumSize(QSize(8, 0))
        self.db_bar_5.setMaximumSize(QSize(8, 16777215))
        self.db_bar_5.setValue(65)
        self.db_bar_5.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_5)

        self.db_bar_6 = AnimatedBar(self.db_widget)
        self.db_bar_6.setObjectName(u"db_bar_6")
        self.db_bar_6.setMinimumSize(QSize(8, 0))
        self.db_bar_6.setMaximumSize(QSize(8, 16777215))
        self.db_bar_6.setValue(65)
        self.db_bar_6.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_6)

        self.db_bar_7 = AnimatedBar(self.db_widget)
        self.db_bar_7.setObjectName(u"db_bar_7")
        self.db_bar_7.setMinimumSize(QSize(8, 0))
        self.db_bar_7.setMaximumSize(QSize(8, 16777215))
        self.db_bar_7.setValue(65)
        self.db_bar_7.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_7)

        self.db_bar_8 = AnimatedBar(self.db_widget)
        self.db_bar_8.setObjectName(u"db_bar_8")
        self.db_bar_8.setMinimumSize(QSize(8, 0))
        self.db_bar_8.setMaximumSize(QSize(8, 16777215))
        self.db_bar_8.setValue(65)
        self.db_bar_8.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_8)

        self.db_bar_9 = AnimatedBar(self.db_widget)
        self.db_bar_9.setObjectName(u"db_bar_9")
        self.db_bar_9.setMinimumSize(QSize(8, 0))
        self.db_bar_9.setMaximumSize(QSize(8, 16777215))
        self.db_bar_9.setValue(65)
        self.db_bar_9.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_9)

        self.db_bar_10 = AnimatedBar(self.db_widget)
        self.db_bar_10.setObjectName(u"db_bar_10")
        self.db_bar_10.setMinimumSize(QSize(8, 0))
        self.db_bar_10.setMaximumSize(QSize(8, 16777215))
        self.db_bar_10.setValue(65)
        self.db_bar_10.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_10)

        self.db_bar_11 = AnimatedBar(self.db_widget)
        self.db_bar_11.setObjectName(u"db_bar_11")
        self.db_bar_11.setMinimumSize(QSize(8, 0))
        self.db_bar_11.setMaximumSize(QSize(8, 16777215))
        self.db_bar_11.setValue(65)
        self.db_bar_11.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_11)

        self.db_bar_12 = AnimatedBar(self.db_widget)
        self.db_bar_12.setObjectName(u"db_bar_12")
        self.db_bar_12.setMinimumSize(QSize(8, 0))
        self.db_bar_12.setMaximumSize(QSize(8, 16777215))
        self.db_bar_12.setValue(65)
        self.db_bar_12.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_12)

        self.db_bar_13 = AnimatedBar(self.db_widget)
        self.db_bar_13.setObjectName(u"db_bar_13")
        self.db_bar_13.setMinimumSize(QSize(8, 0))
        self.db_bar_13.setMaximumSize(QSize(8, 16777215))
        self.db_bar_13.setValue(65)
        self.db_bar_13.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_13)

        self.db_bar_14 = AnimatedBar(self.db_widget)
        self.db_bar_14.setObjectName(u"db_bar_14")
        self.db_bar_14.setMinimumSize(QSize(8, 0))
        self.db_bar_14.setMaximumSize(QSize(8, 16777215))
        self.db_bar_14.setValue(65)
        self.db_bar_14.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_14)

        self.db_bar_15 = AnimatedBar(self.db_widget)
        self.db_bar_15.setObjectName(u"db_bar_15")
        self.db_bar_15.setMinimumSize(QSize(8, 0))
        self.db_bar_15.setMaximumSize(QSize(8, 16777215))
        self.db_bar_15.setValue(65)
        self.db_bar_15.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_15)

        self.db_bar_16 = AnimatedBar(self.db_widget)
        self.db_bar_16.setObjectName(u"db_bar_16")
        self.db_bar_16.setMinimumSize(QSize(8, 0))
        self.db_bar_16.setMaximumSize(QSize(8, 16777215))
        self.db_bar_16.setValue(65)
        self.db_bar_16.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_16)

        self.db_bar_17 = AnimatedBar(self.db_widget)
        self.db_bar_17.setObjectName(u"db_bar_17")
        self.db_bar_17.setMinimumSize(QSize(8, 0))
        self.db_bar_17.setMaximumSize(QSize(8, 16777215))
        self.db_bar_17.setValue(65)
        self.db_bar_17.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_17)

        self.db_bar_18 = AnimatedBar(self.db_widget)
        self.db_bar_18.setObjectName(u"db_bar_18")
        self.db_bar_18.setMinimumSize(QSize(8, 0))
        self.db_bar_18.setMaximumSize(QSize(8, 16777215))
        self.db_bar_18.setValue(65)
        self.db_bar_18.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_18)

        self.db_bar_19 = AnimatedBar(self.db_widget)
        self.db_bar_19.setObjectName(u"db_bar_19")
        self.db_bar_19.setMinimumSize(QSize(8, 0))
        self.db_bar_19.setMaximumSize(QSize(8, 16777215))
        self.db_bar_19.setValue(65)
        self.db_bar_19.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_19)

        self.db_bar_20 = AnimatedBar(self.db_widget)
        self.db_bar_20.setObjectName(u"db_bar_20")
        self.db_bar_20.setMinimumSize(QSize(8, 0))
        self.db_bar_20.setMaximumSize(QSize(8, 16777215))
        self.db_bar_20.setValue(65)
        self.db_bar_20.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_20)

        self.db_bar_21 = AnimatedBar(self.db_widget)
        self.db_bar_21.setObjectName(u"db_bar_21")
        self.db_bar_21.setMinimumSize(QSize(8, 0))
        self.db_bar_21.setMaximumSize(QSize(8, 16777215))
        self.db_bar_21.setValue(65)
        self.db_bar_21.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_21)

        self.db_bar_22 = AnimatedBar(self.db_widget)
        self.db_bar_22.setObjectName(u"db_bar_22")
        self.db_bar_22.setMinimumSize(QSize(8, 0))
        self.db_bar_22.setMaximumSize(QSize(8, 16777215))
        self.db_bar_22.setValue(65)
        self.db_bar_22.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_22)

        self.db_bar_23 = AnimatedBar(self.db_widget)
        self.db_bar_23.setObjectName(u"db_bar_23")
        self.db_bar_23.setMinimumSize(QSize(8, 0))
        self.db_bar_23.setMaximumSize(QSize(8, 16777215))
        self.db_bar_23.setValue(65)
        self.db_bar_23.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_23)

        self.db_bar_24 = AnimatedBar(self.db_widget)
        self.db_bar_24.setObjectName(u"db_bar_24")
        self.db_bar_24.setMinimumSize(QSize(8, 0))
        self.db_bar_24.setMaximumSize(QSize(8, 16777215))
        self.db_bar_24.setValue(65)
        self.db_bar_24.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_24)

        self.db_bar_25 = AnimatedBar(self.db_widget)
        self.db_bar_25.setObjectName(u"db_bar_25")
        self.db_bar_25.setMinimumSize(QSize(8, 0))
        self.db_bar_25.setMaximumSize(QSize(8, 16777215))
        self.db_bar_25.setValue(65)
        self.db_bar_25.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_25)

        self.db_bar_26 = AnimatedBar(self.db_widget)
        self.db_bar_26.setObjectName(u"db_bar_26")
        self.db_bar_26.setMinimumSize(QSize(8, 0))
        self.db_bar_26.setMaximumSize(QSize(8, 16777215))
        self.db_bar_26.setValue(65)
        self.db_bar_26.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_26)

        self.db_bar_27 = AnimatedBar(self.db_widget)
        self.db_bar_27.setObjectName(u"db_bar_27")
        self.db_bar_27.setMinimumSize(QSize(8, 0))
        self.db_bar_27.setMaximumSize(QSize(8, 16777215))
        self.db_bar_27.setValue(65)
        self.db_bar_27.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_27)

        self.db_bar_28 = AnimatedBar(self.db_widget)
        self.db_bar_28.setObjectName(u"db_bar_28")
        self.db_bar_28.setMinimumSize(QSize(8, 0))
        self.db_bar_28.setMaximumSize(QSize(8, 16777215))
        self.db_bar_28.setValue(65)
        self.db_bar_28.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_28)

        self.db_bar_29 = AnimatedBar(self.db_widget)
        self.db_bar_29.setObjectName(u"db_bar_29")
        self.db_bar_29.setMinimumSize(QSize(8, 0))
        self.db_bar_29.setMaximumSize(QSize(8, 16777215))
        self.db_bar_29.setValue(65)
        self.db_bar_29.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_29)

        self.db_bar_30 = AnimatedBar(self.db_widget)
        self.db_bar_30.setObjectName(u"db_bar_30")
        self.db_bar_30.setMinimumSize(QSize(8, 0))
        self.db_bar_30.setMaximumSize(QSize(8, 16777215))
        self.db_bar_30.setValue(65)
        self.db_bar_30.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_30)

        self.db_bar_31 = AnimatedBar(self.db_widget)
        self.db_bar_31.setObjectName(u"db_bar_31")
        self.db_bar_31.setMinimumSize(QSize(8, 0))
        self.db_bar_31.setMaximumSize(QSize(8, 16777215))
        self.db_bar_31.setValue(65)
        self.db_bar_31.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_31)

        self.db_bar_32 = AnimatedBar(self.db_widget)
        self.db_bar_32.setObjectName(u"db_bar_32")
        self.db_bar_32.setMinimumSize(QSize(8, 0))
        self.db_bar_32.setMaximumSize(QSize(8, 16777215))
        self.db_bar_32.setValue(65)
        self.db_bar_32.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_32)

        self.db_bar_33 = AnimatedBar(self.db_widget)
        self.db_bar_33.setObjectName(u"db_bar_33")
        self.db_bar_33.setMinimumSize(QSize(8, 0))
        self.db_bar_33.setMaximumSize(QSize(8, 16777215))
        self.db_bar_33.setValue(65)
        self.db_bar_33.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_33)

        self.db_bar_34 = AnimatedBar(self.db_widget)
        self.db_bar_34.setObjectName(u"db_bar_34")
        self.db_bar_34.setMinimumSize(QSize(8, 0))
        self.db_bar_34.setMaximumSize(QSize(8, 16777215))
        self.db_bar_34.setValue(65)
        self.db_bar_34.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_34)

        self.db_bar_35 = AnimatedBar(self.db_widget)
        self.db_bar_35.setObjectName(u"db_bar_35")
        self.db_bar_35.setMinimumSize(QSize(8, 0))
        self.db_bar_35.setMaximumSize(QSize(8, 16777215))
        self.db_bar_35.setValue(65)
        self.db_bar_35.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_35)

        self.db_bar_36 = AnimatedBar(self.db_widget)
        self.db_bar_36.setObjectName(u"db_bar_36")
        self.db_bar_36.setMinimumSize(QSize(8, 0))
        self.db_bar_36.setMaximumSize(QSize(8, 16777215))
        self.db_bar_36.setValue(65)
        self.db_bar_36.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_36)

        self.db_bar_37 = AnimatedBar(self.db_widget)
        self.db_bar_37.setObjectName(u"db_bar_37")
        self.db_bar_37.setMinimumSize(QSize(8, 0))
        self.db_bar_37.setMaximumSize(QSize(8, 16777215))
        self.db_bar_37.setValue(65)
        self.db_bar_37.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_37)

        self.db_bar_38 = AnimatedBar(self.db_widget)
        self.db_bar_38.setObjectName(u"db_bar_38")
        self.db_bar_38.setMinimumSize(QSize(8, 0))
        self.db_bar_38.setMaximumSize(QSize(8, 16777215))
        self.db_bar_38.setValue(65)
        self.db_bar_38.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_38)

        self.db_bar_39 = AnimatedBar(self.db_widget)
        self.db_bar_39.setObjectName(u"db_bar_39")
        self.db_bar_39.setMinimumSize(QSize(8, 0))
        self.db_bar_39.setMaximumSize(QSize(8, 16777215))
        self.db_bar_39.setValue(65)
        self.db_bar_39.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_39)

        self.db_bar_40 = AnimatedBar(self.db_widget)
        self.db_bar_40.setObjectName(u"db_bar_40")
        self.db_bar_40.setMinimumSize(QSize(8, 0))
        self.db_bar_40.setMaximumSize(QSize(8, 16777215))
        self.db_bar_40.setValue(65)
        self.db_bar_40.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_40)

        self.db_bar_41 = AnimatedBar(self.db_widget)
        self.db_bar_41.setObjectName(u"db_bar_41")
        self.db_bar_41.setMinimumSize(QSize(8, 0))
        self.db_bar_41.setMaximumSize(QSize(8, 16777215))
        self.db_bar_41.setValue(65)
        self.db_bar_41.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_41)

        self.db_bar_42 = AnimatedBar(self.db_widget)
        self.db_bar_42.setObjectName(u"db_bar_42")
        self.db_bar_42.setMinimumSize(QSize(8, 0))
        self.db_bar_42.setMaximumSize(QSize(8, 16777215))
        self.db_bar_42.setValue(65)
        self.db_bar_42.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_42)

        self.db_bar_43 = AnimatedBar(self.db_widget)
        self.db_bar_43.setObjectName(u"db_bar_43")
        self.db_bar_43.setMinimumSize(QSize(8, 0))
        self.db_bar_43.setMaximumSize(QSize(8, 16777215))
        self.db_bar_43.setValue(65)
        self.db_bar_43.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_43)

        self.db_bar_44 = AnimatedBar(self.db_widget)
        self.db_bar_44.setObjectName(u"db_bar_44")
        self.db_bar_44.setMinimumSize(QSize(8, 0))
        self.db_bar_44.setMaximumSize(QSize(8, 16777215))
        self.db_bar_44.setValue(65)
        self.db_bar_44.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_44)

        self.db_bar_45 = AnimatedBar(self.db_widget)
        self.db_bar_45.setObjectName(u"db_bar_45")
        self.db_bar_45.setMinimumSize(QSize(8, 0))
        self.db_bar_45.setMaximumSize(QSize(8, 16777215))
        self.db_bar_45.setValue(65)
        self.db_bar_45.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_45)

        self.db_bar_46 = AnimatedBar(self.db_widget)
        self.db_bar_46.setObjectName(u"db_bar_46")
        self.db_bar_46.setMinimumSize(QSize(8, 0))
        self.db_bar_46.setMaximumSize(QSize(8, 16777215))
        self.db_bar_46.setValue(65)
        self.db_bar_46.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_46)

        self.db_bar_47 = AnimatedBar(self.db_widget)
        self.db_bar_47.setObjectName(u"db_bar_47")
        self.db_bar_47.setMinimumSize(QSize(8, 0))
        self.db_bar_47.setMaximumSize(QSize(8, 16777215))
        self.db_bar_47.setValue(65)
        self.db_bar_47.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_47)

        self.db_bar_48 = AnimatedBar(self.db_widget)
        self.db_bar_48.setObjectName(u"db_bar_48")
        self.db_bar_48.setMinimumSize(QSize(8, 0))
        self.db_bar_48.setMaximumSize(QSize(8, 16777215))
        self.db_bar_48.setValue(65)
        self.db_bar_48.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_48)

        self.db_bar_49 = AnimatedBar(self.db_widget)
        self.db_bar_49.setObjectName(u"db_bar_49")
        self.db_bar_49.setMinimumSize(QSize(8, 0))
        self.db_bar_49.setMaximumSize(QSize(8, 16777215))
        self.db_bar_49.setValue(65)
        self.db_bar_49.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_49)

        self.db_bar_50 = AnimatedBar(self.db_widget)
        self.db_bar_50.setObjectName(u"db_bar_50")
        self.db_bar_50.setMinimumSize(QSize(8, 0))
        self.db_bar_50.setMaximumSize(QSize(8, 16777215))
        self.db_bar_50.setValue(65)
        self.db_bar_50.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_50)

        self.db_bar_51 = AnimatedBar(self.db_widget)
        self.db_bar_51.setObjectName(u"db_bar_51")
        self.db_bar_51.setMinimumSize(QSize(8, 0))
        self.db_bar_51.setMaximumSize(QSize(8, 16777215))
        self.db_bar_51.setValue(65)
        self.db_bar_51.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_51)

        self.db_bar_52 = AnimatedBar(self.db_widget)
        self.db_bar_52.setObjectName(u"db_bar_52")
        self.db_bar_52.setMinimumSize(QSize(8, 0))
        self.db_bar_52.setMaximumSize(QSize(8, 16777215))
        self.db_bar_52.setValue(65)
        self.db_bar_52.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_52)

        self.db_bar_53 = AnimatedBar(self.db_widget)
        self.db_bar_53.setObjectName(u"db_bar_53")
        self.db_bar_53.setMinimumSize(QSize(8, 0))
        self.db_bar_53.setMaximumSize(QSize(8, 16777215))
        self.db_bar_53.setValue(65)
        self.db_bar_53.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_53)

        self.db_bar_54 = AnimatedBar(self.db_widget)
        self.db_bar_54.setObjectName(u"db_bar_54")
        self.db_bar_54.setMinimumSize(QSize(8, 0))
        self.db_bar_54.setMaximumSize(QSize(8, 16777215))
        self.db_bar_54.setValue(65)
        self.db_bar_54.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_54)

        self.db_bar_55 = AnimatedBar(self.db_widget)
        self.db_bar_55.setObjectName(u"db_bar_55")
        self.db_bar_55.setMinimumSize(QSize(8, 0))
        self.db_bar_55.setMaximumSize(QSize(8, 16777215))
        self.db_bar_55.setValue(65)
        self.db_bar_55.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_55)

        self.db_bar_56 = AnimatedBar(self.db_widget)
        self.db_bar_56.setObjectName(u"db_bar_56")
        self.db_bar_56.setMinimumSize(QSize(8, 0))
        self.db_bar_56.setMaximumSize(QSize(8, 16777215))
        self.db_bar_56.setValue(65)
        self.db_bar_56.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_56)

        self.db_bar_57 = AnimatedBar(self.db_widget)
        self.db_bar_57.setObjectName(u"db_bar_57")
        self.db_bar_57.setMinimumSize(QSize(8, 0))
        self.db_bar_57.setMaximumSize(QSize(8, 16777215))
        self.db_bar_57.setValue(65)
        self.db_bar_57.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_57)

        self.db_bar_58 = AnimatedBar(self.db_widget)
        self.db_bar_58.setObjectName(u"db_bar_58")
        self.db_bar_58.setMinimumSize(QSize(8, 0))
        self.db_bar_58.setMaximumSize(QSize(8, 16777215))
        self.db_bar_58.setValue(65)
        self.db_bar_58.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_58)

        self.db_bar_59 = AnimatedBar(self.db_widget)
        self.db_bar_59.setObjectName(u"db_bar_59")
        self.db_bar_59.setMinimumSize(QSize(8, 0))
        self.db_bar_59.setMaximumSize(QSize(8, 16777215))
        self.db_bar_59.setValue(65)
        self.db_bar_59.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_59)

        self.db_bar_60 = AnimatedBar(self.db_widget)
        self.db_bar_60.setObjectName(u"db_bar_60")
        self.db_bar_60.setMinimumSize(QSize(8, 0))
        self.db_bar_60.setMaximumSize(QSize(8, 16777215))
        self.db_bar_60.setValue(65)
        self.db_bar_60.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_60)

        self.db_bar_61 = AnimatedBar(self.db_widget)
        self.db_bar_61.setObjectName(u"db_bar_61")
        self.db_bar_61.setMinimumSize(QSize(8, 0))
        self.db_bar_61.setMaximumSize(QSize(8, 16777215))
        self.db_bar_61.setValue(65)
        self.db_bar_61.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_61)

        self.db_bar_62 = AnimatedBar(self.db_widget)
        self.db_bar_62.setObjectName(u"db_bar_62")
        self.db_bar_62.setMinimumSize(QSize(8, 0))
        self.db_bar_62.setMaximumSize(QSize(8, 16777215))
        self.db_bar_62.setValue(65)
        self.db_bar_62.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_62)

        self.db_bar_63 = AnimatedBar(self.db_widget)
        self.db_bar_63.setObjectName(u"db_bar_63")
        self.db_bar_63.setMinimumSize(QSize(8, 0))
        self.db_bar_63.setMaximumSize(QSize(8, 16777215))
        self.db_bar_63.setValue(65)
        self.db_bar_63.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_63)

        self.db_bar_64 = AnimatedBar(self.db_widget)
        self.db_bar_64.setObjectName(u"db_bar_64")
        self.db_bar_64.setMinimumSize(QSize(8, 0))
        self.db_bar_64.setMaximumSize(QSize(8, 16777215))
        self.db_bar_64.setValue(65)
        self.db_bar_64.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_64)

        self.db_bar_65 = AnimatedBar(self.db_widget)
        self.db_bar_65.setObjectName(u"db_bar_65")
        self.db_bar_65.setMinimumSize(QSize(8, 0))
        self.db_bar_65.setMaximumSize(QSize(8, 16777215))
        self.db_bar_65.setValue(65)
        self.db_bar_65.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_65)

        self.db_bar_66 = AnimatedBar(self.db_widget)
        self.db_bar_66.setObjectName(u"db_bar_66")
        self.db_bar_66.setMinimumSize(QSize(8, 0))
        self.db_bar_66.setMaximumSize(QSize(8, 16777215))
        self.db_bar_66.setValue(65)
        self.db_bar_66.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_66)

        self.db_bar_67 = AnimatedBar(self.db_widget)
        self.db_bar_67.setObjectName(u"db_bar_67")
        self.db_bar_67.setMinimumSize(QSize(8, 0))
        self.db_bar_67.setMaximumSize(QSize(8, 16777215))
        self.db_bar_67.setValue(65)
        self.db_bar_67.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_67)

        self.db_bar_68 = AnimatedBar(self.db_widget)
        self.db_bar_68.setObjectName(u"db_bar_68")
        self.db_bar_68.setMinimumSize(QSize(8, 0))
        self.db_bar_68.setMaximumSize(QSize(8, 16777215))
        self.db_bar_68.setValue(65)
        self.db_bar_68.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_68)

        self.db_bar_69 = AnimatedBar(self.db_widget)
        self.db_bar_69.setObjectName(u"db_bar_69")
        self.db_bar_69.setMinimumSize(QSize(8, 0))
        self.db_bar_69.setMaximumSize(QSize(8, 16777215))
        self.db_bar_69.setValue(65)
        self.db_bar_69.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_69)

        self.db_bar_70 = AnimatedBar(self.db_widget)
        self.db_bar_70.setObjectName(u"db_bar_70")
        self.db_bar_70.setMinimumSize(QSize(8, 0))
        self.db_bar_70.setMaximumSize(QSize(8, 16777215))
        self.db_bar_70.setValue(65)
        self.db_bar_70.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_8.addWidget(self.db_bar_70)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)


        self.verticalLayout.addWidget(self.db_widget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(10, 10, 10, 10)
        self.music_pic_btn = QPushButton(self.widget_2)
        self.music_pic_btn.setObjectName(u"music_pic_btn")
        self.music_pic_btn.setMinimumSize(QSize(50, 50))
        self.music_pic_btn.setMaximumSize(QSize(50, 50))
        self.music_pic_btn.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.music_pic_btn)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_15)

        self.music_name_lab = QLabel(self.widget_2)
        self.music_name_lab.setObjectName(u"music_name_lab")
        self.music_name_lab.setMinimumSize(QSize(200, 30))
        self.music_name_lab.setMaximumSize(QSize(200, 30))
        self.music_name_lab.setStyleSheet(u"")
        self.music_name_lab.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.music_name_lab)

        self.artists_lab = QLabel(self.widget_2)
        self.artists_lab.setObjectName(u"artists_lab")
        self.artists_lab.setMinimumSize(QSize(200, 30))
        self.artists_lab.setMaximumSize(QSize(200, 30))
        self.artists_lab.setStyleSheet(u"")
        self.artists_lab.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.artists_lab)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_16)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.like_btn = QPushButton(self.widget_2)
        self.like_btn.setObjectName(u"like_btn")
        self.like_btn.setMinimumSize(QSize(40, 40))
        self.like_btn.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.like_btn)

        self.last_btn = QPushButton(self.widget_2)
        self.last_btn.setObjectName(u"last_btn")
        self.last_btn.setMinimumSize(QSize(50, 50))
        self.last_btn.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.last_btn)

        self.play_btn = QPushButton(self.widget_2)
        self.play_btn.setObjectName(u"play_btn")
        self.play_btn.setMinimumSize(QSize(50, 50))
        self.play_btn.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.play_btn)

        self.next_btn = QPushButton(self.widget_2)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setMinimumSize(QSize(50, 50))
        self.next_btn.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.next_btn)

        self.order_btn = QPushButton(self.widget_2)
        self.order_btn.setObjectName(u"order_btn")
        self.order_btn.setMinimumSize(QSize(40, 40))
        self.order_btn.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.order_btn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.now_time_lab = QLabel(self.widget_2)
        self.now_time_lab.setObjectName(u"now_time_lab")
        self.now_time_lab.setMinimumSize(QSize(90, 30))
        self.now_time_lab.setMaximumSize(QSize(16777215, 30))
        self.now_time_lab.setStyleSheet(u"")
        self.now_time_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.now_time_lab)

        self.music_time_slider = MusicTimeSlider(self.widget_2)
        self.music_time_slider.setObjectName(u"music_time_slider")
        self.music_time_slider.setMinimumSize(QSize(150, 0))
        self.music_time_slider.setMaximumSize(QSize(16777215, 16777215))
        self.music_time_slider.setStyleSheet(u"")
        self.music_time_slider.setValue(0)
        self.music_time_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_9.addWidget(self.music_time_slider)

        self.all_time_lab = QLabel(self.widget_2)
        self.all_time_lab.setObjectName(u"all_time_lab")
        self.all_time_lab.setMinimumSize(QSize(90, 30))
        self.all_time_lab.setMaximumSize(QSize(16777215, 30))
        self.all_time_lab.setStyleSheet(u"")
        self.all_time_lab.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.all_time_lab)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.volume_btn = QPushButton(self.widget_2)
        self.volume_btn.setObjectName(u"volume_btn")
        self.volume_btn.setMinimumSize(QSize(35, 35))
        self.volume_btn.setMaximumSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.volume_btn)

        self.volume_slider = QSlider(self.widget_2)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setMinimumSize(QSize(100, 0))
        self.volume_slider.setMaximumSize(QSize(100, 16777215))
        self.volume_slider.setStyleSheet(u"")
        self.volume_slider.setMaximum(100)
        self.volume_slider.setValue(75)
        self.volume_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_7.addWidget(self.volume_slider)

        self.mini_btn = QPushButton(self.widget_2)
        self.mini_btn.setObjectName(u"mini_btn")
        self.mini_btn.setMinimumSize(QSize(30, 30))
        self.mini_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.mini_btn)

        self.download_btn = QPushButton(self.widget_2)
        self.download_btn.setObjectName(u"download_btn")
        self.download_btn.setMinimumSize(QSize(30, 30))
        self.download_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.download_btn)

        self.comments_btn = QPushButton(self.widget_2)
        self.comments_btn.setObjectName(u"comments_btn")
        self.comments_btn.setMinimumSize(QSize(30, 30))
        self.comments_btn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.comments_btn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_23.addWidget(self.widget_2)

        self.verticalLayout_23.setStretch(2, 1)

        self.retranslateUi(main_music)
        self.min_btn.clicked.connect(main_music.showMinimized)
        self.close_btn.clicked.connect(main_music.close)

        self.main_stacked_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(main_music)
    # setupUi

    def retranslateUi(self, main_music):
        main_music.setWindowTitle(QCoreApplication.translate("main_music", u"Form", None))
        self.settings_btn.setText("")
        self.settings_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
        self.min_btn.setText("")
        self.min_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
        self.max_btn.setText("")
        self.max_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
        self.close_btn.setText("")
        self.close_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
        self.recommend_playlist_btn.setText(QCoreApplication.translate("main_music", u"\u6bcf\u65e5\u6b4c\u5355", None))
        self.recommend_playlist_btn.setProperty("page", QCoreApplication.translate("main_music", u"0", None))
        self.recommend_music_btn.setText(QCoreApplication.translate("main_music", u"\u6bcf\u65e5\u63a8\u8350", None))
        self.recommend_music_btn.setProperty("page", QCoreApplication.translate("main_music", u"1", None))
        self.search_btn.setText(QCoreApplication.translate("main_music", u"\u641c\u7d22", None))
        self.search_btn.setProperty("page", QCoreApplication.translate("main_music", u"4", None))
        self.display_playlist_btn.setText(QCoreApplication.translate("main_music", u"\u6b4c\u5355", None))
        self.display_playlist_btn.setProperty("page", QCoreApplication.translate("main_music", u"-1", None))
        self.play_page_btn.setText(QCoreApplication.translate("main_music", u"\u64ad\u653e\u9875", None))
        self.play_page_btn.setProperty("page", QCoreApplication.translate("main_music", u"-1", None))
        self.music_name_lab_2.setText(QCoreApplication.translate("main_music", u"\u6b4c\u540d", None))
        self.artists_lab_2.setText(QCoreApplication.translate("main_music", u"\u6b4c\u624b", None))
        self.db_bar_1.setFormat("")
        self.db_bar_2.setFormat("")
        self.db_bar_3.setFormat("")
        self.db_bar_4.setFormat("")
        self.db_bar_5.setFormat("")
        self.db_bar_6.setFormat("")
        self.db_bar_7.setFormat("")
        self.db_bar_8.setFormat("")
        self.db_bar_9.setFormat("")
        self.db_bar_10.setFormat("")
        self.db_bar_11.setFormat("")
        self.db_bar_12.setFormat("")
        self.db_bar_13.setFormat("")
        self.db_bar_14.setFormat("")
        self.db_bar_15.setFormat("")
        self.db_bar_16.setFormat("")
        self.db_bar_17.setFormat("")
        self.db_bar_18.setFormat("")
        self.db_bar_19.setFormat("")
        self.db_bar_20.setFormat("")
        self.db_bar_21.setFormat("")
        self.db_bar_22.setFormat("")
        self.db_bar_23.setFormat("")
        self.db_bar_24.setFormat("")
        self.db_bar_25.setFormat("")
        self.db_bar_26.setFormat("")
        self.db_bar_27.setFormat("")
        self.db_bar_28.setFormat("")
        self.db_bar_29.setFormat("")
        self.db_bar_30.setFormat("")
        self.db_bar_31.setFormat("")
        self.db_bar_32.setFormat("")
        self.db_bar_33.setFormat("")
        self.db_bar_34.setFormat("")
        self.db_bar_35.setFormat("")
        self.db_bar_36.setFormat("")
        self.db_bar_37.setFormat("")
        self.db_bar_38.setFormat("")
        self.db_bar_39.setFormat("")
        self.db_bar_40.setFormat("")
        self.db_bar_41.setFormat("")
        self.db_bar_42.setFormat("")
        self.db_bar_43.setFormat("")
        self.db_bar_44.setFormat("")
        self.db_bar_45.setFormat("")
        self.db_bar_46.setFormat("")
        self.db_bar_47.setFormat("")
        self.db_bar_48.setFormat("")
        self.db_bar_49.setFormat("")
        self.db_bar_50.setFormat("")
        self.db_bar_51.setFormat("")
        self.db_bar_52.setFormat("")
        self.db_bar_53.setFormat("")
        self.db_bar_54.setFormat("")
        self.db_bar_55.setFormat("")
        self.db_bar_56.setFormat("")
        self.db_bar_57.setFormat("")
        self.db_bar_58.setFormat("")
        self.db_bar_59.setFormat("")
        self.db_bar_60.setFormat("")
        self.db_bar_61.setFormat("")
        self.db_bar_62.setFormat("")
        self.db_bar_63.setFormat("")
        self.db_bar_64.setFormat("")
        self.db_bar_65.setFormat("")
        self.db_bar_66.setFormat("")
        self.db_bar_67.setFormat("")
        self.db_bar_68.setFormat("")
        self.db_bar_69.setFormat("")
        self.db_bar_70.setFormat("")
        self.music_pic_btn.setText("")
        self.music_name_lab.setText(QCoreApplication.translate("main_music", u"\u6b4c\u540d", None))
        self.music_name_lab.setProperty("max_length", QCoreApplication.translate("main_music", u"8", None))
        self.artists_lab.setText(QCoreApplication.translate("main_music", u"\u6b4c\u624b", None))
        self.like_btn.setText("")
        self.like_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
        self.last_btn.setText("")
        self.last_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
        self.play_btn.setText("")
        self.play_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
        self.next_btn.setText("")
        self.next_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
        self.order_btn.setText("")
        self.order_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
        self.now_time_lab.setText(QCoreApplication.translate("main_music", u"00:00", None))
        self.now_time_lab.setProperty("time", QCoreApplication.translate("main_music", u"-1", None))
        self.all_time_lab.setText(QCoreApplication.translate("main_music", u"00:00", None))
        self.all_time_lab.setProperty("time", QCoreApplication.translate("main_music", u"-1", None))
        self.volume_btn.setText("")
        self.volume_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
#if QT_CONFIG(tooltip)
        self.mini_btn.setToolTip(QCoreApplication.translate("main_music", u"Mini\u64ad\u653e\u9875\u9762", None))
#endif // QT_CONFIG(tooltip)
        self.mini_btn.setText("")
        self.mini_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
        self.download_btn.setText("")
        self.download_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
        self.comments_btn.setText("")
        self.comments_btn.setProperty("effect", QCoreApplication.translate("main_music", u"-1", None))
    # retranslateUi

