import sys
from pprint import pprint

from PySide6.QtCore import Qt, QObject, Signal, Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication

from PySide_UI.ui.tools.sub_ui.one_music import Ui_music
from PySide_UI.ui.tools.sub_ui.search import Ui_search


class OneMusic(QWidget, Ui_music):
    # 单个音乐
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置顶层窗口qwidget样式生效
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground)


class SearchPage(QWidget, Ui_search):
    # 设置每日推荐歌单
    search = Signal(str)
    play_search_music = Signal(str)
    add_songs = Signal()
    error = Signal(str)
    enable_ui = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置顶层窗口qwidget样式生效
        self.setAttribute(Qt.WA_StyledBackground)
        self.setupUi(self)
        # self.show()

        # 设置滚动到底部的事件
        self.set_scrollbar_singl()
        self.keywords = ''
        self.index = 0


    def add_search_music(self, music_infos: dict):
        # 获取歌单信息后，插入指定数量的歌单子项并设置内容
        # pprint(music_infos)
        try:
            if self.keywords != music_infos['keywords']:
                # 关键字改变，移除之前的音乐
                # 下标设置为0
                self.index = 0
                # 滚动到开头
                self.search_music_scrollArea.verticalScrollBar().setValue(0)
                # 移除音乐
                self.remove_search_music()
            # 更新关键字
            self.keywords = music_infos['keywords']
            for key in music_infos['songs_detail']:
                # 插入指定数量的音乐子项
                music_info = music_infos['songs_detail'][key]
                music_count = len(music_info.keys())
                self.insert_music(self.search_music_verticalLayout, music_count, 'search_music')

                for key in music_info.keys():
                    music_id = music_info[key]['id']
                    widget = self.search_music_scrollArea.findChild(QWidget, f'search_music_{self.index}')
                    # 设置音乐图片及id
                    img_path = music_info[key]['img_path']
                    widget.img_btn.setStyleSheet(f'border-image: url({img_path});')
                    widget.img_btn.setProperty('music_id', music_id)

                    # 时长
                    duration = music_info[key]['dt']
                    time = self.trans_time(duration)
                    widget.duration_lab.setText(time)

                    # vip
                    if music_info[key]['vip']:
                        widget.vip_btn.setStyleSheet(self.icon_vip)

                    # 设置音乐名称及歌手名称和音乐id
                    # 音乐名称
                    name = music_info[key]['name']
                    widget.music_name_lab.setText(name)
                    widget.music_name_lab.setProperty('music_id', music_id)

                    # 歌手名称
                    singer = []
                    artists = music_info[key]['ar']
                    for artist in artists:
                        singer.append(artist['name'])
                    widget.singer_lab.setText(', '.join(singer))

                    widget.play_music_btn.setProperty('music_id', music_id)

                    # # 左击事件
                    # widget.img_btn.leftclick.connect(lambda val: pprint(val))
                    # widget.music_name_lab.leftclick.connect(lambda val: pprint(val))
                    # widget.play_music_btn.leftclick.connect(lambda val: pprint(val))

                    # 左击名称或按钮
                    widget.music_name_lab.leftclick.connect(lambda val: self.play_search_music.emit(val['music_id']))
                    widget.play_music_btn.leftclick.connect(lambda val: self.play_search_music.emit(val['music_id']))

                    self.index += 1
        except Exception as e:
            pprint(e)
            self.error.emit(str(e))
        finally:
            # 恢复ui
            self.enable_ui.emit()

    def remove_search_music(self):
        # 移除推荐歌单内容
        self.remove_music(self.search_music_scrollArea, 'search_music')

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
            new_index = self.index + i
            widget.setObjectName(f'{obj_name}_{new_index}')
            # 将面板插入到末尾
            index2 = layout.count()
            widget.count_lab.setText(str(new_index + 1))
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

    @Slot()
    def on_sub_search_btn_clicked(self):
        # 搜索按钮被点击
        keywords = self.search_lineEdit.text().strip()
        if keywords is not None:
            # 搜索内容不为空，发射信号
            self.search.emit(keywords)
        return

    @Slot()
    def on_search_lineEdit_returnPressed(self):
        # 文本框回车键
        self.sub_search_btn.click()
        return

    def set_scrollbar_singl(self):
        # 滚动条滚动到底部事件
        scrollbar = self.search_music_scrollArea.verticalScrollBar()

        def scroll_down():
            if scrollbar.value() == scrollbar.maximum() and scrollbar.value() != 0:
                print('滑动到底部')
                self.add_songs.emit()

        scrollbar.valueChanged.connect(scroll_down)
        return

    icon_vip = 'border-image: url(:/vip/tools/resource/bg/icon/vip/vip.png);'
    icon_vip_no = 'border-image: url(:/vip/tools/resource/bg/icon/vip/vip_no.png);'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SearchPage()
    w.show()
    sys.exit(app.exec())
