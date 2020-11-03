<div align="center"> 
<h1 align="center">Bilibili播放量助手</h1>
</div>

# 简介

哔哩哔哩(B站)自动播放视频，

如果本项目对你有帮助，那么就请给个`star`吧。

# 功能

- [x] 自动播放视频，可大量增加播放量（仅增加pv）
- [x] 增加用server酱推送运行结果到微信

# 使用方法

## 1.fork本项目

项目地址：[https://github.com/aydcyhr/bili-play-action](https://github.com/aydcyhr/bili-play-action)

## 2.准备需要的参数

本项目成功运行需要两个参数，分别是`url.txt`，`ua.txt`

- ua.txt不建议修改
- 使用时将你的视频地址粘贴在url.txt后面，一个一行

## 3.开启actions

默认`actions`处于禁止状态，在`Actions`选项中开启`Actions`功能，把那个绿色的长按钮点一下。

## 4.进行一次push操作

发现有部分朋友的定时任务，在第二天没有正常执行。解决办法就是进行一次`push`操作。

打开`README.md`，随意加一个空格即可。

## 5.运行一次工作流

项目创建`Wiki`则会触发一次工作流。

- `Wiki` --> `Create the first` --> `Save Page`
- 查看`actions`，显示对勾就说明运行成功了。理论上每分钟都会执行，实际上运行速度远低于预期，因此加入了5个工作流，每个工作流除了名称之外，完全相同（嫌慢可自行添加新的工作流）。

# 推送运行结果到微信

使用`server`酱将程序运行结果推送到微信。

`server`酱官网：http://sc.ftqq.com

- 按照`server`酱官网使用教程，用`github`登录并绑定微信。
- 获得`SCKEY`并将其填入到`bv.py`最后一行中。
- 取消`bv.py`中最后一行的注释。

这样就可以在微信接收到运行结果了。

# 如何拉取最新代码

1、查看是否有源头仓库的别名和地址

```sh
$ git remote -v
origin  https://github.com/aydcyhr/bili-play-action.git (fetch)
origin  https://github.com/aydcyhr/bili-play-action.git (push)
upstream  https://github.com/aydcyhr/bili-play-action (fetch)
upstream  https://github.com/aydcyhr/bili-play-action (push)
```

`origin`是你的仓库地址，`upstream`是你`fork`的源头仓库。通常第一次是没有`upstream`的。

2、添加源头仓库

```sh
git remote add upstream https://github.com/aydcyhr/bili-play-action
```

3、把上游仓库`main`分支的更新拉取到本地

```sh
git pull upstream main
```

4、将更新后的代码推送到你的仓库

```sh
git push origin main 
```

由于添加有配置文件`*.yml`，有可能会覆盖你自定义的`*.yml`，需要注意。

# 参考项目

[happy888888/BiliExp](https://github.com/happy888888/BiliExp)

[srcrs/BilibiliTask](https://github.com/srcrs/BilibiliTask)
