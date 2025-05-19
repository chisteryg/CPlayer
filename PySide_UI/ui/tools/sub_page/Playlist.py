import sys
from pprint import pprint

from PySide6.QtCore import Qt, Signal, QObject, Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication

from PySide_UI.ui.tools.sub_ui.one_music import Ui_music
from PySide_UI.ui.tools.sub_ui.playlist import Ui_playlist


class OneMusic(QWidget, Ui_music):
    # 单个音乐
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置顶层窗口qwidget样式生效
        self.setAttribute(Qt.WA_StyledBackground)
        self.setupUi(self)

        self.playlist_id = None
        self.page = -1
        self.max_page = -1


class PlaylistPage(QWidget, Ui_playlist):
    # 歌单音乐
    play_playlist_music = Signal(str)
    load_playlist = Signal(dict)
    add_playlist_songs = Signal()
    error = Signal(str)
    enable_ui = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground)


        # 设置滚动到底部的信号
        self.set_scrollbar_singl()
        # 音乐加载下标
        self.index = 0

    def add_playlist_music(self, playlist_info: dict):
        # 获取歌单信息后，插入指定数量的歌单子项并设置内容
        try:
            # 图片
            img_path = playlist_info['img_path']
            self.list_img_btn.setStyleSheet(f'border-image: url({img_path});')
            # 歌单名称
            self.list_name_lab.setText(f'{playlist_info["name"]}（共{playlist_info["trackCount"]}首）')

            # 加载音乐内容
            songs_info = playlist_info['songs_detail']
            for key in songs_info:
                playlist_music = songs_info[key]
                playlist_count = len(playlist_music.keys())
                # 插入指定数量的歌单子项
                self.insert_music(self.playlist_verticalLayout, playlist_count, 'playlist_music')

                # 设置歌单内容
                for key2 in playlist_music.keys():
                    music_id = playlist_music[key2]['id']
                    widget = self.playlist_scroll_area.findChild(QWidget, f'playlist_music_{self.index}')
                    # 设置音乐图片及id
                    img_path = playlist_music[key2]['img_path']
                    widget.img_btn.setStyleSheet(f'border-image: url({img_path});')
                    widget.img_btn.setProperty('music_id', music_id)

                    # 时长
                    duration = playlist_music[key2]['dt']
                    time = self.trans_time(duration)
                    widget.duration_lab.setText(time)

                    # vip
                    if playlist_music[key2]['vip']:
                        widget.vip_btn.setStyleSheet(self.icon_vip)

                    # 设置音乐名称及歌手名称和音乐id
                    # 音乐名称
                    name = playlist_music[key2]['name']
                    widget.music_name_lab.setText(name)
                    widget.music_name_lab.setProperty('music_id', music_id)

                    # 歌手名称
                    singer = []
                    artists = playlist_music[key2]['ar']
                    for artist in artists:
                        singer.append(artist['name'])
                    widget.singer_lab.setText(', '.join(singer))

                    widget.play_music_btn.setProperty('music_id', music_id)

                    # # 左击事件
                    # widget.img_btn.leftclick.connect(lambda val: pprint(val))
                    # widget.music_name_lab.leftclick.connect(lambda val: pprint(val))
                    # widget.play_music_btn.leftclick.connect(lambda val: pprint(val))

                    # 左击事件
                    widget.music_name_lab.leftclick.connect(lambda val: self.play_playlist_music.emit(val['music_id']))
                    widget.play_music_btn.leftclick.connect(lambda val: self.play_playlist_music.emit(val['music_id']))

                    self.index += 1

        except Exception as e:
            print(e)
            self.error.emit(str(e))
        finally:
            # 恢复ui
            self.enable_ui.emit()
        return


    def remove_playlist_music(self):
        # 移除推荐歌单内容
        self.remove_music(self.playlist_scroll_area, 'playlist_music')

    def insert_music(self, layout: QVBoxLayout, count: int = 10, obj_name: str = 'music'):
        '''
        将指定数量的单个音乐插入到垂直布局中
        :param layout: 要插入的布局
        :param count: 音乐数量
        :param obj_name: 歌单对象名称，用于区分不同的歌单
        :return:
        '''
        for i in range(count):
            # 创建单首音乐面板
            widget = OneMusic()
            widget.setObjectName(f'{obj_name}_{self.index + i}')
            # 将面板插入到末尾
            index2 = layout.count() - 1
            widget.count_lab.setText(str(layout.count()))
            layout.insertWidget(index2, widget)
        return

    def remove_music(self, obj: QObject, obj_name='music'):
        '''
        移除格子布局中所有的歌单子项
        :param obj: 父控件，从哪里移除
        :param obj_name: 歌单对象名，删除指定类型的歌单
        :return:
        '''
        # 查找该控件下所有的qwidget
        wiget_list = obj.findChildren(QWidget)
        for item in wiget_list:
            if obj_name in item.objectName():
                item.setParent(None)
                item.deleteLater()
        return

    def trans_time(self, time):
        # 将毫秒转换为分秒
        m = int(time) // 60000
        s = (int(time) % 60000) // 1000
        return f"{m}:{s}"

    def set_scrollbar_singl(self):
        # 滚动条滚动到底部事件
        scrollbar = self.playlist_scroll_area.verticalScrollBar()

        def scroll_down():
            if scrollbar.value() == scrollbar.maximum() and scrollbar.value() != 0:
                print('滑动到底部')
                self.add_playlist_songs.emit()

        scrollbar.valueChanged.connect(scroll_down)
        return

    icon_vip = 'border-image: url(:/vip/tools/resource/bg/icon/vip/vip.png);'
    icon_vip_no = 'border-image: url(:/vip/tools/resource/bg/icon/vip/vip_no.png);'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = PlaylistPage()
    w.show()
    sys.exit(app.exec())
