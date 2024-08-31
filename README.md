# autotask_android
基于[airtest_mobileauto](airtest_mobileauto)的安卓自动化任务脚本

![GitHub forks](https://img.shields.io/github/forks/cndaqiang/autotask_android?color=60c5ba&style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/cndaqiang/autotask_android?color=ffd700&style=for-the-badge)


## 开发进度
**[基于via浏览器的签到](run_via.md)**
* `via_ablesci`, [科研通](https://www.ablesci.com/)每日签到
* `via_muchong`, [小木虫](https://muchong.com/bbs/)每日签到

## 环境依赖
```
python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple  --upgrade
```


## 我的配置
* 模拟器MuMu
* 分辨率`960x540`,dpi`160`

配置文件`config.win.txt`
```
[client]
mynode = 0
#ADB的ip和端口号
LINK_dict = {
    0: "Android:///127.0.0.1:16448"}
[control]
figdir=assets
logfile={
    0: "result.txt"}
```

## 运行示例
### 终端运行
```
python run_via.py config.win.txt
```

### Windows平台: bat文件运行
双击`run_via.bat`, 需要根据python环境修改其中的python路径

亦可将`run_via.bat`添加到系统的自动化任务，方法同:[关于windows平台的计划任务](https://cndaqiang.github.io/WZRY/howtorun.html#%E5%85%B3%E4%BA%8Ewindows%E5%B9%B3%E5%8F%B0%E7%9A%84%E8%AE%A1%E5%88%92%E4%BB%BB%E5%8A%A1)
![alt text](https://cndaqiang.github.io/WZRY/doc/crontab_win.png)

### Linux平台
```
python run_via.py config.lin.txt
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=cndaqiang/autotask_android&type=Date)](https://star-history.com/#cndaqiang/autotask_android&Date)
