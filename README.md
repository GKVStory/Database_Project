# 数据库大作业

> 最终版本，最高品质

## 使用说明🪄

### 1. 检查文件是否完好并修改数据库配置，具体位置为day16/settings.py中

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'new_ins',  	# 数据库名字
           'USER': 'root',  		# 数据库用户名
           'PASSWORD': 'root',  	# 数据库密码
           'HOST': '127.0.0.1',  	# 主机
           'PORT': 3306,			# 端口
       }
   }
   ```

   

### 2. 在项目根目录运行`python manage.py runserver`命令，进入服务器

### 3. 初次登录可用现有用户名：康康 以及密码：123 进入系统，后续可以自己创建账户进行登录

### 4. 若有其他问题，请随时联系开发者（Email: junchikang0611@163.com）

