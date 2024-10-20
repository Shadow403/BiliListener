<div align="center">

<a href="https://github.com/Shadow403/BiliListener">
  <img src="./image/logo.png"alt="LOGO">
</a>

### _✨ 一个异步B站直播监听程序 ✨_

</div>

## 📖 简介
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
- 需修改 `config` 文件夹下的 `config.py` 文件内的 `SESSDATA` 字段 `(填入已登录B站的SESSDATA)`

## 📌 运行
- `app.py` 监听入口程序
- `web.py` 接口入口程序

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
 │  ├─pusher                [监听检查]
 │  ├─utils                 [函数]
 │  └─worker
 ├─config                   [配置文件夹]
 │  └─data
 │     ├─config.py
 │     └─data
 │        ├─uid_list.json   [监听列表]
 │        └─cache.json      [正在监听]
 ├─data                     [监听数据]
 ├─modules                  [项目依赖]
 │  └─blivedm
 │     ├─clients
 │     └─models
 └─web                      [接口程序]
     ├─router               [路由]
     └─utils                [函数]
```

## 💖 感谢
- [`xfgryujk/blivedm`](https://github.com/xfgryujk/blivedm)


<br>

<details>
<summary> 日志 </summary>

- `v0.1.0` 🎉创世提交
