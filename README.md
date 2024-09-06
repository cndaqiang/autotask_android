# autotask_android
基于[airtest_mobileauto](airtest_mobileauto)的安卓自动化任务脚本

![GitHub forks](https://img.shields.io/github/forks/cndaqiang/autotask_android?color=60c5ba&style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/cndaqiang/autotask_android?color=ffd700&style=for-the-badge)


## 环境依赖
```
python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple  --upgrade
```


## 我的配置
* 模拟器LDPlayer
* 分辨率`960x540`,dpi`160`
* dpi或者分辨率不同很容易识别失败。
* 有的模拟器无法打开特定APP。

我的配置文件`config.win.txt`
```
[client]
# 节点配置
mynode = 0
LDPlayerdir = D:\GreenSoft\LDPlayer
multiprocessing = True
LINK_dict = {
    0: "Android:///127.0.0.1:5555"}
[control]
logfile={
    0: "result.txt"}
```


## 运行示例
```
#默认控制127.0.0.1:5555的安卓设备
python via_ablesci.py
# 也可以自定义设备信息，填到`config.win.txt`,
python via_ablesci.py config.win.txt
```

## 基于浏览器的签到
* **via浏览器** 开启桌面模式，自己登录网页并收藏网页到主页
* `via_ablesci`, [科研通](https://www.ablesci.com/)每日签到
* `via_muchong`, [小木虫](https://muchong.com/bbs/)每日签到


## 基于app的签到
* `app_jd_smartrouter`, 京东无线宝路由器,每日看广告领京豆.
* * 模拟器领取存在各种问题，不再更新，手机版见`app_jd_smartrouter_m`
* `app_alicloud`, 阿里云盘每日签到(横屏版960x540)

## 全部签到
* Windows可以点击`run.bat`， 亦可以`python run.py`
* 只有存在`tag.txt`时，才会领取`tag.py`中定义的礼包
* 将`run.bat`添加到Windows的自动化任务
![alt text](doc/crontab_win.png)

## 其他
* 有些APP无法用模拟器打开，这些程序控制我的手机领取
* * 如京东无线宝, MuMu模拟器打不开, LDPlayer领取四次后再领取就卡住不动
* * 运行`python run.m.py`或者`run.m.bat`
* 开发注意
* * 由于手机会自动锁屏，所以在脚本运行开头需要`self.移动端.解锁设备()`
* 目前支持的模块
* * `app_jd_smartrouter_m`,京东无线宝路由器
* 我的配置文件`config.m.txt`
```
[client]
# 节点配置
mynode = 0
multiprocessing = True
LINK_dict = {
    0: "Android:///4e86ac13"}
[control]
figdir=assets
logfile={
    0: "result.m.txt"}
```



## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=cndaqiang/autotask_android&type=Date)](https://star-history.com/#cndaqiang/autotask_android&Date)
