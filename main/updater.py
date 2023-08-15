# -*- coding: UTF-8 -*-
# ////////////////////////////////
# 这是更新模块!,相关的逻辑都写在这里啦
# ////////////////////////////////

import enum
import json
import requests


class VersionStatus(enum.IntEnum):
    # 无须更新
    UpToDate = 0
    # 有新版本
    Lower = 1
    # 无下载链接
    NoLink = 2
    # error, with a str error message
    Error = 3


# 思路            (这里要判断网络是否连接 没连接就不试了
# 获得更新检查权限->检查更新 如果有新版本就发射信号并且保存好可能会用的download url ->


class ProgramUpdater(object):
    def __init__(self, now_version, version_type):
        # 需求变量
        self.version_type = version_type  # 版本类型一定要完全匹配!包括后缀名!
        self.now_version = now_version
        self.new_version = ""
        self.change_log = ""
        self.download_url = ""

    def get_latest_version(self, mode: str, api_link: str) -> tuple[VersionStatus, str | None]:
        """
        获得最新的版本号,如果有就写入self中
        :param mode: 从哪个网站获取? 目前支持解析 github gitee 处获得的
        :param api_link: 要获得的链接
        :return:0为无新版本 1为有新版本且一切正常 2为没有找到可用的新版下载链接 否则表明获得api的时候出错了
        """
        # 从api link获得后再去匹配mode
        response = requests.get(api_link)  # 获得api数据
        
        if response.status_code != 200:  # 获取了不正常的数据
            return (VersionStatus.Error, f"错误的状态码: {response.status_code}")
        
        response = json.loads(response.json())  # 得到相应的数据
        if mode in ('github', 'gitee'):
            
            if response.get("name") == self.now_version:  # 版本相等的情况
                return (VersionStatus.UpToDate, None)
            
            self.new_version = response.get("name")
            self.change_log = response.get("body")
            
            # 遍历assets以获得匹配版本类型的download_url
            assets = response.get("assets")
            
            if any(i.get("name") == self.version_type for i in assets):
                
                self.download_url = response.get("browser_download_url")
                return (VersionStatus.Lower, None)
            
            return (VersionStatus.NoLink, None)
        
        return (VersionStatus.Error, f"未知错误 {response=} {mode=} {api_link=}")