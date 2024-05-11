# CS2-OTC

## 简介

CS2-OTC是基于Open-DGLAB-Controller的，实现CS2内游戏事件对DGLAB硬件的控制的Python程序。

使用Counter-Strike 2 Game State Integration (GSI)协议，实现游戏内事件监听。

使用WebSocket连接至移动端的OTC控制器，通过其连接DGLAB硬件，实现控制。

## 依赖

Python 3.8+

安装requirements.txt中的依赖

## 使用

1. 安装依赖

```bash
pip install -r requirements.txt
```

2. 配置CS2 GSI

将`gamestate_integration_CS2OTC.cfg`放入`steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg`文件夹

3. 确认手机和电脑在同一局域网下，手机端打开OTC控制器，连接DGLAB硬件，打开娱乐模式

4. 运行`app.py`

```bash
python app.py
```

5. 根据提示输入手机上显示的IP地址

6. 打开CS2，开始游戏。当前实现在玩家受伤时DGLAB硬件进行单次波形输出。
