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
**[基于via浏览器的签到](run_via.md)**
* via浏览器 开启桌面模式，自己登录网页并收藏网页到主页
* `via_ablesci`, [科研通](https://www.ablesci.com/)每日签到
* `via_muchong`, [小木虫](https://muchong.com/bbs/)每日签到


## 基于app的签到
* `app_jd_smartrouter`, 京东无线宝路由器,每日看广告领京豆

## 全部签到
* Windows可以点击`run.bat`， 亦可以`python run.py`
* 只有存在`tag.txt`时，才会领取`tag.py`中定义的礼包
* 将`run.bat`添加到Windows的自动化任务
![alt text](doc/crontab_win.png)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=cndaqiang/autotask_android&type=Date)](https://star-history.com/#cndaqiang/autotask_android&Date)
