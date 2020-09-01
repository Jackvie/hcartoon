# hcartoon

```
start.sh
#!/bin/sh
/bin/bash
```

```sh
pull centos image
sudo docker run --name=hcartoon --privileged  -p 10022:22 -p 8000:8000 -v /home/yuntao/hcartoon/:/hcartoon --restart=on-failure:5 -itd centos /hcartoon/start.sh

# 查看版本
cat /etc/centos-release
CentOS Linux release 8.2.2004 (Core)

# 修改字符集
vi /etc/locale.conf
#LANG="en_US.UTF-8"
LANG="C.utf-8"
source /etc/locale.conf
```

```
# 安装python
https://www.jianshu.com/p/b978e46de442
```

```
# 安装 mysql
拉取镜像
https://dev.mysql.com/doc/refman/8.0/en/docker-mysql-getting-started.html
# 创建mysql容器
sudo docker run -p 3307:3306 -p 33060:33060 --name mysql -v /home/yuntao/mysql/conf:/etc/mysql/conf.d -v /home/yuntao/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=a123456 -e "TZ=UTC" -e "LANG=C.UTF-8" -d mysql

centos容器安装mysql客户端
yum -y install mysql
# 使用客户端链接mysql容器的服务端
# sudo systemctl restart mysql.service
mysql -uroot -h 172.18.196.63 -P 3307 -p
```