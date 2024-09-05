#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################
# Author : cndaqiang             #
# Update : 2024-08-29            #
# Build  : 2024-08-29            #
# What   : 京东云无线宝领京豆     #
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


class app_jd_smartrouter():
    def __init__(self):
        self.prefix = self.__class__.__name__  # 类的名字
        # device
        self.mynode = Settings.mynode
        self.totalnode = Settings.totalnode
        self.LINK = Settings.LINK_dict[Settings.mynode]
        self.移动端 = deviceOB(mynode=self.mynode, totalnode=self.totalnode, LINK=self.LINK)
        self.设备类型 = self.移动端.设备类型
        self.APPID = "com.jdcloud.mt.smartrouter"
        self.APPOB = appOB(APPID=self.APPID, big=True, device=self.移动端)
        self.Tool = DQWheel(var_dict_file=f"{self.移动端.设备类型}.var_dict_{self.prefix}.txt",
                            mynode=self.mynode, totalnode=self.totalnode)
        #
        self.dayFILE = f"{self.prefix}.txt"
        self.timelimit = 60*10
        self.运行时间 = [3.0, 4.0]
        self.today = self.Tool.time_getweek()
        self.yesterday = (self.today-1) % 7
        self.APPOB.big = False
        #
        self.looptime = 8
    #

    def stop(self):
        self.APPOB.关闭APP()
    #

    def run(self, times=0):
        if not connect_status():
            self.移动端.连接设备()
        if times == 0:
            self.today = self.Tool.time_getweek()
            self.yesterday = (self.today-1) % 7
            try:
                self.yesterday = int(self.Tool.readfile(self.dayFILE)[0].strip())
            except:
                TimeECHO(f"未能从{self.dayFILE}中获取到上次运行时间")
            self.Tool.timelimit(timekey="RUN", limit=self.timelimit, init=True)
        #
        if self.Tool.timelimit(timekey="RUN", limit=self.timelimit, init=False):
            TimeECHO(f"{self.prefix}.运行超时")
            self.Tool.touchfile(self.dayFILE, content=str(self.yesterday))
            return
        #
        if times == 4:
            self.移动端.重启APP()
        if times > 8:
            TimeECHO("失败次数太多，停止")
            self.Tool.touchfile(self.dayFILE, content=str(self.yesterday))
            return
        #
        times = times + 1
        # 重新打开程序
        self.APPOB.重启APP()
        #
        # ------------------------------------------------------------------------------
        # 不存在对应图片则设置为None
        二级入口 = Template(r"tpl1725539964575.png", record_pos=(0.002, 0.833), resolution=(540, 960))
        主页元素 = []
        主页元素.append(Template(r"tpl1725539939012.png", record_pos=(-0.276, -0.804), resolution=(540, 960)))
        主页元素.append(二级入口)
        #
        三级入口 = Template(r"tpl1725539970386.png", record_pos=(-0.165, -0.72), resolution=(540, 960))
        #
        领取按钮 = Template(r"tpl1725539985690.png", record_pos=(0.004, 0.419), resolution=(540, 960))
        领取界面 = []
        领取界面.append(Template(r"tpl1725539977727.png", record_pos=(-0.391, -0.052), resolution=(540, 960)))
        领取界面.append(Template(r"tpl1725539982068.png", record_pos=(0.148, -0.048), resolution=(540, 960)))
        领取界面.append(领取按钮)
        # ------------------------------------------------------------------------------
        # 打开程序
        for i in range(10):
            存在, 主页元素 = self.Tool.存在任一张图(主页元素, self.prefix+"主页元素")
            if 存在:
                break
            sleep(12)
            self.APPOB.打开APP()
            存在, 主页元素 = self.Tool.存在任一张图(主页元素, self.prefix+"主页元素")
        # 检测主页
        self.Tool.存在任一张图([二级入口], self.prefix+"二级入口", savepos=True)
        self.Tool.existsTHENtouch(二级入口, self.prefix+"二级入口", savepos=True)
        #
        if 三级入口:
            self.Tool.存在任一张图([三级入口], self.prefix+"三级入口", savepos=True)
            self.Tool.existsTHENtouch(三级入口, self.prefix+"三级入口", savepos=True)
        #
        存在, 领取界面 = self.Tool.存在任一张图(领取界面, self.prefix+"领取界面")
        if not 存在:
            TimeECHO(f"{self.prefix}检测不到领取界面")
            return self.run(times)
        #
        self.Tool.存在任一张图([领取按钮], self.prefix+"领取按钮", savepos=True)
        if not self.Tool.existsTHENtouch(领取按钮, self.prefix+"领取按钮", savepos=True):
            TimeECHO(f"{self.prefix}检测不到领取按钮")
            return self.run(times)
        else:
            for i in range(10):
                # 这里再次点击是为了让程序人为我们在看, 使用领取图标的好处还有，万一被跳转了，还可以再点回来
                TimeECHO(f"{self.prefix}.模拟人手点击看广告")
                self.Tool.existsTHENtouch(领取按钮, self.prefix+"领取按钮", savepos=True)
                # 再跳转回来, 隐含sleep(20)
                self.APPOB.打开APP()
                #
                存在, 元素 = self.Tool.存在任一张图([领取按钮], self.prefix+"领取按钮", savepos=False)
                if 存在:
                    TimeECHO(f"{self.prefix}.注意, 貌似没有跳转到广告界面")
                    return self.run(times)
        #
        self.yesterday = self.today
        self.Tool.touchfile(self.dayFILE, content=str(self.yesterday))
        self.APPOB.关闭APP()
        return True
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
            for i in range(self.looptime):
                self.run()


if __name__ == "__main__":
    config_file = ""
    if len(sys.argv) > 1:
        config_file = str(sys.argv[1])
    Settings.Config(config_file)
    ce = app_jd_smartrouter()
    # 每天领取多次
    for i in range(ce.looptime):
        ce.run()
    exit()
