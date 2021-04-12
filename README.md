# Glucosamine_ChatBot

a QQ chat bot

注：本项目使用Pycharm Professional完成，感谢Jetbrains为全球学生提供的技术支持。

## 运行前必须的环境

[Python < 3.8.0](https://www.python.org/downloads/release/python-374/)

[Mirai Console Loader](github.com/iTXTech/mirai-console-loader)

## 提供帮助的项目：

[Ossas_ChatBot](https://github.com/Dimsmary/Ossas_ChatBot)

## Note

运行`Chat/main.py`时，会报错：`AttributeError: 'str' object has no attribute 'decode'`。这是包本身的bug。

解决方式：查看Traceback，把报错的文件中的`.decode("utf-8")`和`.decode("utf8")`直接全部删除即可。
