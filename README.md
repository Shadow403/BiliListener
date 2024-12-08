<div align="center">
<a href="https://github.com/Shadow403/BiliListener">
  <img src="./image/logo.png"alt="LOGO">
</a>
</div>

## 📖 简介
#### ✨ 一个异步B站直播监听程序 ✨
- 配置项: `Json`
- 数据库: `SQLite3`
- API框架: `FastAPI`

## 📚 使用方法
```bash
git clone https://github.com/Shadow403/BiliListener.git
cd BiliListener
```
```bash
(建议创建虚拟环境)
python -m venv .venv
.\.venv\Scripts\activate
```
```bash
pip install -r requirements.txt
```

## 📝 配置
- 修改 `config` 文件夹下的 `config.py.example` 重命名为 `config.py` 并修改文件内的 `SESSDATA` 字段 `(填入已登录B站的SESSDATA)`

## 📌 运行
- `pusher.py` 监听入口程序
- `worker.py` 接口入口程序

## 🎯 功能
- 入场
- 弹幕
- 礼物
- 上舰
- SC (醒目留言)

## 🧱 结构
```bash
BiliListener
 ├─app                      [监听程序]
 │  ├─database              [数据库]
 │  ├─utils                 [函数]
 │  ├─pusher                [监听检查]
 │  └─worker                [监听WS]
 ├─config                   [配置文件夹]
 │  └─data
 │     └─config.py
 ├─data                     [监听数据]
 └─modules                  [项目依赖]
    └─blivedm (package)
```

## 💖 感谢
- [`xfgryujk/blivedm`](https://github.com/xfgryujk/blivedm)


## TODO ⏰

- [] 打包该项目

<br>

<details>
<summary> 日志 </summary>

- `v0.1.0` 🎉 创世提交
- `v0.1.1` 🧱 监听异步支持
- `v0.1.2` ⚡ 接口优化
- `v0.1.3` ⚡ `ws` 断线重连后记录的数据恢复 | 添加 `ws` `LIKE_V3_UPDATE`
- `v0.1.4` ✨ 添加更多记录的数据 `config.json`
- `v0.1.5` ✨ 整体重构
