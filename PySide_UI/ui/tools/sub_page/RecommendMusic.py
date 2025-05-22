import sys
from datetime import datetime
from pprint import pprint

from PySide6.QtCore import Signal, Qt, QObject
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout

from PySide_UI.ui.tools.sub_ui.one_music import Ui_music
from PySide_UI.ui.tools.sub_ui.recommend_music import Ui_recommend_music


class OneMusic(QWidget, Ui_music):
    # 单个音乐
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置顶层窗口qwidget样式生效
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setupUi(self)


class RecommendMusicPage(QWidget, Ui_recommend_music):
    # 设置每日推荐歌单
    play_recommend_music = Signal(str)
    error = Signal(str)
    enable_ui = Signal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        # 设置样式生效
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        # self.show()
        # 设置日期
        day = datetime.today().date().day
        month = datetime.today().date().month
        year = datetime.today().date().year
        self.day_lab.setText(f'{year} / {month} / {day}')

    def set_recommend_music(self, recommend_music: dict):
        # 获取歌单信息后，插入指定数量的歌单子项并设置内容

        try:
            # 设置推荐音乐内容
            # 插入指定数量的音乐子项
            music_count = len(recommend_music.keys())
            self.insert_music(self.recommend_music_vertical_layout, music_count, 'recommend_music')

            i = 0
            for key in recommend_music.keys():
                music_id = recommend_music[key]['id']
                widget = self.recommend_music_scroll_area.findChild(QWidget, f'recommend_music_{i}')
                # 设置音乐图片及id
                img_path = recommend_music[key]['img_path']
                widget.img_btn.setStyleSheet(f'border-image: url({img_path});')
                widget.img_btn.setProperty('music_id', music_id)

                # 时长
                duration = recommend_music[key]['dt']
                time = self.trans_time(duration)
                widget.duration_lab.setText(time)

                # vip
                if recommend_music[key]['vip']:
                    widget.vip_btn.setStyleSheet(self.icon_vip)

                # 设置音乐名称及歌手名称和音乐id
                # 音乐名称
                name = recommend_music[key]['name']
                widget.music_name_lab.setText(name)
                widget.music_name_lab.setProperty('music_id', music_id)

                # 歌手名称
                singer = []
                artists = recommend_music[key]['ar']
                for artist in artists:
                    singer.append(artist['name'])
                widget.singer_lab.setText(', '.join(singer))

                widget.play_music_btn.setProperty('music_id', music_id)

                # # 左击事件
                # widget.music_name_lab.leftclick.connect(lambda val: pprint(val))
                # widget.play_music_btn.leftclick.connect(lambda val: pprint(val))

                # 左击事件
                widget.music_name_lab.leftclick.connect(lambda val: self.play_recommend_music.emit(val['music_id']))
                widget.play_music_btn.leftclick.connect(lambda val: self.play_recommend_music.emit(val['music_id']))

                i += 1

        except Exception as e:
            print(e)
            self.error.emit(str(e))
        finally:
            self.enable_ui.emit()
        return

    def remove_recommend_music(self):
        # 移除推荐歌单内容
        self.remove_music(self.recommend_music_scroll_area, 'recommend_music')

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
            widget.setObjectName(f'{obj_name}_{i}')
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

    icon_vip = 'border-image: url(:/vip/tools/resource/bg/icon/vip/vip.png);'
    icon_vip_no = 'border-image: url(:/vip/tools/resource/bg/icon/vip/vip_no.png);'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = RecommendMusicPage()
    sys.exit(app.exec())
