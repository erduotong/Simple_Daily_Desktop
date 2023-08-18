# -*- coding: UTF-8 -*-
# ////////////////////////////////
# 这是更新模块!,相关的逻辑都写在这里啦
# ////////////////////////////////

import enum
import json
import os.path
from concurrent.futures import ThreadPoolExecutor

import requests


class VersionStatus(enum.IntEnum):
    UpToDate = 0  # 无须更新
    Lower = 1  # 有新版本
    NoLink = 2  # 无下载链接
    Error = 3  # error


class DownloadStatus(enum.IntEnum):
    Success = 0  # 下载成功
    ErrorGetSize = 1  # 获取文件大小时出错
    ErrorDownload = 2  # 下载时出错
    ErrorWriteChunk = 3  # 写入文件块时出错


# 思路            (这里要判断网络是否连接 没连接就不试了
# 获得更新检查权限->检查更新 如果有新版本就发射信号并且保存好可能会用的download url ->
# 应用名是Simple Class Information Display!
# TODO 启动的时候要尝试删除will_delete文件夹

def download_file(destination, download_url) -> DownloadStatus:
    """
    下载新版本并在完成时改名为complete(因为没开安全认证所以会吐出来报错 不管就行了)
    :param download_url: 要下载的链接
    :param destination:下载数据保存文件的路径(包括后缀名)
    :return:状态
    """

    def download_chunk(url, file_obj, start):
        # noinspection PyBroadException
        try:
            headers = {'Range': f'bytes={start}-{start + 1024 * 1024}'}
            res = requests.get(url, headers=headers, stream=True)
        except:
            return DownloadStatus.ErrorDownload
        # noinspection PyBroadException
        try:
            file_obj.seek(start)
            file_obj.write(res.content)
        except:
            return DownloadStatus.ErrorWriteChunk
        return DownloadStatus.Success

    # noinspection PyBroadException
    try:  # 获取文件大小
        response = requests.get(download_url, stream=True, verify=False)
        file_size = int(response.headers.get('Content-Length', 0))  # 获得文件大小
    except:  # 获取的时候出现错误了
        return DownloadStatus.ErrorGetSize

    # noinspection PyBroadException
    try:  # 下载文件!
        with open(destination, 'wb') as f, ThreadPoolExecutor(max_workers=10) as executor:  # 打开目标文件并创建一个线程池
            futures = []
            for chunk_start in range(0, file_size, 1024 * 1024):  # 遍历文件的每个1MB块
                # 提交一个下载任务
                futures.append(executor.submit(download_chunk, download_url, f, chunk_start))
            for future in futures:
                result = future.result()
                if result != DownloadStatus.Success:
                    return result
    except:  # 没下成功
        return DownloadStatus.ErrorDownload

    return DownloadStatus.Success  # 成功结束!


# 源代码会特殊处理
def check_helper(mode: str, where: str) -> DownloadStatus:
    """
    检查是否有辅助程序
    :param where: 从哪儿下?(github / gitee)
    :param mode: 模式 分为source(从源代码安装的)和exe(正常安装打包的exe)
    :return:下载的状态 也就相当于检索的状态了
    """
    file_type = 'pyw' if mode == 'source' else 'exe'
    file_path = f"../data/DownloadHelper/upgrade_helper.{file_type}"
    if os.path.exists(file_path):
        return DownloadStatus.Success
    # TODO 填入下载链接
    if where == 'gitee':
        download_link = ('https://gitee.com/erduotong/Simple_Class_Information_Display/releases/download/v1.1'
                         '-upgrade_helper/upgrade_helper.pyw') if mode == 'source' else \
            ('https://gitee.com/erduotong/Simple_Class_Information_Display/releases/download/v1.1-upgrade_helper'
             '/upgrade_helper.exe')  # gitee 源代码/exe
    else:
        download_link = ('https://github.com/erduotong/Simple_Class_Information_Display/releases/download/v1.1'
                         '-upgrade_helper/upgrade_helper.pyw') if mode == 'source' else \
            ('https://github.com/erduotong/Simple_Class_Information_Display/releases/download/v1.1-upgrade_helper'
             '/upgrade_helper.exe')  # github 源代码/exe
    state = download_file(file_path, download_link)
    return state


class ProgramUpdater(object):
    def __init__(self, now_version, version_type):
        # 需求变量
        self.version_type = version_type  # 版本类型一定要完全匹配!包括后缀名!
        self.now_version = now_version
        self.new_version = None
        self.change_log = None
        self.download_url = None

    def get_latest_version(self, mode: str, api_link: str) -> VersionStatus:
        """
        获得最新的版本号,如果有就写入self中
        :param mode: 从哪个网站获取? 目前支持解析 github gitee 处获得的
        :param api_link: 要获得的链接
        :return:0为无新版本 1为有新版本且一切正常 2为没有找到可用的新版下载链接 否则表明获得api的时候出错了
        """
        # 从api link获得后再去匹配mode
        response = requests.get(api_link)  # 获得api数据
        if response.status_code != 200:  # 获取了不正常的数据
            return VersionStatus.Error
        response = json.loads(response.json())  # 得到相应的数据
        if mode in ('github', 'gitee'):
            if response.get("name") == self.now_version:  # 版本相等的情况
                return VersionStatus.UpToDate
            self.new_version = response.get("name")
            self.change_log = response.get("body")
            # 遍历assets以获得匹配版本类型的download_url
            assets = response.get("assets")
            if any(i.get("name") == self.version_type for i in assets):
                self.download_url = response.get("browser_download_url")
                return VersionStatus.Lower
            return VersionStatus.NoLink
        return VersionStatus.Error

    def download_update(self):
        pass
