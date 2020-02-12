# weibo_spider

## 克隆

```bash
git clone git@github.com:liyi3889/weibo_spider.git
cd weibo_spider
```

## 安装依赖

``` bash
pip install -r requirements.txt
```

## 修改配置文件 `src/config.py`

- `host` 主机地址
- `port` mysql服务端口
- `user` 数据库用户名
- `password` 密码
- `name` 数据库名

## 初始化数据库

```bash
python ./src/dbinit.py
```

## 获取数据并写入数据库

```bash
python ./main.py
```
