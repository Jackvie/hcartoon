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