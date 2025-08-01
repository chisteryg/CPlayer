# 网易云音乐httpx版接口
import hashlib
import json
import math
import os
import sys
import time
from pprint import pprint
import asyncio
import httpx

from fake_useragent import UserAgent
from pydub import AudioSegment

# Windows 兼容性修复
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class NeteaseCloudMusicAPI:

    def __init__(self):
        self.init_var()
        pass

    def __del__(self):
        # print('析构函数被执行')
        self.async_loop.stop()
        self.async_loop.close()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭爬虫客户端
        await self.AsyncClient.aclose()

    # 初始化变量
    def init_var(self):
        # 创建一个异步爬虫对象，AsyncClient类似与session
        self.AsyncClient = httpx.AsyncClient(
            follow_redirects=True,  # 跟随重定向链接
            limits=httpx.Limits(max_connections=100, max_keepalive_connections=50),  # 设置最大连接数量，以及保持活跃的连接数量
        )
        self.headers = {
            'referer': 'https://music.163.com',
            'user-agent': self.random_ua(),
            # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
            'cookie': 'NMTID=00O9xs3UVSfPX_mWkPEuqofuqH03IoAAAGWCOtPPA; _ntes_nnid=10a8218653af2096c92703d630f8f771,1743906361470; _ntes_nuid=10a8218653af2096c92703d630f8f771; WEVNSM=1.0.0; WNMCID=gpziqp.1743906361747.01.0; WM_TID=sHZ1ri%2FeXxhFEERVVEKHPADU6cp2Nuei; sDeviceId=YD-7wnFnWBe%2BSVEVwAFQBPCKQCErMtz1avQ; __snaker__id=qP4fuODvrYRUZWMn; ntes_utid=tid._.eqe9jRgjGD1AFxFQFRaSaAHQ%252BM4zwbUO._.0; ntes_kaola_ad=1; _iuqxldmzr_=32; gdxidpyhxdE=t8XTWbgJbvR5yNyrzMsWCmtn8ni%5CdVOwDoVLfMQKOpUN2%5CTpwHPixmsAtYGNQN9uNKuZuj6DcS8XZhOhhADwvn76OG8GJJIJ9tX%2FrwuKuwB0DwmLpsS%2B3N8xQBaLT4OptspfJZZ6auC5%5CJ6rY5UX4Rrn2NJs%5CjwQcsvyUHH2kS8JODMz%3A1749654836661; __csrf=3c2174659d9ec0d46c18cabf367895c1; MUSIC_U=009FECF64D0A36B76BC7517C1D895B5AE8AF98729C58651762B0A2CC5F44E613C0F1F4AFCD0B2DA6040491236C1B8D94A12A0BD9AFB85B2698818D0496365B7E509EEAE9FA762DB5701549AA26A4BF369D25D8738746AD429D0928B4C7D45147F2675832ABD06C2F72FFF4D468511006CECD04DD4E164B80BD0FAB11CEDC6820AAC18D54580AB01972F02D75E1A4FFE7A3099BEA42D6507680C8AA165B4A44F2F8729C1E6A1BEFFA0774CCE5D7B19FA6FC58F4E2A956427554CB32FFC2022588E9BECC597F19F318923DBD92A464AEEB95447DF7A9E395A5D60BCC4C2449FEEC6B463D9AB7759289D122C2CBD72F17D31282EA9601C1467BC3F7FA114D166EB10E60279E278BCD96CDACCD12D69D819BFF9F536AFBF6DF145FF836E97C7861F15B890E4408757801D63A189A226A6D403D9D6DDE249AE0CB4C420DE37FA3F9038D41B56DA6590EDEDD53E8A7F9A678330BEB8F43E94F60E07DCC38C8CCA41802FC; JSESSIONID-WYYY=gIWqXVnVPH%5CK6eBAadKVHBN59xyZyMH8zHQ2XqlsocGnwj1iFnir%2FElGv1lMeJ55M9KVWMAVCZJD57S%5CejinJ824AiZrmW8Y6PcNir5k304m8%2F0Sgbl%2BrcKMkarPdzY0Zc2RJ0RKR%2BNzBaBdTbZE%2BAcPQqs9tigsJJP3G13kjpjZnc75%3A1749990245149; WM_NI=G1XoibRKePMU4z9Rl3Vr7%2FERQfeFW601gwyBBaqzfEb15cROdnhU%2BUAVwY1VvzPMPLyCg5rbjxFo9vEkqGxL2FXfLHAdLUhqvPuKBG96x2CmISjr1w9ZPtFyLn4J%2BCXHUXk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb3c95aafb6aea6c473879e8fa7d15e968e9a86d645bbb0ae87e64fb6ac9f84f22af0fea7c3b92a85ef9890ec6a9295abb1d05ff8a6f7b3ef3996aef9d0c85a93baaba7d63ef4efa998fc4a82bfbf9be54fa2effb84d145a8b2a8b6aa5f838ab9bab45eb6a6a0aed348bb9da9d6f16aaaa88a90bc7e87b5bfa8fb48f29a9887cf4483bc84b6eb7bb690bbacc14dfbeab8d3c2678b8da693b47dfb86a095c57390b2fcabaa499c989bb9ea37e2a3'
        }

        # 创建异步事件循环
        self.async_loop = asyncio.get_event_loop()
        # # 初始化连接
        # self.init_client()
        return

    def init_client(self):
        # 向163发送一条请求，初步创建client长连接对象
        url = 'https://music.163.com/'
        self.async_function(self.get_url(url))
        self.headers['referer'] = 'https://music.163.com/'

    def async_function(self, function):
        # 执行异步函数并获取结果
        loop = self.async_loop
        task = self.async_loop.create_task(function)
        loop.run_until_complete(task)
        return task.result()

    async def get_url(self, url: str) -> dict:
        """异步get请求单个 URL"""
        try:
            response = await self.AsyncClient.get(url, headers=self.headers, timeout=self.timeout)
            response_data = {
                'requests_status': True,
                'code': response.status_code,
                'data': response
            }
            return response_data
        except Exception as e:
            response_data = {
                'requests_status': False,
                'exception': str(e),
                'data': None
            }
            return response_data

    async def post_url(self, url: str, data: dict) -> dict:
        """异步post请求单个 URL"""
        try:
            response = await self.AsyncClient.post(url, headers=self.headers, data=data, timeout=self.timeout)
            response_data = {
                'requests_status': True,
                'code': response.status_code,
                'data': response
            }
            return response_data
        except Exception as e:
            response_data = {
                'requests_status': False,
                'exception': str(e),
                'data': None
            }
            return response_data

    async def async_download_large_file(self, url: str, save_path: str, chunk_size: int = 1024 * 1024):
        """异步流式下载文件"""
        try:
            # 发起流式请求
            async with self.AsyncClient.stream("GET", url) as response:
                response.raise_for_status()  # 检查 HTTP 状态码
                # 获取文件总大小（可选，用于进度条）
                total_size = int(response.headers.get("Content-Length", 0))
                # 分块写入文件
                with open(save_path, "wb") as f:
                    async for chunk in response.aiter_bytes(chunk_size):
                        f.write(chunk)
                        # print(len(chunk))
                        # print(1024*1024)

                print(f"文件已保存至: {save_path}")
                return save_path
        except httpx.HTTPError as e:
            print(f"请求失败: {str(e)}")
            return ''
        except IOError as e:
            print(f"文件写入错误: {str(e)}")
            return ''
        except Exception as e:
            print(e)
            return ''

    async def get_pic(self, key: str, url: str, size: int = 50) -> list:
        """异步请求单个图片"""
        # 生成图片目录
        pic_dir = self.PicDir
        self.generate_dir(pic_dir)
        try:
            save_path = pic_dir + url.split('/')[-1]
            url = url + f'?{size}y{size}'
            response = await self.AsyncClient.get(url, headers=self.headers, timeout=self.timeout)
            with open(save_path, 'wb') as f:
                f.write(response.content)
            result = [key, save_path]
            return result
        except Exception as e:
            print(e)
            return []

    async def get_pics(self, urls_dict: dict, size: int = 50):
        # 异步批量爬取图片
        '''
        {
            '0': {'url': 'xxxxx'}
        }
        '''
        result = urls_dict
        task = []
        for key in urls_dict.keys():
            task.append(self.get_pic(key, urls_dict[key]['url'], size))
        results = await asyncio.gather(*task)
        for result1 in results:
            key = result1[0]
            result[key]['save_path'] = result1[1]
            # print(result)
        return result

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 推荐音乐相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    def recommend_music_info(self) -> dict:
        # 每日推荐音乐
        url = 'https://music.163.com/api/v3/discovery/recommend/songs'
        result = self.async_function(self.get_url(url=url))
        if result['requests_status'] and result['code'] == 200:
            # 请求成功
            data = json.loads(result['data'].text)
            result['api_return_code'] = data['code']
            if data['code'] == 200:
                # 接口返回成功
                # 重新构建字典，筛选所需数据
                recommend_music = {}
                # 批量音乐图片url字典
                img_url_dict = {}
                # 接口返回值为200，请求正确，筛选所需数据
                i = 1
                for item in data['data']['dailySongs']:
                    # music_id
                    music_id = str(item['id'])
                    recommend_music[str(i)] = {}
                    recommend_music[str(i)]['id'] = music_id
                    # 图片地址
                    recommend_music[str(i)]['picUrl'] = item['al']['picUrl']
                    img_url_dict[str(i)] = {}
                    img_url_dict[str(i)]['url'] = item['al']['picUrl']
                    # 歌手
                    recommend_music[str(i)]['ar'] = item['ar']
                    # 时长
                    recommend_music[str(i)]['dt'] = item['dt']
                    # 名称
                    recommend_music[str(i)]['name'] = item['name']
                    # 是否为vip
                    recommend_music[str(i)]['vip'] = True if item['fee'] == 1 else False
                    i += 1

                # 批量爬取音乐图片
                imgs_path = self.async_function(self.get_pics(img_url_dict))
                for key in imgs_path.keys():
                    recommend_music[key]['img_path'] = imgs_path[key]['save_path']

                result['data'] = recommend_music
            else:
                result['data'] = None

        return result

    # 推荐音乐
    def old_recommend_music_info(self) -> dict:
        url = 'https://music.163.com/api/personalized/newsong'
        result = self.async_function(self.get_url(url=url))
        if result['requests_status'] and result['code'] == 200:
            # 请求成功
            data = json.loads(result['data'].text)
            result['api_return_code'] = data['code']
            if data['code'] == 200:
                # 接口返回成功
                # 重新构建字典，筛选所需数据
                recommend_music = {}
                # 批量音乐图片url字典
                img_url_dict = {}
                i = 1
                for item in data['result']:
                    # music_id
                    recommend_music[i] = {}
                    recommend_music[i]['id'] = item['id']
                    # 图片地址
                    recommend_music[i]['picUrl'] = item['picUrl']
                    img_url_dict[i] = {}
                    img_url_dict[i]['url'] = item['picUrl']
                    # 歌手
                    recommend_music[i]['ar'] = item['song']['artists']
                    # 时长
                    recommend_music[i]['dt'] = item['song']['duration']
                    # 名称
                    recommend_music[i]['name'] = item['song']['name']
                    i += 1

                # 批量爬取音乐图片
                imgs_path = self.async_function(self.get_pics(img_url_dict))
                for key in imgs_path.keys():
                    recommend_music[key]['img_path'] = imgs_path[key]['save_path']
                result['data'] = recommend_music
            else:
                result['data'] = None

        return result

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 推荐音乐相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 单首音乐相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    def song_detail(self, song_id: str) -> dict:
        # 单首音乐信息
        url = 'https://music.163.com/api/song/detail'
        # 查询参数
        data = {
            "id": f"{song_id}",
            "ids": f"[{song_id}]",
            "limit": 10000,
            "offset": 0
        }
        result = self.async_function(self.post_url(url=url, data=data))

        if result['requests_status'] and result['code'] == 200:
            # 请求成功
            data = json.loads(result['data'].text)
            result['api_return_code'] = data['code']
            if data['code'] == 200:
                # 接口返回成功
                # 筛选数据
                data = data['songs'][0]
                song_detail = {}
                song_detail['id'] = data['id']
                # mvid，如有则展示id，没有为空字符串
                song_detail['mvid'] = data['mvid']
                # 是否为vip
                song_detail['vip'] = True if data['fee'] == 1 else False
                # 图片地址
                song_detail['picUrl'] = data['album']['picUrl']
                if data['album']['picUrl']:
                    song_detail['img_path'] = self.async_function(self.get_pic('0', data['album']['picUrl']))[1]
                else:
                    song_detail['img_path'] = None
                # 歌手
                song_detail['ar'] = data['artists']
                # 时长
                song_detail['dt'] = data['duration']
                # 名称
                song_detail['name'] = data['name']
                # 歌词
                lrc = self.song_lyric(song_id)
                song_detail['lyric'] = lrc['data']
                # 比特率
                song_detail['br'] = self.find_all_values(data, 'bitrate')
                song_detail['max_br'] = max(self.find_all_values(data, 'bitrate'))
                result['data'] = song_detail
            else:
                result['data'] = None

        return result

    def songs_detail(self, music_id_list: list[str]) -> dict:
        url = 'https://music.163.com/api/song/detail'
        # 查询参数
        data = {
            "ids": f'{music_id_list}'
        }
        result = self.async_function(self.post_url(url=url, data=data))
        # print(result)
        if result['requests_status'] and result['code'] == 200:
            # 请求成功
            data = json.loads(result['data'].text)
            result['api_return_code'] = data['code']
            if data['code'] == 200:
                # 接口返回成功
                data = data['songs']

                songs_detail = {}
                img_url_dict = {}
                i = 1
                for item in data:
                    # music_id
                    music_id = str(item['id'])
                    songs_detail[str(i)] = {}
                    songs_detail[str(i)]['id'] = music_id
                    # mvid，如有则展示id，没有为空字符串
                    songs_detail[str(i)]['mvid'] = item['mvid']
                    # 是否为vip
                    songs_detail[str(i)]['vip'] = True if item['fee'] == 1 else False
                    # 图片地址
                    songs_detail[str(i)]['picUrl'] = item['album']['picUrl']
                    img_url_dict[str(i)] = {}
                    img_url_dict[str(i)]['url'] = item['album']['picUrl']
                    # 歌手
                    songs_detail[str(i)]['ar'] = item['artists']
                    # 时长
                    songs_detail[str(i)]['dt'] = item['duration']
                    # 名称
                    songs_detail[str(i)]['name'] = item['name']
                    # 比特率
                    songs_detail[str(i)]['br'] = self.find_all_values(item, 'bitrate')
                    songs_detail[str(i)]['max_br'] = max(self.find_all_values(item, 'bitrate'))

                    i += 1
                imgs_path = self.async_function(self.get_pics(img_url_dict))
                for key in imgs_path.keys():
                    songs_detail[key]['img_path'] = imgs_path[key]['save_path']

                result['data'] = songs_detail
            else:
                result['data'] = None
        return result

    def song_lyric(self, song_id) -> dict:
        # 获取单曲歌词
        url = f'http://music.163.com/api/song/lyric?os=osx&id={song_id}&lv=-1&kv=-1&tv=-1'
        result = self.async_function(self.get_url(url=url))
        if result['requests_status'] and result['code'] == 200:
            # 请求成功
            data = json.loads(result['data'].text)
            result['api_return_code'] = data['code']
            if data['code'] == 200:
                # 接口返回成功

                try:
                    if '[' in data['lrc']['lyric'] and ']' in data['lrc']['lyric']:
                        # 判断歌词是否规范
                        result['data'] = data['lrc']['lyric']
                except Exception as e:
                    result['data'] = None
            else:
                result['data'] = None

        return result

    def download_song(self, song_id) -> dict:
        # 下载单曲
        result = {}
        # 获取音乐信息
        detail = self.song_detail(song_id)
        result['song_detail'] = detail['data']

        # 通过接口方式获取高品质音乐下载地址
        # 音乐下载地址，level代表音质等级，encodeType代表编码类型，flac可存储无损音质，目前无法下载无损音乐
        # 音质 standard标准 higher较高 exhigh极高 lossless无损 hires
        # 编码类型 aac flac
        # url = f'https://music.163.com/api/song/enhance/player/url/v1?ids=[{song_id}]&level=hires&encodeType=flac'
        url = f'https://music.163.com/api/song/enhance/player/url/v1?ids=[{song_id}]&level=exhigh&encodeType=acc'
        download_url = json.loads(self.async_function(self.get_url(url=url))['data'].text)
        music_path = None
        if download_url['code'] == 200:
            # 接口获取成功
            # 音乐类型
            music_type = download_url['data'][0]['type']
            # 下载地址
            url = download_url['data'][0]['url']
            # url.replace('http', 'https')
            music_path = self.MusicDir + f'/{song_id}.{music_type}'
            # 流式下载
            music_path = self.async_function(self.async_download_large_file(url=url, save_path=music_path))
            # 音乐时长
            result['dt'] = download_url['data'][0]['time']
            # 音质
            result['level'] = download_url['data'][0]['level']
            # 比特率
            result['br'] = download_url['data'][0]['br']

        result['music_save_path'] = music_path

        return result

    def save_song(self, song_id) -> dict:
        # 下载单曲（外链播放器）
        result = {}
        # 获取音乐信息
        detail = self.song_detail(song_id)
        result['song_detail'] = detail['data']

        music_name = result['song_detail']['name']

        # 生成音乐存放目录
        self.generate_dir(self.MusicDir)

        # 保存歌词
        lrc_path = self.MusicDir + f'/{music_name}.lrc'
        lrc = result['song_detail']['lyric']
        with open(lrc_path, 'w', encoding='utf-8') as f:
            f.write(lrc)
        result['lrc_save_path'] = lrc_path

        # 下载音乐
        url = f'http://music.163.com/song/media/outer/url?id={song_id}.mp3'
        music_path = self.MusicDir + f'/{music_name}.mp3'
        # 流式下载
        music_path = self.async_function(self.async_download_large_file(url=url, save_path=music_path))
        result['music_save_path'] = music_path

        return result

    def save_song_v2(self, song_id) -> dict:
        # 下载单曲（接口）
        # 音乐下载地址，level代表音质等级，encodeType代表编码类型，flac可存储无损音质，目前无法下载无损音乐
        # 音质 standard标准 higher较高 exhigh极高 lossless无损 hires
        # 编码类型 aac flac
        result = {}
        # 获取音乐信息
        detail = self.song_detail(song_id)
        result['song_detail'] = detail['data']

        music_name = result['song_detail']['name']

        # 生成音乐存放目录
        self.generate_dir(self.MusicDir)

        # 保存歌词
        lrc_path = self.MusicDir + f'/{music_name}.lrc'
        lrc = result['song_detail']['lyric']
        if lrc is not None:
            with open(lrc_path, 'w', encoding='utf-8') as f:
                f.write(lrc)
        result['lrc_save_path'] = lrc_path

        # 通过接口获取高品质音乐下载地址
        url = f'https://music.163.com/api/song/enhance/player/url/v1?ids=[{song_id}]&level=hires&encodeType=flac'
        download_url = json.loads(self.async_function(self.get_url(url=url))['data'].text)
        music_path = None
        pprint(download_url)
        if download_url['code'] == 200:
            # 接口获取成功
            # 音乐类型
            music_type = download_url['data'][0]['type']
            # 下载地址
            url = download_url['data'][0]['url']
            # url.replace('http', 'https')
            music_path = self.MusicDir + f'/{music_name}.{music_type}'
            # 流式下载
            music_path = self.async_function(self.async_download_large_file(url=url, save_path=music_path))
            # 音乐时长
            result['dt'] = download_url['data'][0]['time']
            # 音质
            result['level'] = download_url['data'][0]['level']
            # 比特率
            result['br'] = download_url['data'][0]['br']

        result['music_save_path'] = music_path

        return result

    def save_song_v3(self, song_id) -> dict:
        # 下载单曲（接口）
        # 音乐下载地址，level代表音质等级，encodeType代表编码类型，flac可存储无损音质，目前无法下载无损音乐
        # 音质 standard标准 higher较高 exhigh极高 lossless无损 hires
        # 编码类型 aac flac
        result = {}
        # 获取音乐信息
        detail = self.song_detail(song_id)

        result['song_detail'] = detail['data']

        music_name = result['song_detail']['name']

        # 生成音乐存放目录
        self.generate_dir(self.MusicDir)

        # 保存歌词
        lrc_path = self.MusicDir + f'/{music_name}.lrc'
        lrc = result['song_detail']['lyric']
        if lrc is not None:
            with open(lrc_path, 'w', encoding='utf-8') as f:
                f.write(lrc)
        result['lrc_save_path'] = lrc_path

        music_path = None
        try:
            # 通过接口获取音乐下载url
            br = detail['data']['max_br']
            url = f'https://music.163.com/api/song/enhance/player/url?ids=["{song_id}"]&br={br}'
            download_info = json.loads(self.async_function(self.get_url(url=url))['data'].text)
            music_type = download_info['data'][0]['type']
            download_url = download_info['data'][0]['url']
        except Exception as e:
            print(e)

        # result['music_save_path'] = music_path

        return result

    def song_comments(self, song_id, offset: int = 0, limit: int = 30) -> dict:
        # 单曲评论
        url = f'https://music.163.com/api/v1/resource/comments/R_SO_4_{song_id}'
        # 查询参数
        data = {
            'rid': song_id,
            'offset': offset,
            'total': 'total',
            'limit': limit
        }
        result = self.async_function(self.post_url(url=url, data=data))
        if result['requests_status'] and result['code'] == 200:
            # 请求成功
            data = json.loads(result['data'].text)
            result['api_return_code'] = data['code']
            if data['code'] == 200:
                # 接口返回成功
                result['data'] = data
            else:
                result['data'] = None
        return result

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 单首音乐相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 歌单相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    def playlist_info(self, playlist_id, page: int = 1, music_count: int = 50) -> dict:
        # v2版歌单内容获取，可获取所有歌曲id，但详细内容限制只有前10首

        url = f'https://music.163.com/api/v1/playlist/detail?id={playlist_id}'
        result = self.async_function(self.get_url(url=url))
        if result['requests_status'] and result['code'] == 200:
            # 请求成功
            data = json.loads(result['data'].text)
            result['api_return_code'] = data['code']
            if data['code'] == 200:
                # 接口返回成功
                data = data['playlist']

                playlist_info = {}
                # 背景图片
                playlist_info['coverImgUrl'] = data['coverImgUrl']
                playlist_info['img_path'] = self.async_function(self.get_pic('0', data['coverImgUrl']))[1]
                # 描述
                playlist_info['description'] = data['description']
                # id
                playlist_info['id'] = data['id']
                # 名称
                playlist_info['name'] = data['name']
                # 播放量
                playlist_info['playCount'] = data['playCount']
                # 收藏量
                playlist_info['subscribedCount'] = data['subscribedCount']

                # 音乐数量

                playlist_info['trackCount'] = data['trackCount']
                # 页数
                playlist_info['page'] = page
                playlist_info['max_page'] = math.ceil(data['trackCount'] / music_count)

                # 歌单中所有音乐的id
                playlist_info['trackIds'] = []
                for item in data['trackIds']:
                    playlist_info['trackIds'].append(str(item['id']))

                # 提取前指定首音乐详细内容
                songs_detail = {
                    'data': {}
                }
                # 起始下标
                start_index = (page - 1) * music_count
                # 结束下标
                end_index = start_index + music_count

                if start_index <= len(playlist_info['trackIds']):
                    # 起始下标在范围内
                    music_id_list = playlist_info['trackIds'][start_index:end_index]
                    if end_index > len(playlist_info['trackIds']):
                        # 但是结束下标不在范围内
                        music_id_list = playlist_info['trackIds'][start_index:]
                    songs_detail = self.songs_detail(music_id_list)

                # pprint(playlist_info)
                # 音乐的详细内容
                playlist_info['songs_detail'] = {}
                playlist_info['songs_detail'][str(page)] = songs_detail['data']

                result['data'] = playlist_info
            else:
                result['data'] = None

        return result

    def recommend_playlist(self, count: int = 35, page: int = 1, cat: str = '全部') -> dict:
        '''
        每日推荐歌单
        :param count: 获取数量
        :param page: 页数
        :param cat: 风格
        :return:
        '''

        cat_dict = {
            '语种': {
                '1': '华语',
                '2': '欧美',
                '3': '日语',
                '4': '韩语',
                '5': '粤语',
            },
            '风格': {
                '1': '流行',
                '2': '摇滚',
                '3': '民谣',
                '4': '电子',
                '5': '舞曲',
                '6': '说唱',
                '7': '轻音乐',
                '8': '爵士',
                '9': '乡村',
                '10': 'R&B/Soul',
                '11': '古典',
                '12': '民族',
                '13': '英伦',
                '14': '金属',
                '15': '朋克',
                '16': '蓝调',
                '17': '雷鬼',
                '18': '世界音乐',
                '19': '拉丁',
                '20': 'New Age',
                '21': '古风',
                '22': '后摇',
                '23': 'Bossa Nova',

            },
            '场景': {
                '1': '清晨',
                '2': '夜晚',
                '3': '学习',
                '4': '工作',
                '5': '午休',
                '6': '下午茶',
                '7': '地铁',
                '8': '驾车',
                '9': '运动',
                '10': '旅行',
                '11': '散步',
                '12': '酒吧',
            },
            '情感': {
                '1': '怀旧',
                '2': '清新',
                '3': '浪漫',
                '4': '伤感',
                '5': '治愈',
                '6': '放松',
                '7': '孤独',
                '8': '感动',
                '9': '兴奋',
                '10': '快乐',
                '11': '安静',
                '12': '思念',
            },
            '主题': {
                '1': '综艺',
                '2': '影视原声',
                '3': 'ACG',
                '4': '儿童',
                '5': '校园',
                '6': '游戏',
                '7': '70后',
                '8': '80后',
                '9': '90后',
                '10': '网络歌曲',
                '11': 'KTV',
                '12': '经典',
                '13': '翻唱',
                '14': '吉他',
                '15': '钢琴',
                '16': '器乐',
                '17': '榜单',
                '18': '00后',
            },
        }

        # cat = 'Bossa Nova'

        limit = count
        offset = (page - 1) * count

        url = f'https://music.163.com/api/playlist/list?order=hot&limit={limit}&offset={offset}&cat={cat}'

        result = self.async_function(self.get_url(url=url))
        if result['requests_status'] and result['code'] == 200:
            # 请求成功
            data = json.loads(result['data'].text)
            result['api_return_code'] = data['code']
            if data['code'] == 200:
                # 接口返回成功
                # 筛选所需数据
                data = json.loads(result['data'].text)
                playlist_info = {
                    'playlist': {
                        str(page): {}
                    },
                    'total': data['total'],  # 歌单数量
                    'count': count,
                    'page': page,
                    'max_page': math.ceil(data['total'] / count),
                    'cat': cat,
                }
                img_url_dict = {}
                data = data['playlists']

                # 筛选所需内容
                i = 1
                for item in data:
                    playlist_info['playlist'][str(page)][str(i)] = {}
                    # 歌单图片
                    playlist_info['playlist'][str(page)][str(i)]['picUrl'] = item['coverImgUrl']
                    img_url_dict[str(i)] = {}
                    img_url_dict[str(i)]['url'] = item['coverImgUrl']
                    # 创建者
                    playlist_info['playlist'][str(page)][str(i)]['creator'] = {}
                    playlist_info['playlist'][str(page)][str(i)]['creator']['avatarUrl'] = item['creator']['avatarUrl']
                    playlist_info['playlist'][str(page)][str(i)]['creator']['signature'] = item['creator']['signature']
                    playlist_info['playlist'][str(page)][str(i)]['creator']['name'] = item['creator']['nickname']
                    playlist_info['playlist'][str(page)][str(i)]['creator']['id'] = item['creator']['userId']
                    # 歌单名称
                    playlist_info['playlist'][str(page)][str(i)]['name'] = item['name']
                    # 歌单id
                    playlist_info['playlist'][str(page)][str(i)]['id'] = item['id']
                    # 播放量
                    playlist_info['playlist'][str(page)][str(i)]['playcount'] = item['playCount']
                    i += 1
                # pprint(playlist_info)
                imgs_path = self.async_function(self.get_pics(img_url_dict))
                for key in imgs_path.keys():
                    playlist_info['playlist'][str(page)][key]['img_path'] = imgs_path[key]['save_path']

                result['data'] = playlist_info
            else:
                result['data'] = None

        return result

    def highquality_recommend_playlist(self, limit: int = 100):
        # 精品歌单推荐（最多100条）
        url = f'https://music.163.com/api/playlist/highquality/list?limit={limit}'
        result = self.async_function(self.get_url(url=url))
        if result['status'] and result['code'] == 200:
            result = json.loads(result['data'].text)
            result = result['playlists']
            # 筛选所需数据
            playlist_info = {}
            img_url_dict = {}
            # 筛选所需内容
            i = 1
            for item in result:
                # pprint(item)
                playlist_info[str(i)] = {}
                # 歌单图片
                playlist_info[str(i)]['coverImgUrl'] = item['coverImgUrl']
                img_url_dict[str(i)] = {}
                img_url_dict[str(i)]['url'] = item['coverImgUrl']
                # 创建者
                playlist_info[str(i)]['creator'] = {}
                playlist_info[str(i)]['creator']['avatarUrl'] = item['creator']['avatarUrl']
                playlist_info[str(i)]['creator']['signature'] = item['creator']['signature']
                playlist_info[str(i)]['creator']['name'] = item['creator']['nickname']
                playlist_info[str(i)]['creator']['id'] = item['creator']['userId']
                # 歌单简介
                playlist_info[str(i)]['description'] = item['description']
                # 歌单名称
                playlist_info[str(i)]['name'] = item['name']
                # 歌单id
                playlist_info[str(i)]['id'] = item['id']
                # 播放量
                playlist_info[str(i)]['playCount'] = item['playCount']
                # 收藏量
                playlist_info[str(i)]['subscribedCount'] = item['subscribedCount']
                i += 1

            imgs_path = self.async_function(self.get_pics(img_url_dict))
            for key in imgs_path.keys():
                playlist_info[key]['img_path'] = imgs_path[key]['save_path']

            return playlist_info
        return False

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 歌单相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 搜索相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    # 单曲搜索
    def search(self, keywords: str, count: int = 20, page: int = 1) -> dict:
        # type搜索单曲(1)，歌手(100)，专辑(10)，歌单(1000)，用户(1002) *(type)*
        type = 1
        limit = count
        offset = (page - 1) * count
        url = f'https://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={keywords}&type={type}&offset={offset}&total=true&limit={limit}'
        result = self.async_function(self.get_url(url=url))
        if result['requests_status'] and result['code'] == 200:
            # 请求成功
            data = json.loads(result['data'].text)
            result['api_return_code'] = data['code']
            if data['code'] == 200:
                # 接口返回成功
                data = data['result']
                # 筛选所需数据
                music_info = {
                    'count': count,
                    'keywords': keywords,
                    'page': page,
                    'max_page': math.ceil(data['songCount'] / count),
                    'total': data['songCount'],
                    'songs_detail': {},
                }
                # 获取音乐详细信息
                music_list = []
                for item in data['songs']:
                    music_list.append(str(item['id']))
                music_info['songs_detail'][str(page)] = self.songs_detail(music_list)['data']

                result['data'] = music_info
            else:
                result['data'] = None
        return result

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 搜索相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ mv相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    def mv_details(self, mvid: str = '522365') -> dict:
        # mv信息（下载地址）
        url = f'https://music.163.com/api/mv/detail?id={mvid}&type=mp4'
        result = self.async_function(self.get_url(url=url))

        if result['requests_status'] and result['code'] == 200:
            # 请求成功
            data = json.loads(result['data'].text)
            result['api_return_code'] = data['code']
            if data['code'] == 200:
                # 接口返回成功
                data = data['data']
                # 筛选所需数据
                mv_details = {}
                # id
                mv_details['id'] = data['id']
                # 歌手
                mv_details['ar'] = data['artists']
                # 下载链接
                mv_details['brs'] = data['brs']
                # 图片
                mv_details['cover'] = data['cover']
                mv_details['img_path'] = self.async_function(self.get_pic('0', data['cover']))[1]
                # 简介
                mv_details['desc'] = data['desc']
                # 时长
                mv_details['dt'] = data['duration']
                # 名称
                mv_details['name'] = data['name']
                # 播放量
                mv_details['playCount'] = data['playCount']
                # 发布时间
                mv_details['publishTime'] = data['publishTime']

                result['data'] = mv_details
            else:
                result['data'] = None
        return result

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ mv相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ 云盘相关方法 ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

    def cloud_info(self, page: int = 1, count: int = 30) -> dict:
        # 用户云盘内容（音乐直接根据id下载）
        limit = count
        offset = (page - 1) * count

        url = f'https://music.163.com/api/v1/cloud/get?limit={limit}&offset={offset}'
        result = self.async_function(self.get_url(url=url))
        if result['requests_status'] and result['code'] == 200:
            # 请求成功
            data = json.loads(result['data'].text)
            pprint(data)
            result['api_return_code'] = data['code']
            if data['code'] == 200:
                # 接口返回成功
                # 筛选所需数据
                cloud_info = {}
                img_url_dict = {}
                # 云盘音乐总数
                cloud_info['count'] = data['count']
                # 云盘音乐页数
                cloud_info['page'] = page
                # 云盘音乐最大页数
                cloud_info['max_page'] = math.ceil(data['count'] / count)

                #
                cloud_info['songs'] = {}
                data = data['data']

                i = 1
                for item in data:
                    cloud_info['songs'][i] = {}
                    # 文件名称
                    cloud_info['songs'][i]['songName'] = item['songName']
                    # 专辑图片
                    cloud_info['songs'][i]['picUrl'] = item['simpleSong']['al']['picUrl']
                    img_url_dict[i] = {}
                    img_url_dict[i]['url'] = item['simpleSong']['al']['picUrl']
                    # 歌手
                    cloud_info['songs'][i]['artist'] = item['artist']
                    # 时长
                    cloud_info['songs'][i]['dt'] = item['simpleSong']['dt']
                    # 音乐名称
                    cloud_info['songs'][i]['name'] = item['simpleSong']['name']
                    # id
                    cloud_info['songs'][i]['songId'] = item['songId']
                    i += 1
                # pprint(img_url_dict)
                imgs_dict = self.async_function(self.get_pics(urls_dict=img_url_dict))
                for key in imgs_dict:
                    cloud_info['songs'][key]['img_path'] = imgs_dict[key]['save_path']

                result['data'] = cloud_info

            else:
                result['data'] = None
        return result

    def cloud_upload(self) -> dict:
        file_path = '../player/1.flac'
        # 加载音频文件
        audio = AudioSegment.from_file(file_path)

        # 获取时长（毫秒）
        duration_ms = len(audio)

        # 获取比特率（kbps）
        bit_rate = audio.frame_rate * audio.sample_width * 8 * audio.channels

        # 获取md5
        md5 = self.get_file_md5(file_path)

        # 检测是否需要上传文件
        url = 'https://interface.music.163.com/api/cloud/upload/check'
        data = {
            'bitrate': str(bit_rate),
            'ext': '',
            'length': duration_ms,
            'md5': md5,
            'songId': '0',
            'version': 1,
        }

        data = self.async_function(self.post_url(url=url, data=data))
        # pprint(data)
        data = json.loads(data['data'].text)
        # 获取songId后续上传使用
        song_id = data['songId']
        pprint(data)

        # 获取上传token
        url = 'https://music.163.com/api/nos/token/alloc'
        data = {
            'bucket': '',
            'ext': 'flac',
            'filename': '1.flac',
            'local': False,
            'nos_product': 3,
            'type': 'audio',
            'md5': md5,
        }

        data = self.async_function(self.post_url(url=url, data=data))
        data = json.loads(data['data'].text)
        pprint(data)
        # 获取resourceId， 后续上传使用
        resourceId = data['result']['resourceId']

        # 上传
        url = 'https://music.163.com/api/upload/cloud/info/v2'
        data = {
            'md5': md5,
            'songid': song_id,
            'filename': '1.flac',  # 文件名
            'song': '1.flac',  # 音乐名
            'album': '未知专辑',
            'artist': '未知艺术家',
            'bitrate': str(bit_rate),
            'resourceId': resourceId,
        }
        data = self.async_function(self.post_url(url=url, data=data))
        data = json.loads(data['data'].text)
        # 获取音乐id供上传使用
        songId = data['songId']
        pprint(data)

        url = 'https://interface.music.163.com/api/cloud/pub/v2'
        data = {
            'songid': songId,
        }
        data = self.async_function(self.post_url(url=url, data=data))
        data = json.loads(data['data'].text)
        pprint(data)
        # print(duration_sec, bitrate, md5)

        return {}

    def get_file_md5(self, file_path):
        """计算文件的 MD5 哈希值"""
        with open(file_path, 'rb') as f:
            file_data = f.read()
            return hashlib.md5(file_data).hexdigest()
    def cloud_del(self, song_id: str) -> dict:
        # 删除云盘音乐
        url = f'https://music.163.com//api/cloud/del?songIds=[{song_id}]'
        result = self.async_function(self.get_url(url=url))
        if result['requests_status'] and result['code'] == 200:
            # 请求成功
            data = json.loads(result['data'].text)
            result['api_return_code'] = data['code']
            if data['code'] == 200:
                # 接口返回成功
                '''
                成功删除返回示例
                {'succIds': [26600702], 'failIds': [], 'code': 200}
                '''
                data = json.loads(result['data'].text)
                result['data'] = data
            else:
                result['data'] = None
        return result

    '''↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ 云盘相关方法 ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑'''

    '''工具方法'''

    def set_cookies(self, cookies: str):
        # 请求头中设置cookies
        self.headers['cookie'] = cookies
        return

    def set_save_path(self, save_path: str):
        # 设置保存路径
        self.MusicDir = save_path
        return

    # 生成随机UA
    def random_ua(self):
        return UserAgent().random

    # 生成目录
    def generate_dir(self, dir_name: str):
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        return

    def find_all_values(self, data, target_key):
        """
        递归遍历字典和列表，收集所有目标键对应的值。

        :param data: 要遍历的数据（字典、列表等）
        :param target_key: 目标键名
        :return: 所有匹配的值的列表
        """
        results = []

        # 如果是字典，遍历键值对
        if isinstance(data, dict):
            for key, value in data.items():
                # 如果当前键匹配目标键，收集值
                if key == target_key:
                    results.append(value)
                # 递归遍历值（可能是嵌套结构）
                results.extend(self.find_all_values(value, target_key))

        # 如果是列表或元组，遍历元素
        elif isinstance(data, (list, tuple)):
            for item in data:
                results.extend(self.find_all_values(item, target_key))

        # 其他类型（如字符串、数字）不处理
        return results

    timeout = 10
    MusicDir = './music'
    PicDir = './pic/'
    ChunkSize = 1024 * 1024 * 10

    '''https://music.163.com/api/w/user/safe/bindings/495748490'''


if __name__ == '__main__':
    'http://music.163.com/song/media/outer/url?id=ID数字.mp3'
    n = NeteaseCloudMusicAPI()
    t1 = time.time()
    # music_id_list = [
    #     '1875993690',
    #     '189688',
    #     '29774171',
    #     '407759199',
    #     '411214279',
    #
    #     '20531567',
    #     '1296753761',
    #     '20531567',
    #     '186014',
    #     '2526625',
    # ]
    # pprint(n.songs_detail(music_id_list))
    # pprint(n.song_detail('26609877'))
    # # pprint(n.song_comments('26609877', offset=50))
    # # pprint(n.playlist_info('2701866695'))
    # # pprint(n.search('林俊杰'))
    # pprint(n.playlist_info('331841455', page=2, music_count=10))
    # pprint(n.save_song('2688097771'))
    # pprint(n.save_song_v2('40558833'))
    # pprint(n.cloud_info())
    pprint(n.cloud_upload())
    print(time.time() - t1)
