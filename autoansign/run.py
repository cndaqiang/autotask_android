#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################
# Author : cndaqiang             #
# Update : 2024-08-29            #
# Build  : 2024-08-29            #
# What   : 领取所有签到红包       #
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
import importlib

class autotask_android():
    def __init__(self):
        self.prefix=self.__class__.__name__ # 类的名字
        # device
        self.mynode = Settings.mynode
        self.totalnode = Settings.totalnode
        self.LINK = Settings.LINK_dict[Settings.mynode]
        self.移动端 = deviceOB(mynode=self.mynode, totalnode=self.totalnode, LINK=self.LINK)
        self.设备类型 = self.移动端.设备类型
        self.Tool = DQWheel(var_dict_file=f"{self.移动端.设备类型}.var_dict_{self.prefix}.yaml",
                            mynode=self.mynode, totalnode=self.totalnode)
        #
        self.内置循环FILE =f"{self.prefix}.loop.txt"  # 采用本脚本自带的循环。
        self.timelimit = 60*10
        self.运行时间 = [0.01, 23.5]
        # 模块
        py_files = []
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith('.py') and not file.startswith('run.'):
                    #筛选模块
                    #_m.py结尾的是高分辨率手机的模块
                    # 获取当前脚本的完整路径
                    script_name = os.path.basename(__file__)
                    if file.endswith('_m.py') and script_name == "run.m.py":
                        pass
                    elif not file.endswith('_m.py') and script_name == "run.py":
                        pass
                    else:
                        continue
                    #
                    # 使用os.path.splitext()去除扩展名
                    file_name_without_extension = os.path.splitext(file)[0]
                    py_files.append(file_name_without_extension)
        self.taglist=py_files

    def check_status(self):
        if not connect_status():
            self.移动端.连接设备()
            return connect_status()
        return True
    
    def stop(self):
        self.移动端.关闭设备()
        return
    #
    def run(self):
        if not self.check_status():
            TimeECHO("无法连接设备，退出")
            return False
        #
        for tag in self.taglist:
            if not os.path.exists(tag+".txt"):
                TimeECHO(f"不进行{tag}")
                continue
            TimeECHO(f"=>>>>{tag}<<<<="*3)
            try:
                # 动态导入模块
                module = importlib.import_module(tag)
                # 获取模块中与模块名相同的类
                tag_class = getattr(module, tag)
                tag_object = tag_class()  # 假设类构造函数不需要参数
                # 使用类来创建一个对象实例
                tag_object.APPOB.big=False
                tag_object.run()
                tag_object.stop()
            except:
                traceback.print_exc()
                continue
        #

    def looprun(self, times=0):
        times = times + 1
        startclock = self.运行时间[0]
        endclock = self.运行时间[1]
        leftmin = self.Tool.hour_in_span(startclock, endclock)*60.0
        while True:
            if leftmin > 0:
                TimeECHO("剩余%d分钟进入新的一天" % (leftmin))
                self.APPOB.关闭APP()
                self.移动端.重启重连设备(leftmin*60)
                leftmin = self.Tool.hour_in_span(startclock, endclock)*60.0
                continue
            times = times+1
            TimeECHO("="*10)
            self.run()
            #
            if not os.path.exists(self.内置循环FILE):
                return self.stop()
            # 如果提前结束了，就让脚本再等一会
            leftmin = self.Tool.hour_in_span(endclock+0.1,startclock)*60.0

def main():
    config_file = ""
    if len(sys.argv) > 1:
        config_file = str(sys.argv[1])
    Settings.Config(config_file)
    ce = autotask_android()
    ce.looprun()
    exit()

if __name__ == "__main__":
    main()

