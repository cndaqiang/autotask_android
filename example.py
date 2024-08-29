#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################
# Author : cndaqiang             #
# Update : 2024-08-18            #
# Build  : 2024-08-18            #
# What   : 更新登录体验服         #
##################################
try:
    from airtest_mobileauto.control import *
except ImportError:
    print("模块[airtest_mobileauto]不存在, 尝试安装")
    import pip
    try:
        pip.main(['install', 'airtest_mobileauto', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple'])
    except:
        print("安装失败")
        exit(1)
import sys


class example():
    def __init__(self):
        # device
        self.mynode = Settings.mynode
        self.totalnode = Settings.totalnode
        self.LINK = Settings.LINK_dict[Settings.mynode]
        self.移动端 = deviceOB(mynode=self.mynode, totalnode=self.totalnode, LINK=self.LINK)
        self.设备类型 = self.移动端.设备类型
        self.APPID = "mark.via"
        self.APPOB = appOB(APPID=self.APPID, big=True, device=self.移动端)
        self.Tool = DQWheel(var_dict_file=f"{self.移动端.设备类型}.var_dict_{self.mynode}.ce.txt",
                            mynode=self.mynode, totalnode=self.totalnode)
        #
        prefix="example"
        self.初始化FILE=f"{prefix}.{self.mynode}初始化FILE.txt"
        self.timelimit = 60*30
        self.运行时间 = [3.0, 4.0]

    def run(self, times=0):
        if not connect_status():
            self.移动端.连接设备()
        if times == 0:
            self.Tool.timelimit(timekey="RUN", limit=self.timelimit, init=True)
        if self.Tool.timelimit(timekey="RUN", limit=self.timelimit, init=False):
            TimeECHO("RUN")
            return
        times = times + 1
        self.APPOB.打开APP()
        if times > 10 and times % 5 == 4:
            self.APPOB.重启APP()
        waittime = 10
        # ------------------------------------------------------------------------------
        run_class_command(self=self, command=self.Tool.readfile(self.初始化FILE))
        # ------------------------------------------------------------------------------
        #
        return self.run(times)
        #

    def looprun(self, times=0):
        times = times + 1
        startclock = self.运行时间[0]
        endclock = self.运行时间[1]
        while True:
            leftmin = self.Tool.hour_in_span(startclock, endclock)*60.0
            if leftmin > 0:
                TimeECHO("剩余%d分钟进入新的一天" % (leftmin))
                self.APPOB.关闭APP()
                self.移动端.重启重连设备(leftmin*60)
                continue
            times = times+1
            TimeECHO("="*10)
            self.run()


if __name__ == "__main__":
    config_file = ""
    if len(sys.argv) > 1:
        config_file = str(sys.argv[1])
    Settings.Config(config_file)
    ce = example()
    ce.run()
    exit()
