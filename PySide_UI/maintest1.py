import json
import os
import random

from PySide6.QtGui import Qt, QIcon
from PySide6.QtCore import Slot, QTimer, Qt, QPoint, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import *

from PySide_UI.tools.NeteaseCloudMusic_API.httpx_api_2 import NeteaseCloudMusicAPI
from PySide_UI.tools.player.palyer import MusicPlayer
from PySide_UI.ui import main_v2
from PySide_UI.ui.tools.requester_thread import *
from PySide_UI.ui.tools.sub_page.Message import MessagePage
from PySide_UI.ui.tools.sub_page.MiniPage import MiniPage
from PySide_UI.ui.tools.sub_page.Playlist import PlaylistPage
from PySide_UI.ui.tools.sub_page.RecommendMusic import RecommendMusicPage
from PySide_UI.ui.tools.sub_page.RecommendPlaylist import RecommendPlaylistPage
from PySide_UI.ui.tools.sub_page.SearchPage import SearchPage
from PySide_UI.ui.tools.sub_page.Settings import SettingsPage


class MyForm(QWidget, main_v2.Ui_main_music):
    destored_thread = Signal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        # 设置顶层窗口qwidget样式生效
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowTitle('CPlayer')
        self.show()

        # 加载爬虫模块
        self.cloud = NeteaseCloudMusicAPI()
        # 加载播放模块
        self.player = MusicPlayer(self)
        # 添加按钮组
        self.set_btn_group()
        # 设置字体
        self.loadFont()
        # # 设置全局qss
        # self.set_qss()

        # 音乐信息
        self.data = {
            # 设置内容
            'settings': {
                "cookies": "",
                "save_path": "C:/",
                "repeat": self.repeat_order
            },

            # 计时器
            'timer': QTimer(),  # 定时器对象
            'now': 0,  # 当前时间
            'duration': 0,  # 总时长

            # 音乐播放情况
            'music_list': [],  # 播放列表
            'music_list_type': None,  # 播放类型
            'auto_play_music_list': False,  # 是否自动播放列表
            'music_loaded': False,  # 加载情况
            'music_id': None,  # 当前音乐id
            'play_status': self.stop,  # 当前播放状态
            'music_info': {},
            'lrc': {
                'lyric': [],
                'need_screen': False,
                'last_lyric_index': -1,
            },

            # 推荐歌单
            'recommend_playlist_info': {},  # 歌单信息

            # 推荐音乐加载情况
            'recommend_music_loaded': False,
            'recommend_music_info': {},

            # 搜索音乐加载情况
            'keywords': None,  # 当前搜索的内容
            'search_music_info': {},  # 搜索信息

            # 歌单加载情况
            'playlist_id': None,
            'playlist_info': {},

        }
        # 设置计时器间隔
        self.data['timer'].setInterval(self.interval)
        # 设置精度为毫秒级
        self.data['timer'].setTimerType(Qt.TimerType.PreciseTimer)
        self.data['timer'].timeout.connect(self.add_time)

        # 加载设置

        self.set_settings()

        # 子页面
        self.subpage = None
        self.settings_page = None
        self.mini_page = None
        self.recommend_playlist_btn.click()

        # 子线程
        self.save_thread = None

        # 左下角调整大小方法
        self.setMouseTracking(True)  # 启用鼠标跟踪
        # 按压标志
        self.press_flag = False
        # 鼠标形状改变标志
        self.cursor_shape_flag = False
        # 调整大小标志
        self.resize_flag = False

        return

    def close(self):
        # 退出时保存设置
        self.save_settings()
        super().close()
        return

    def remove_subpage(self):
        # 移除子页面内容
        if self.subpage is not None:
            self.recommend_playlist_verticalLayout.removeWidget(self.subpage)
            self.subpage.deleteLater()
            self.subpage = None
        return

    def enable_ui(self):
        # 恢复ui
        self.main_stacked_widget.setEnabled(True)

    def disable_ui(self):
        # 阻塞ui
        self.main_stacked_widget.setEnabled(False)

    def set_btn_group(self):
        # 添加按钮组
        self.bg = QButtonGroup(self)
        # 设置排他性
        self.bg.setExclusive(True)
        self.bg.addButton(self.recommend_playlist_btn)
        self.bg.addButton(self.recommend_music_btn)
        self.bg.addButton(self.search_btn)
        self.bg.addButton(self.display_playlist_btn)
        self.bg.addButton(self.play_page_btn)

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 每日歌单推荐相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    @Slot()
    def on_recommend_playlist_btn_toggled(self):
        # 每日推荐歌单按钮被点击，加载歌单
        if self.recommend_playlist_btn.isChecked():
            # 如果是选中状态
            # 切换到页面0
            self.main_stacked_widget.setCurrentIndex(0)
            # 首先移除子页面
            self.remove_subpage()
            if self.data['recommend_playlist_info'] == {}:
                # 如果未加载歌单
                # 加载首页歌单
                self.load_recommend_playlist(1)
            else:
                # 如果已加载歌单
                # 获取歌单数据
                playlist_info = {}
                playlist_info['data'] = self.data['recommend_playlist_info']
                # 加载歌单
                self.set_recommend_playlist(playlist_info)
                return
            return

    def load_recommend_playlist(self, page=1):
        if self.data['recommend_playlist_info'] != {}:
            # 已加载过歌单信息
            max_page = self.data['recommend_playlist_info']['max_page']
            if page > max_page:
                # 当前页数超过最大页数，不在加载
                return

        # 加载指定页数的歌单
        self.disable_ui()

        # 启动线程
        self.thread = RecommendPlayList(self.cloud, page=page, count=self.playlist_count, cat='全部')
        self.thread.recommend_playlist_finished.connect(self.set_recommend_playlist)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        return

    def set_recommend_playlist(self, playlist_info):
        # 创建子页面
        if self.subpage is None:
            # 未页面则创建子页面
            self.subpage = RecommendPlaylistPage(self.main_stacked_widget)
            self.recommend_playlist_verticalLayout.addWidget(self.subpage, 0)
            # 歌单被点击信号
            self.subpage.load_playlist_page.connect(self.load_recommend_playlist_page)
            # 滚动到底部，加载歌单
            self.subpage.add_playlists.connect(
                lambda: self.load_recommend_playlist(self.data['recommend_playlist_info']['page'] + 1))
            # 页面加载完毕，恢复主窗口信号
            self.subpage.enable_ui.connect(self.enable_ui)
        playlist_info = playlist_info['data']

        # 设置内容
        self.subpage.add_recommend_playlist(playlist_info)

        # 存储歌单信息
        if self.data['recommend_playlist_info'] == {}:
            # 如果歌单信息未加载
            self.data['recommend_playlist_info'] = playlist_info
        else:
            # 如果歌单信息已加载
            page = str(playlist_info['page'])
            # 将歌单内容增添至data
            self.data['recommend_playlist_info']['playlist'][page] = playlist_info['playlist'][page]
            # 更新页数
            self.data['recommend_playlist_info']['page'] = playlist_info['page']
        return

    def load_recommend_playlist_page(self, playlist_info: dict):
        # 歌单被左击，加载歌单
        self.data['playlist_id'] = playlist_info['list_id']
        self.display_playlist_btn.click()
        return

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 每日歌单推荐相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 每日推荐音乐相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    @Slot()
    def on_recommend_music_btn_clicked(self):
        # 精品歌单按钮被点击，加载歌单
        # 每日推荐歌单按钮被点击，加载歌单
        if self.recommend_music_btn.isChecked():
            # 如果是选中状态

            self.main_stacked_widget.setCurrentIndex(0)
            # 首先移除子页面
            self.remove_subpage()
            self.load_recommend_music()
            return

    def load_recommend_music(self):
        # 加载每日推荐音乐
        self.disable_ui()
        if self.data['recommend_music_info'] != {}:
            # 如果已加载每日推荐音乐
            # 设置页面
            recommend_music = {}
            recommend_music['data'] = self.data['recommend_music_info']
            self.set_recommend_music(recommend_music)
            return

        # 启动下载线程
        self.thread = RecommendMusic(self.cloud)
        self.thread.recommend_music_finished.connect(self.set_recommend_music)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        return

    def set_recommend_music(self, recommend_music: dict):
        # 设置推荐音乐的内容
        # 创建子页面
        if self.subpage is None:
            # 未页面则创建子页面
            self.subpage = RecommendMusicPage(self.main_stacked_widget)
            self.recommend_playlist_verticalLayout.addWidget(self.subpage, 0)
            # 播放信号
            self.subpage.play_recommend_music.connect(self.play_recommend_music)
            # 页面加载完毕，恢复主窗口信号
            self.subpage.enable_ui.connect(self.enable_ui)
        # 设置内容
        recommend_music = recommend_music['data']
        self.subpage.set_recommend_music(recommend_music)

        # 更新页数
        self.data['recommend_music_info'] = recommend_music
        return

    def play_recommend_music(self, music_id: str):
        self.data['auto_play_music_list'] = False
        # 播放推荐音乐
        self.load_music(music_id)
        # 设置当前播放列表为每日推荐
        if self.data['music_list_type'] != self.music_list_recommend:
            # 当前播放列表类型不是推荐音乐
            music_list = []
            for key in self.data['recommend_music_info'].keys():
                music_list.append(self.data['recommend_music_info'][key]['id'])
            self.data['music_list'] = music_list
            self.data['music_list_type'] = self.music_list_recommend
        return

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 每日推荐音乐相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 搜索音乐相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    @Slot()
    def on_search_btn_toggled(self):
        # 搜索按钮被点击，加载歌单
        if self.search_btn.isChecked():
            # 如果是选中状态
            # 切换至页面0
            self.main_stacked_widget.setCurrentIndex(0)
            # 首先移除子页面
            self.remove_subpage()
            # 加载搜索页面
            self.subpage = SearchPage(self.main_stacked_widget)
            self.recommend_playlist_verticalLayout.addWidget(self.subpage, 0)

            # 搜索信号
            self.subpage.search.connect(self.load_search_music)
            # 点击播放按钮
            self.subpage.play_search_music.connect(self.play_search_music)
            # 滚动到底部，继续加载音乐信号
            self.subpage.add_songs.connect(self.add_search_songs)
            # 页面加载完毕，恢复主窗口信号
            self.subpage.enable_ui.connect(self.enable_ui)

            return

    def add_search_songs(self):
        # 搜索音乐加载情况
        keywords = self.data['keywords']
        if keywords != None:
            # 已搜索
            # 当前搜索页数加一
            page = self.data['search_music_info'][keywords]['page'] + 1
            if page <= self.data['search_music_info'][keywords]['max_page']:
                # 当前页数在范围内
                # pprint(keywords)
                # pprint(page)
                # 加载下一页搜索内容
                self.load_search_music(keywords=keywords, page=page)
        return

    def load_search_music(self, keywords: str, page: int = 1):
        # 加载指定页数的搜索内容
        self.disable_ui()

        if keywords in self.data['search_music_info'].keys() and page == 1:
            # 已加载过该关键字且当前需要加载首页
            # 提取内容并加载
            search_music_info = {}
            search_music_info['data'] = self.data['search_music_info'][keywords]
            # pprint(search_music_info)
            self.add_search_music(search_music_info)
            return

        # 启动线程
        self.thread = SearchMusic(self.cloud, keywords=keywords, page=page, count=self.music_count)
        self.thread.search_music_finished.connect(self.add_search_music)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        return

    def add_search_music(self, search_music_info):
        # 添加搜索音乐
        search_music_info = search_music_info['data']
        # 设置内容
        self.subpage.add_search_music(search_music_info)

        # 储存该页歌单信息
        page = str(search_music_info['page'])
        keywords = search_music_info['keywords']
        if keywords in self.data['search_music_info'].keys():
            # 搜索内容已加载，将单页内容添加至data
            self.data['search_music_info'][keywords]['songs_detail'][page] = search_music_info['songs_detail'][page]
            self.data['search_music_info'][keywords]['page'] = search_music_info['page']
        else:
            # 搜索内容未加载，将内容添加至data
            self.data['search_music_info'][keywords] = search_music_info
        self.data['keywords'] = keywords  # 更新搜索关键字

        return

    def play_search_music(self, music_id: str):
        self.data['auto_play_music_list'] = False
        # 播放搜索内容中的音乐
        self.load_music(music_id)

        # 设置当前播放列表为搜索音乐
        music_list = []
        keywords = self.data['keywords']
        list1 = self.data['search_music_info'][keywords]['songs_detail']
        for key in list1.keys():
            for key2 in list1[key].keys():
                music_list.append(list1[key][key2]['id'])
        self.data['music_list'] = music_list
        self.data['music_list_type'] = self.music_list_search
        return

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 搜索音乐相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 歌单展示相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    @Slot()
    def on_display_playlist_btn_toggled(self):
        # 歌单按钮被点击，加载歌单
        if self.display_playlist_btn.isChecked():
            # 如果是选中状态
            self.main_stacked_widget.setCurrentIndex(0)
            # 首先移除子页面
            self.remove_subpage()

            # 创建子页面
            if self.subpage is None:
                # 未页面则创建子页面
                self.subpage = PlaylistPage(self.main_stacked_widget)
                self.recommend_playlist_verticalLayout.addWidget(self.subpage, 0)
                # 页面切换信号
                self.subpage.add_playlist_songs.connect(self.add_playlist_music)

                # 播放歌单音乐信号
                self.subpage.play_playlist_music.connect(self.play_playlist_music)
                # 页面加载完毕，恢复主窗口信号
                self.subpage.enable_ui.connect(self.enable_ui)
            # 加载指定id的歌单
            playlist_id = self.data['playlist_id']
            self.load_playlist(playlist_id)
            return

    def add_playlist_music(self):
        # 滑动到底部，加载音乐
        # 当前歌单id
        playlist_id = self.data['playlist_id']
        # 下一页页数
        page = self.data['playlist_info'][playlist_id]['page'] + 1
        if page <= self.data['playlist_info'][playlist_id]['max_page']:
            # 当前页数在范围内
            self.load_playlist(playlist_id=playlist_id, page=page)
        return

    def load_playlist(self, playlist_id: str, page: int = 1, music_count: int = 30):
        # 加载歌单音乐信息
        if playlist_id == '' or playlist_id == None:
            # 歌单id不存在直接退出
            return

        self.display_playlist_btn.click()
        self.disable_ui()

        # 歌单id
        if playlist_id in self.data['playlist_info'].keys():
            # 歌单信息已存储
            # 已加载页数
            load_page = self.data['playlist_info'][playlist_id]['page']
            if page <= load_page:
                # 要加载的页数小于已加载的页数，直接加载当前数据
                # print('该歌单已加载')
                playlist_info = {}
                playlist_info['data'] = self.data['playlist_info'][playlist_id]
                self.set_playlist(playlist_info)
                return

        # 启动线程
        self.thread = PlaylistInfo(self.cloud, playlist_id=playlist_id, page=page, count=self.music_count)
        self.thread.playlist_finished.connect(self.set_playlist)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        return

    def set_playlist(self, playlist_info: dict):
        # 加载歌单内容
        playlist_info = playlist_info['data']
        # 设置内容
        self.subpage.add_playlist_music(playlist_info)

        # 储存该页歌单信息
        # 更新当前歌单id
        playlist_id = str(playlist_info['id'])
        self.data['playlist_id'] = playlist_id
        # 本次加载的页数
        page = playlist_info['page']
        if playlist_id not in self.data['playlist_info'].keys():
            # 未加载该歌单内容
            # 储存歌单信息
            self.data['playlist_info'][playlist_id] = playlist_info
        else:
            # 已加载该歌单内容
            # 储存单页歌单音乐信息
            self.data['playlist_info'][playlist_id]['songs_detail'][str(page)] = playlist_info['songs_detail'][
                str(page)]
            self.data['playlist_info'][playlist_id]['page'] = playlist_info['page']
            pass
        return

    def play_playlist_music(self, music_id: str):
        self.data['auto_play_music_list'] = False
        # 播放歌单音乐
        self.load_music(music_id)
        # 设置当前播放列表为歌单音乐
        playlist_id = self.data['playlist_id']
        music_list = self.data['playlist_info'][playlist_id]['trackIds']
        self.data['music_list'] = music_list
        self.data['music_list_type'] = self.music_list_playlist
        return

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 歌单展示相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 播放音乐相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    @Slot()
    def on_max_btn_clicked(self):
        # 最大化
        if not self.isMaximized():
            self.showMaximized()
        else:
            self.showNormal()

    @Slot()
    def on_play_page_btn_toggled(self):
        # 播放页按钮被点击，加载播放页面
        if self.play_page_btn.isChecked():
            # 如果是选中状态
            self.main_stacked_widget.setCurrentIndex(1)

    @Slot()
    def on_music_time_slider_sliderReleased(self):
        # 滑块按钮按下，设置滑块至不在实时更新
        val = self.music_time_slider.value()
        self.play_at_music(val)
        return

    def showFullScreen(self):
        # 全屏展示时将当前歌词滚动至中心
        super().showFullScreen()
        index = self.data['lrc']['last_lyric_index']
        self.scroll_lrc_to_center(index)
        return

    def load_music(self, music_id: str):
        # 启动下载线程
        # music_id = '1974443814'
        self.stop_music()
        # 启动下载线程并连接更新界面
        self.disable_ui()
        self.download_thread = SongDownload(self.cloud, music_id)
        self.download_thread.songs_download_finished.connect(self.update_ui)
        self.download_thread.finished.connect(self.download_thread.deleteLater)
        self.download_thread.finished.connect(lambda: self.enable_ui())
        self.download_thread.start()
        return

    def update_ui(self, music_info):
        # pprint(music_info)
        # 更新界面

        # 设置基本信息
        self.set_music_info(music_info)
        # 载入音乐并播放
        self.player.setMusic(music_info['music_save_path'])

        self.player.setVolume(self.volume_slider.value() / 100)

        self.play_music()

        return

    def set_music_info(self, music_info):
        # 设置音乐信息（图片、名称、歌手）
        # pprint(music_info)
        # 设置图片
        img_path = music_info['song_detail']['img_path']
        self.music_pic_btn.setStyleSheet(f'border-image: url({img_path})')
        # 设置音乐名
        music_name = music_info['song_detail']['name']
        self.music_name_lab.setText(music_name)
        self.music_name_lab_2.setText(music_name)
        # 设置歌手
        artists = ''
        for artist in music_info['song_detail']['ar']:
            # print(artist)
            if artists == '':
                artists += artist['name']
            else:
                artists += ', ' + artist['name']
        self.artists_lab.setText(artists)
        self.artists_lab_2.setText(artists)
        # 设置滑动条最大值为音乐毫秒值
        max_value = music_info['song_detail']['dt']
        self.data['duration'] = max_value
        self.music_time_slider.setMaximum(max_value)
        self.set_mini_page_time_maximum(max_value)
        # 设置最大时间
        max_time = self.trans_time(music_info['song_detail']['dt'])
        self.all_time_lab.setText(max_time)

        # 设置当前音乐信息
        self.data['music_loaded'] = True
        self.data['music_info'] = music_info
        self.data['music_id'] = str(music_info['song_detail']['id'])

        # 设置歌词
        self.set_lyric(music_info['song_detail']['lyric'])

        return

    def set_lyric(self, lyric):
        # 设置歌词

        try:
            # 首先清空歌词
            self.remove_lyric()

            lyric_list = []
            for item in lyric.split('\n'):
                # 换行符号拆分歌词
                if item != '':
                    # 拆分单行歌词并转换为毫秒值
                    # print(item)
                    time1 = item.split(']')[0][1:]
                    m = time1.split(':')[0]  # 分钟
                    s = time1.split(':')[1]  # 秒
                    time1 = int(int(m) * 60000 + float(s) * 1000)  # 组合为毫秒值
                    # 拆分单行歌词的词部分
                    lrc = item.split(']')[1] if len(item.split(']')) > 1 else ''  # 单行歌词
                    # 以字典类型添加至歌词列表
                    lyric_list.append({'time': time1, 'lrc': lrc})
            # 储存歌词列表并将当前歌词下标设置为1
            self.data['lrc']['lyric'] = lyric_list
            # self.data['lrc']['lyric_index'] = 0

            # 插入歌词
            i = 0
            for item in self.data['lrc']['lyric']:
                label = QLabel()
                label.setStyleSheet(self.lrc_stylesheet)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                label.setWordWrap(True)
                label.setMinimumWidth(300)
                label.setMinimumHeight(40)
                label.setText(item['lrc'])
                label.setObjectName(f'lyric_lab_{i}')
                self.lyric_vertical_layout.insertWidget(i, label)
                i += 1

            # 歌词设置成功，设置歌词滚动
            self.data['lrc']['need_screen'] = True

        except Exception as e:
            print(e)
            # 歌词设置失败，设置歌词滚动
            self.data['lrc']['need_screen'] = False

            # 首先清空歌词
            self.remove_lyric()
            # 设置暂无歌词
            label = QLabel()
            label.setStyleSheet(self.lrc_stylesheet)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setWordWrap(True)
            label.setMinimumWidth(300)
            label.setMinimumHeight(40)
            label.setText('暂无歌词')
            label.setObjectName(f'lyric_lab_{0}')
            self.lyric_vertical_layout.insertWidget(0, label)

    def remove_lyric(self):
        # 移除歌词
        lrc_lab_list = self.lyric_scroll_area.findChildren(QLabel)
        for item in lrc_lab_list:
            if 'lyric_lab_' in item.objectName():
                item.setParent(None)
                item.deleteLater()
        # 清空已存储的歌词内容
        self.data['lrc']['lyric'] = []
        # self.data['lrc']['lyric_index'] = 0

    def scroll_lrc(self):
        # 判断是否需要滚动歌词
        if self.data['lrc']['need_screen']:
            # 需要滚动歌词

            index = -1
            lrc = self.data['lrc']['lyric']
            for item in lrc:
                if self.data['now'] > item['time']:
                    index += 1

            if index <= len(lrc):
                if index != self.data['lrc']['last_lyric_index']:
                    # 将当前歌词滚动至中心
                    self.scroll_lrc_to_center(index)
                    # 设置样式
                    self.highlight_lrc(index)
        return

    def highlight_lrc(self, index: int):
        # 设置当前歌词高亮
        # 重置上一行样式
        last_index = self.data['lrc']['last_lyric_index']
        if last_index >= 0:
            # 清空上一行样式
            self.reset_lrc_style(last_index)
        # 设置本行样式
        label = self.lyric_scroll_area.findChild(QLabel, f'lyric_lab_{index}')
        if label is not None:
            if label.text() != '':
                label.setStyleSheet(self.lrc_stylesheet_highlight)
                self.set_mini_page_lrc(label.text())
        # 设置上一行歌词下标为当前下标
        self.data['lrc']['last_lyric_index'] = index
        return

    def reset_lrc_style(self, index: int):
        # 重置一行歌词的样式
        if index >= 0:
            # 清空一行样式
            label = self.lyric_scroll_area.findChild(QLabel, f'lyric_lab_{index}')
            if label is not None:
                label.setStyleSheet(self.lrc_stylesheet)
        return

    def scroll_lrc_to_center(self, index: int = 1, duration: int = 800):
        # 将某行歌词移动至滚动区域中心
        label = self.lyric_scroll_area.findChild(QLabel, f'lyric_lab_{index}')
        if label:
            # print(label.text())
            # 当前label距离滚动区域左上角的距离
            label_pos = label.mapTo(self.scrollAreaWidgetContents_4, QPoint(0, 0))
            # label的高度
            label_height = label.size().height()
            # 歌词滚动区域可见区域高度
            viewport_height = self.lyric_scroll_area.viewport().height()
            # label_pos是将label滚动到0，0的值，减去(可视区域 - label高度) / 2 即为中心位置，超出范围自动失效
            target_y = label_pos.y() - (viewport_height - label_height) // 2

            # 开始滚动
            self.animate_scroll(target_y, duration)

        return

    def animate_scroll(self, target_value, duration: int = 800):
        # 滚动目标至指定位置
        """修复动画存储问题的版本"""
        # print(f'进入滚动动画: {target_value}')
        scroll_bar = self.lyric_scroll_area.verticalScrollBar()

        # 创建并存储动画对象
        self.scroll_animation = QPropertyAnimation(scroll_bar, b"value")
        self.scroll_animation.setDuration(duration)
        self.scroll_animation.setStartValue(scroll_bar.value())
        self.scroll_animation.setEndValue(target_value)
        self.scroll_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        # 确保动画完成后释放资源
        self.scroll_animation.finished.connect(
            lambda: self.scroll_animation.deleteLater()
        )

        self.scroll_animation.start()
        return

    def add_time(self):
        # 增加时间，同步更新ui
        if self.data['now'] >= self.data['duration']:
            # 超过最大时间，自动停止并播放下一首
            self.auto_stop()
            return

        # 设置滑动条
        self.data['now'] += self.interval
        self.music_time_slider.setValue(self.data['now'])
        self.set_mini_page_time_value(self.data['now'])
        # 设置时间标签
        now = self.trans_time(self.data['now'])
        self.now_time_lab.setText(f'{now}')
        self.set_mini_page_time(f'{now}')
        # 判断是否滚动歌词
        self.scroll_lrc()

        return

    def play_music(self):
        if self.data['music_loaded']:
            # 播放音乐
            self.player.play()
            # 设置播放状态为正在播放
            self.data['play_status'] = self.playing
            # 设置一个0.2s触发一次的定时器
            self.data['timer'].start()
            # 设置图标为暂停
            self.play_btn.setStyleSheet(self.icon_pause)
            self.set_mini_page_play_icon(self.icon_pause)
            # 设置自动播放标志
            self.data['auto_play_music_list'] = True
        return

    def play_at_music(self, position: int):
        if self.data['music_loaded']:
            # 指定位置播放音乐
            self.player.playAt(position)
            # 设置播放状态为正在播放
            self.data['play_status'] = self.playing
            self.data['now'] = position
            # 设置一个0.2s触发一次的定时器
            self.data['timer'].start()
            # 设置图标为暂停
            self.play_btn.setStyleSheet(self.icon_pause)
            self.set_mini_page_play_icon(self.icon_pause)
            # 设置自动播放标志
            self.data['auto_play_music_list'] = True
        return

    def pause_music(self):
        # 播放或暂停音乐
        if self.data['music_loaded']:
            # 加载过音乐才可进行
            if self.data['play_status'] == self.playing:
                # 如果当前为播放中，暂停播放
                # 暂停计时器
                self.data['timer'].stop()
                # 停止播放
                self.player.pause()
                self.data['play_status'] = self.pause
            # 设置图标为播放
            self.play_btn.setStyleSheet(self.icon_play)
            self.set_mini_page_play_icon(self.icon_play)

        return


    def stop_music(self):
        if self.data['play_status'] == self.playing or self.data['play_status'] == self.pause:
            # 如果当前处于播放或暂停状态，停止播放音乐
            if self.data['timer'].isActive():
                self.data['timer'].stop()
            # 停止播放
            self.player.stop()
            self.data['play_status'] = self.stop
        # 滑动条设置0
        self.music_time_slider.setValue(0)
        # 设置滑动条值为0
        self.now_time_lab.setText('00:00')
        # 当前时间设置为0
        self.data['now'] = 0
        # 重置歌词样式并滚动到开头
        self.reset_lrc_style(self.data['lrc']['last_lyric_index'])
        self.data['lrc']['last_lyric_index'] = 0
        self.lyric_scroll_area.verticalScrollBar().setValue(0)
        # 设置图标为播放
        self.play_btn.setStyleSheet(self.icon_play)
        self.set_mini_page_play_icon(self.icon_play)
        return

    def auto_stop(self):
        # 停止音乐并播放下一首
        self.stop_music()
        if self.data['auto_play_music_list']:
            # 如果是自动播放标志
            # 自动播放下一首
            self.next_music()
        return

    def next_music(self):
        # 播放下一首音乐
        if self.data['music_list'] != []:
            # 播放列表不为空
            index = 0
            music_id = self.data['music_id']
            if self.data['settings']['repeat'] == self.repeat_order:
                # 顺序播放
                if music_id in self.data['music_list']:
                    # 当前id在播放列表中
                    # 列表到底末尾自动置零
                    index = (self.data['music_list'].index(music_id) + 1) % len(self.data['music_list'])
            elif self.data['settings']['repeat'] == self.repeat_one:
                # 单曲循环
                if music_id in self.data['music_list']:
                    # 当前id在播放列表中
                    index = self.data['music_list'].index(music_id)
            elif self.data['settings']['repeat'] == self.repeat_random:
                # 随机播放
                index = random.randint(0, len(self.data['music_list']))
            # 播放
            self.load_music(self.data['music_list'][index])
        return

    def prev_music(self):
        # 播放下一首音乐
        if self.data['music_list'] != []:
            # 播放列表不为空
            index = 0
            music_id = self.data['music_id']
            if music_id in self.data['music_list']:
                # 当前id在播放列表中
                # 列表到底末尾自动置零
                if self.data['settings']['repeat'] == self.repeat_order:
                    # 顺序播放
                    index = (self.data['music_list'].index(music_id) - 1) % len(self.data['music_list'])
                    index = index if index >= 0 else len(self.data['music_list']) - 1
                elif self.data['settings']['repeat'] == self.repeat_one:
                    # 单曲循环
                    if music_id in self.data['music_list']:
                        # 当前id在播放列表中
                        index = self.data['music_list'].index(music_id)
                elif self.data['settings']['repeat'] == self.repeat_random:
                    # 随机播放
                    index = random.randint(0, len(self.data['music_list']))
            # 播放协议书
            self.load_music(self.data['music_list'][index])
        return

    @Slot()
    def on_like_btn_clicked(self):
        # self.stop_music()
        self.msg_page = MessagePage('下载完成', '456已保存至')
        return

    @Slot(int)
    def on_volume_slider_valueChanged(self, val):
        # 音量滑动条变化，同步修改音量
        self.player.setVolume(val / 100)
        if val == 0:
            self.volume_btn.setStyleSheet(self.icon_volume_0)
        elif val < 50:
            self.volume_btn.setStyleSheet(self.icon_volume_1)
        elif val > 50:
            self.volume_btn.setStyleSheet(self.icon_volume_2)

    @Slot()
    def on_play_btn_clicked(self):
        # 播放按钮
        self.auto_play()
        return

    @Slot()
    def on_next_btn_clicked(self):
        # 上一首按钮
        self.next_music()
        return

    @Slot()
    def on_last_btn_clicked(self):
        # 下一首按钮
        self.prev_music()
        return

    @Slot()
    def on_order_btn_clicked(self):
        # 播放顺序按钮
        if self.data['settings']['repeat'] == self.repeat_order:
            # 顺序播放，则设置为单曲循环
            self.order_btn.setStyleSheet(self.icon_repeat_one)
            self.data['settings']['repeat'] = self.repeat_one
        elif self.data['settings']['repeat'] == self.repeat_one:
            # 单曲循环播放，则设置为随机播放
            self.order_btn.setStyleSheet(self.icon_repeat_random)
            self.data['settings']['repeat'] = self.repeat_random
        elif self.data['settings']['repeat'] == self.repeat_random:
            # 随机播放，则设置为顺序播放
            self.order_btn.setStyleSheet(self.icon_repeat_order)
            self.data['settings']['repeat'] = self.repeat_order
        return

    def auto_play(self):
        if self.data['play_status'] == self.playing:
            self.pause_music()
        elif self.data['play_status'] == self.pause or self.data['play_status'] == self.stop:
            self.play_music()
        return

    def trans_time(self, time):
        # 将毫秒转换为分秒
        m = int(time) // 60000
        s = (int(time) % 60000) // 1000
        return f"{m}:{s}"

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 播放音乐相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 下载音乐相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    @Slot()
    def on_download_btn_clicked(self):
        # 音乐下载按钮
        if self.data['music_id'] is not None and self.data['music_loaded']:
            if self.save_thread is None:
                self.save_thread = SaveSong(self.cloud, self.data['music_id'])
                self.save_thread.save_song_finished.connect(self.save_finish_msg)
                self.save_thread.finished.connect(self.save_thread.deleteLater)
                self.save_thread.finished.connect(self.delete_save_song_thread)
                self.save_thread.start()
            else:
                self.msg_page = MessagePage('无法下载', '音乐下载中，请等待下载完成')
        else:
            self.msg_page = MessagePage('无法下载', '未加载音乐')
        return

    def save_finish_msg(self, data: dict):
        save_path = data['music_save_path']
        self.msg_page = MessagePage('下载完成', f'音乐已保存至：{save_path}')
        return

    def delete_save_song_thread(self):
        # 清空保存线程
        self.save_thread = None
        return

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 下载音乐相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 播放子页面相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    @Slot()
    def on_mini_btn_clicked(self):
        if self.mini_page == None:
            self.mini_page = MiniPage()
            self.set_mini_page()
            self.mini_page.mini_page_close.connect(self.close_mini_page)
            self.mini_page.play.connect(self.auto_play)
            self.mini_page.play_at.connect(self.play_at_music)
        else:
            self.mini_page.close()
        return

    def set_mini_page(self):
        # 初始化子页面内容
        if self.mini_page != None:
            maximum = self.music_time_slider.maximum()
            self.set_mini_page_time_maximum(maximum)

            value = self.music_time_slider.value()
            self.set_mini_page_time_value(value)

            now_time = self.now_time_lab.text()
            self.set_mini_page_time(now_time)

            lrc = ''
            index = self.data['lrc']['last_lyric_index']
            if self.data['lrc']['lyric'] != [] and index >= 0 and index < len(self.data['lrc']['lyric']):
                lrc = self.data['lrc']['lyric'][index]['lrc']
            self.set_mini_page_lrc(lrc)

            qss = self.play_btn.styleSheet()
            self.set_mini_page_play_icon(qss)
        return

    def set_mini_page_time_maximum(self, maximum: int = 100):
        # 设置子页面滑动条最大值
        if self.mini_page != None:
            self.mini_page.set_mini_page_time_maximum(maximum)
        return

    def set_mini_page_time_value(self, value: int = 100):
        # 设置子页面滑动条当前值
        if self.mini_page != None:
            self.mini_page.set_mini_page_time_value(value)
        return

    def set_mini_page_time(self, time: str = ''):
        # 设置子页面当前时间
        if self.mini_page != None:
            self.mini_page.set_mini_page_time(time)
        return

    def set_mini_page_lrc(self, lrc: str = ''):
        # 设置子页面当前歌词
        if self.mini_page != None:
            self.mini_page.set_mini_page_lrc(lrc)
        return

    def set_mini_page_play_icon(self, qss: str = ''):
        # 设置播放音乐图标
        if self.mini_page != None:
            self.mini_page.set_mini_page_play_icon(qss)
        return

    def close_mini_page(self):
        # 删除子页面
        if self.mini_page != None:
            self.mini_page = None
        return

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 播放子页面相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 左下角调整大小相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    def mousePressEvent(self, event):
        # 设置按压状态
        self.press_flag = True
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        # 恢复按压状态和调整大小标准
        self.press_flag = False
        self.resize_flag = False
        return super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        width = self.width()
        height = self.height()
        if event.pos().x() > width - 10 and event.pos().x() < width + 10 and event.pos().y() > height - 10 and event.pos().y() < height + 10:
            # print('进入边界')
            if not self.cursor_shape_flag:
                self.setCursor(Qt.CursorShape.SizeFDiagCursor)
                self.cursor_shape_flag = True

            if self.cursor_shape_flag and self.press_flag:
                # 图标形状改变，并且按压，设置调整大小标志
                self.resize_flag = True
        else:
            # 移出边界，恢复鼠标形状
            if self.cursor_shape_flag:
                self.unsetCursor()
                self.cursor_shape_flag = False

        if self.resize_flag:
            geo = self.geometry()
            x = geo.x()
            y = geo.y()
            width = event.x()
            height = event.y()
            self.setGeometry(x, y, width, height)

        return super().mouseMoveEvent(event)

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 左下角调整大小相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 修改设置相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    @Slot()
    def on_settings_btn_clicked(self):

        settings_data = self.load_settings()
        self.settings_page = SettingsPage(settings_data)
        self.settings_page.settings_save.connect(self.save_settings)
        return

    def load_settings(self):
        # 获取设置内容
        settings = {
            'cookies': '',
            'save_path': 'C:/',
            'repeat': self.repeat_order
        }
        path = self.settings_dir + 'settings.json'
        if os.path.exists(path):
            # 文件存在
            settings_1 = ''
            with open(path, 'r', encoding='utf-8') as f:
                settings_1 = json.loads(f.read())
            try:
                self.data['settings']['cookies'] = settings_1['cookies']
                settings['cookies'] = settings_1['cookies']
                self.data['settings']['save_path'] = settings_1['save_path']
                settings['save_path'] = settings_1['save_path']
                self.data['settings']['repeat'] = settings_1['repeat']
                settings['repeat'] = settings_1['repeat']
            except Exception as e:
                print(e)

        # 设置顺序图标
        if self.data['settings']['repeat'] == self.repeat_order:
            # 顺序播放
            self.order_btn.setStyleSheet(self.icon_repeat_order)
        elif self.data['settings']['repeat'] == self.repeat_one:
            # 单曲循环播放
            self.order_btn.setStyleSheet(self.icon_repeat_one)
        elif self.data['settings']['repeat'] == self.repeat_random:
            # 随机播放
            self.order_btn.setStyleSheet(self.icon_repeat_random)
        return settings

    def set_settings(self):
        try:
            data = self.load_settings()
            # 加载设置
            if 'cookies' in data:
                self.cloud.set_cookies(data['cookies'])
            if 'save_path' in data:
                self.cloud.set_save_path(data['save_path'])
        except Exception as e:
            print(e)
        return

    def save_settings(self, data: dict = None):
        # 保存设置内容
        if data == None:
            data = {}
            data['cookies'] = self.data['settings']['cookies']
            data['save_path'] = self.data['settings']['save_path']
        data['repeat'] = self.data['settings']['repeat']
        if not os.path.exists(self.settings_dir):
            os.mkdir(self.settings_dir)
        path = self.settings_dir + 'settings.json'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(data, indent=4))
        self.set_settings()
        return

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 修改设置相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    def loadFont(self):
        # 加载字体到数据库
        font_id = QFontDatabase.addApplicationFont(self.font_dir)
        if font_id == -1:
            print("字体加载失败！")
            return

        # ============================
        # 2. 获取字体家族名称
        # ============================
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        if not font_families:
            print("未找到有效字体家族")
            return
        return

    def set_qss(self):
        # 设置全局qss样式
        with open(self.qss_dir, 'r', encoding='utf-8') as qss_file:
            qss = qss_file.read()
            self.setStyleSheet(qss)

    playlist_count = 35  # 每次获取多少歌单
    music_count = 20  # 歌单每次获取多少首音乐
    qss_dir = 'ui/tools/resource/qss/main.qss'
    settings_dir = './settings/'
    font_dir = 'ui/tools/resource/bg/font/ZCOOL_KuaiLe/ZCOOLKuaiLe-Regular.ttf'  # 替换为你的字体文件路径

    # 刷新间隔
    interval = 100

    # 歌词样式
    lrc_stylesheet = """
    QLabel{
        color: white;
        font-size: 18px;
        font-weight: 600;
        padding: 12px 25px;
        border: none;
        border-radius: 8px;
    }
    """
    lrc_stylesheet_highlight = """
    QLabel{
        color: #E0EEEE;
        color: #E6659D;
        font-size: 22px;
        font-weight: 800;
        border: none;
        /*background-color: rgba(255, 255, 255, 0.4);
        border-radius: 5px;*/
    }
    """

    # 播放状态
    playing = 1
    pause = 2
    stop = 3

    # 当前播放列表类型
    music_list_recommend = 1
    music_list_search = 2
    music_list_playlist = 3

    # 重复类型
    repeat_order = 1
    repeat_one = 2
    repeat_random = 3

    # 图标
    icon_volume_0 = 'border-image: url(:/play/tools/resource/bg/icon/play/volume_0.png);'
    icon_volume_1 = 'border-image: url(:/play/tools/resource/bg/icon/play/volume_1.png);'
    icon_volume_2 = 'border-image: url(:/play/tools/resource/bg/icon/play/volume_2.png);'

    icon_play = 'border-image: url(:/play/tools/resource/bg/icon/play/play.png);'
    icon_pause = 'border-image: url(:/play/tools/resource/bg/icon/play/pause.png);'

    icon_vip = 'border-image: url(:/vip/tools/resource/bg/icon/vip/vip.png);'
    icon_vip_no = 'border-image: url(:/vip/tools/resource/bg/icon/vip/vip_no.png);'

    icon_repeat_order = 'border-image: url(:/play/tools/resource/bg/icon/play/shuffe_repeat.png);'
    icon_repeat_one = 'border-image: url(:/play/tools/resource/bg/icon/play/shuffe_1.png);'
    icon_repeat_random = 'border-image: url(:/play/tools/resource/bg/icon/play/shuffle_random.png);'


if __name__ == "__main__":
    app = QApplication([])
    window = MyForm()
    app.exec()
