from pprint import pprint

from PySide6.QtCore import QThread, Signal
from PySide_UI.tools.NeteaseCloudMusic_API.httpx_api_2 import NeteaseCloudMusicAPI





class RecommendPlayList(QThread):
    recommend_playlist_finished = Signal(dict)

    # 推荐歌单线程
    def __init__(self, cloud: NeteaseCloudMusicAPI, page: int, count: int, cat: str):
        super().__init__()
        self.cloud = cloud
        self.page = page
        self.count = count
        self.cat = cat

    def run(self):
        """获取推荐歌单内容"""
        data = {
            'status': None,
            'msg': '',
            'data': None,
        }
        recommend_playlist = self.cloud.recommend_playlist(count=self.count, page=self.page, cat=self.cat)
        if recommend_playlist['requests_status']:
            # 请求成功
            if recommend_playlist['code'] == 200:
                # 接口获取成功
                if recommend_playlist['api_return_code'] == 200:
                    # api接口返回正常
                    data['status'] = True
                    data['msg'] = '网络请求成功，接口返回成功'
                    data['data'] = recommend_playlist['data']
                else:
                    # api接口返回不正常
                    data['status'] = False
                    data['msg'] = '网络请求成功，但接口返回异常'
            else:
                # 状态码不正常
                data['status'] = False
                data['msg'] = '网络请求成功，但状态码不正常'
        else:
            # 请求失败
            data['status'] = False
            data['msg'] = '网络请求失败，请检查网络是否连通，api接口是否有效'

        self.recommend_playlist_finished.emit(data)
        return


class RecommendMusic(QThread):
    recommend_music_finished = Signal(dict)
    error = Signal(str)

    # 推荐歌单线程
    def __init__(self, cloud: NeteaseCloudMusicAPI):
        super().__init__()
        self.cloud = cloud

    def run(self):
        """获取推荐音乐内容"""
        data = {
            'status': None,
            'msg': '',
            'data': None,
        }
        recommend_music = self.cloud.recommend_music_info()
        if recommend_music['requests_status']:
            # 请求成功
            if recommend_music['code'] == 200:
                # 接口获取成功
                if recommend_music['api_return_code'] == 200:
                    # api接口返回正常
                    data['status'] = True
                    data['msg'] = '网络请求成功，接口返回成功'
                    data['data'] = recommend_music['data']
                else:
                    # api接口返回不正常
                    data['status'] = False
                    data['msg'] = '网络请求成功，但接口返回异常'
            else:
                # 状态码不正常
                data['status'] = False
                data['msg'] = '网络请求成功，但状态码不正常'
        else:
            # 请求失败
            data['status'] = False
            data['msg'] = '网络请求失败，请检查网络是否连通，api接口是否有效'


        self.recommend_music_finished.emit(data)
        self.finished.emit()
        return


class SearchMusic(QThread):
    search_music_finished = Signal(dict)

    # 推荐歌单线程
    def __init__(self, cloud: NeteaseCloudMusicAPI, keywords: str, page: int = 1, count: int = 30):
        super().__init__()
        self.cloud = cloud
        self.keywords = keywords
        self.page = page
        self.count = count

    def run(self):
        """获取搜索音乐内容"""

        data = {
            'status': None,
            'msg': '',
            'data': None,
        }
        search_music = self.cloud.search(keywords=self.keywords, page=self.page, count=self.count)
        if search_music['requests_status']:
            # 请求成功
            if search_music['code'] == 200:
                # 接口获取成功
                if search_music['api_return_code'] == 200:
                    # api接口返回正常
                    data['status'] = True
                    data['msg'] = '网络请求成功，接口返回成功'
                    data['data'] = search_music['data']
                else:
                    # api接口返回不正常
                    data['status'] = False
                    data['msg'] = '网络请求成功，但接口返回异常'
            else:
                # 状态码不正常
                data['status'] = False
                data['msg'] = '网络请求成功，但状态码不正常'
        else:
            # 请求失败
            data['status'] = False
            data['msg'] = '网络请求失败，请检查网络是否连通，api接口是否有效'
        self.search_music_finished.emit(data)
        self.finished.emit()
        return


class PlaylistInfo(QThread):
    # 单个歌单首页信息线程
    playlist_finished = Signal(dict)
    def __init__(self, cloud: NeteaseCloudMusicAPI, playlist_id: str, page: int, count: int):
        super().__init__()
        self.cloud = cloud
        self.playlist_id = playlist_id
        self.page = page
        self.count = count

    def run(self):
        """获取推荐的高品质歌单内容及图片"""
        data = {
            'status': None,
            'msg': '',
            'data': None,
        }
        list_info = self.cloud.playlist_info(playlist_id=self.playlist_id, page=self.page, music_count=self.count)
        if list_info['requests_status']:
            # 请求成功
            if list_info['code'] == 200:
                # 接口获取成功
                if list_info['api_return_code'] == 200:
                    # api接口返回正常
                    data['status'] = True
                    data['msg'] = '网络请求成功，接口返回成功'
                    data['data'] = list_info['data']
                else:
                    # api接口返回不正常
                    data['status'] = False
                    data['msg'] = '网络请求成功，但接口返回异常'
            else:
                # 状态码不正常
                data['status'] = False
                data['msg'] = '网络请求成功，但状态码不正常'
        else:
            # 请求失败
            data['status'] = False
            data['msg'] = '网络请求失败，请检查网络是否连通，api接口是否有效'
        self.playlist_finished.emit(data)
        self.finished.emit()
        return


class SongDownload(QThread):
    songs_download_finished = Signal(dict)

    # 下载单曲线程
    def __init__(self, cloud: NeteaseCloudMusicAPI, song_id: str):
        super().__init__()
        self.cloud = cloud
        self.song_id = song_id

    def run(self):
        """下载非vip单曲"""
        song_info = self.cloud.download_song(song_id=self.song_id)
        self.songs_download_finished.emit(song_info)
        self.finished.emit()
        return

class SaveSong(QThread):
    save_song_finished = Signal(dict)

    # 下载单曲线程
    def __init__(self, cloud: NeteaseCloudMusicAPI, song_id: str):
        super().__init__()
        self.cloud = cloud
        self.song_id = song_id

    def run(self):
        """下载非vip单曲"""
        song_info = self.cloud.save_song_v2(song_id=self.song_id)
        self.save_song_finished.emit(song_info)
        self.finished.emit()
        return
