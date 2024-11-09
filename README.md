# autotask_android

基于[airtest_mobileauto](airtest_mobileauto)的安卓自动化任务脚本

![GitHub forks](https://img.shields.io/github/forks/cndaqiang/autotask_android?color=60c5ba&style=for-the-badge)![GitHub stars](https://img.shields.io/github/stars/cndaqiang/autotask_android?color=ffd700&style=for-the-badge)


## 脚本开发环境说明
* 本脚本基于分辨率`960x540`, dpi`160`的安卓模拟器开发
* dpi或者分辨率不同很容易识别失败。
* 有的模拟器打开特定APP会闪退

环境依赖

```
python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple  --upgrade
```

## 当前开发项目
### 基于url的签到
* `web_url`,直接打开特定url,实现签到, **适配任意的安卓设备**
* 将url存储到`web_url.txt`,下面是我常用的url
```
none
```

### 基于浏览器的签到
* *注: 本脚本于via-5.9.0测试通过, 需开启桌面模式、全屏、浏览器标识(windows/chrome),其他浏览器自行替换图片资源*
* 只能在境内的模拟器/容器内执行, 这些网站在不同地区显示的内容不同.
* `web_ablesci`, [科研通](https://www.ablesci.com/)每日签到
* `web_muchong`, [小木虫](https://muchong.com/bbs/)每日签到

### 基于app的签到
* `app_alicloud`, 阿里云盘每日签到(横屏版960x540)




## 运行
* 创建`tag.txt`则开启领取`tag.py`中定义的礼包

```
python run.py config.win.yaml
```

我的配置文件 `config.win.yaml`
```
mynode: 1
BlueStackdir: C:\Program Files\BlueStacks_nxt
BlueStack_Instance: {1: "Pie64_2"}
BlueStack_Windows: {1: "autotask"}
LINK_dict: {1: "Android:///127.0.0.1:5575"}
figdir: assets
logfile: {1: "result.1.txt"}
prefix: "autotask"
```


## 计划任务
* Windows可以点击`run.bat`， 或将`run.bat`添加到Windows的自动化任务
![alt text](doc/crontab_win.png)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=cndaqiang/autotask_android&type=Date)](https://star-history.com/#cndaqiang/autotask_android&Date)
