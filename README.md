# Trade_Bear_Backend
### 路由地址
```
http://81.70.0.250:6666
```
### 激活虚拟环境
```
source /home/ubuntu/develop/bin/activate
```
### 安装需要的库
```
pip install -r requirements.txt
```
### 部署项目
```
gunicorn -b 0.0.0.0:6666 manage:app
```