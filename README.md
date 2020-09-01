# hcartoon

```
start.sh
#!/bin/sh
/bin/bash
```

```
sudo docker run --name=hcartoon --privileged  -p 10022:22 -p 8000:8000 -v /home/yuntao/hcartoon/:/hcartoon --restart=on-failure:5 -itd centos /hcartoon/start.sh
```
