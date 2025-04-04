<div align="center">
<a href="https://github.com/Shadow403/BiliListener">
  <img src="./image/logo.png"alt="LOGO">
</a>
</div>

## 📖 简介
#### ✨ 一个B站直播监听程序 ✨
- 配置项: `Yaml`
- 数据库: `SQLite3`
- API框架: `FastAPI`

## 📚 使用方法
```bash
git clone https://github.com/Shadow403/BiliListener.git
cd BiliListener
pip install poetry
poetry config virtualenvs.in-project true
poetry install
```

## 📝 配置
- 修改 `config.yml` 下的 `auth.bili_jct` 填入`填入已登录B站的 bili_jct`
- 修改 `config.yml` 下的 `auth.sessdata` 填入`填入已登录B站的 sessdata`

```yml
api:
  cors:                       # 跨域设置
  - 10.20.0.1                 # 跨域IP列表
  host: 127.0.0.1             # api监听地址
  port: 5700                  # api监听端口
  router_access:              # api访问权限
    r_put_uid:                # 允许访问的IP
    - 127.0.0.1               # 允许访问的IP列表
    strict: true              # 严格模式, 如果为true, 则只有允许的IP可以访问
  ws_push_delay:              # WebSocket 推送延迟(秒)
    hub: 5                    # ws_hub 推送延迟(秒)
    listening: 35             # ws_listening 推送延迟(秒)
auth:                         # 登录信息
  bili_jct: ''                # 填入已登录B站的 bili_jct
  sessdata: ''                # 填入已登录B站的 sessdata
data:                         # 数据配置
  db_path: db                 # 数据库路径
  json:                       # json记录配置
    enable: false             # 是否启用json文件记录
    json_path: json           # json文件记录路径
  root: data                  # 监听数据存储根路径
debug: false                  # 是否启用debug模式
hide_console: true            # 是否隐藏控制台
live_clear_delay: 300         # 清除直播状态时间(秒)
live_query_delay: 30          # 查询直播状态时间(秒)
```

## 🍻 运行
- `pusher.py` 监听入口程序

## 📦 打包
```python
poetry shell
cd app
python build.py
```

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
 │  ├─config                [配置文件夹]
 │  ├─database              [数据库]
 │  ├─pusher                [监听MI]
 │  ├─worker                [监听WS]
 │  ├─data                  [监听数据]
 │  └─scripts               [打包脚本]
 │     └─build.py
 ├─modules                  [项目依赖]
 │  └─blivedm (package)
 └─web
    └─frontend              [前端](TODO)
```

## 💖 感谢
- [`xfgryujk/blivedm`](https://github.com/xfgryujk/blivedm)

## TODO ⏰

- [x] 打包该项目 📦
- [x] 支持配置文件 🛠️
- [x] 掉线(数据不完整)标记 😢
- [ ] 分布式监听 ☕

<br>

<details>
<summary> 日志 </summary>

- `v0.1.0` 🎉 创世提交
- `v0.1.1` 🧱 监听异步支持
- `v0.1.2` ⚡ 接口优化
- `v0.1.3` ⚡ `ws` 断线重连后记录的数据恢复 | 添加 `ws` `LIKE_V3_UPDATE`
- `v0.1.4` ✨ 添加更多记录的数据 `config.json`
- `v0.1.5` ✨ 整体重构
- `v0.1.6` 📦 打包该项目 🐍 修复数据库 `Bugs`
- `v0.1.7` 🛠️ 支持配置文件
- `v0.1.8` 🛠️ 支持更多配置项 🐍 修复数据库 `commit.handle` `Bugs`
- `v0.1.9-b1` 🌐 添加前端
- `v0.1.9-b2` 📦 添加打包图标 `(ico)`
- `v0.1.9` 🛠️ 支持更多配置项 ✨ 添加重置直播状态 `24h` ✨ 添加 `api` 版本区分
- `v0.2.0-b1` ✨ 打包版本控制
- `v0.2.0-b2` ✨ API接口更新
- `v0.2.0-b3` ✨ API接口更新 🛠️ 添加权限 `strict`
- `v0.2.0` ✨📦🛠️ 整体更新
- `v0.2.1-b1` 🐍 修复了一些小问题
- `v0.2.1` 🐍 修复了一些小问题
- `v0.2.1` 🐍 修复了一些小问题
- `v0.2.2` ✨ 合并 `pusher` & `worker`
- `v0.2.3` ✨ 添加 初始化监听 🐍 修复监听完成数据提交失败问题
- `v0.2.4` 🐍 修复修改 `UID` API
- `v0.2.5` 🐍 [issues #69](https://github.com/xfgryujk/blivedm/commit/a45ee8f6774064978ba062621475cb78d6e27df8)
- `v0.2.6` ✨ 添加 `ws` 多路径支持
