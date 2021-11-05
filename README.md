# Trade_Bear_Backend
### 路由地址
```
http://81.70.0.250:6666
```
### 部署项目
```
source /home/ubuntu/develop/bin/activate # 激活环境
cd /home/ubuntu/Trade_Bear_Backend/      # 进入项目的文件夹
gunicorn -b 0.0.0.0:6666 manage:app      
```