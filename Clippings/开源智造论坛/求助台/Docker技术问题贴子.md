---
title: "Docker技术问题贴子"
source: "http://www.thinkltd.cn/forum/1/docker-3589"
forum: "求助台"
author: "杨浔波"
published: 2022-12-18
created: 2026-08-17
tags:
  - clippings
  - odoo
  - 论坛/求助台
---

# Docker技术问题贴子

> [!info] 来源
> 开源智造论坛 · 求助台 | 作者:杨浔波 | 2022-12-18
> <http://www.thinkltd.cn/forum/1/docker-3589>

> 引言：由于一部分客户存在自主和之前我们给予的服务器安装时采用了Docker进行部署，特此本帖子目的是解决Docker从无到有的完整记录过程

###
Ubuntu安装部署Docker

1. 安装Docker所需的依赖环境

```python
    $ sudo apt-get update
    $ sudo apt-get install
        ca-certificates
        curl
        gnupg
        lsb-release
```

2. 安装Docker的ubuntu apt源PGP证书

    $ sudo mkdir -p /etc/apt/keyrings
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

3. 设置Docker的存储库信息

```python
    $ echo
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

4. 更新获取Docker的Apt源文件

    $ sudo apt-get update

5. 安装并测试Docker启动

    $ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
    $ sudo docker run hello-world

PS：以上步骤操作完毕后即完成了Ubuntu的Docker容器服务的安装，如需启动时不需要sudo，参考官方文档：[https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) 当中关于Manage Docker as a non-root user的内容介绍

#### 待研究和验证的课题内容：

- Docker修改容器内部文件的方法：[https://blog.csdn.net/m0_67391377/article/details/123871347](https://blog.csdn.net/m0_67391377/article/details/123871347https://blog.csdn.net/hzblucky1314/article/details/127333943)
- 容器的打包与迁移拷贝：
  [https://blog.csdn.net/hzblucky1314/article/details/127333943](https://blog.csdn.net/hzblucky1314/article/details/127333943)
  [https://blog.csdn.net/m0_54853503/article/details/123873558](https://blog.csdn.net/m0_54853503/article/details/123873558)

#### Odoo的Docker容器部署安装与后期维护更新（待更新完善）

1. 首先点击访问： [GitHub - odoo/docker](https://github.com/odoo/docker)

选择使用具体的版本文件夹，进入具体版本文件夹，编辑Dockerfile，将必要的文件包的ARG信息修改指定的源码版本信息。如：

    ARG ODOO_RELEASE=20221216
    ARG ODOO_SHA=f6aeed95ae4fe3c891fe7c35e0dc08e83553493d

其余需要补充运行环境的python依赖库的可以在RUN定义区域中增加pip install来操作。

所有 Dockerfile文件构建完成后，需要修改该的所属文件夹，在服务器的权限为777。

之后服务器中切换到该文件所在的目录位置下，操作以下命令：

    docker build -t odoo16:20221215 .

其中odoo16为odoo版本，20221215为具体Odoo官方build的代码版本。当然也可以自由定义，但为了规范管理，最好按照这样方式进行，避免多个Odoo版本在同一台服务器无法分清楚具体的版本和官方的代码获取的更新日期节点。

2. 运行启动Odoo

在 Dockerfile所在的服务器文件夹里建立一个docker-compose.yml文件，具体的代码用法参考官方github地址： [docs/odoo at master · docker-library/docs · GitHub](https://github.com/docker-library/docs/tree/master/odoo) 之后使用以下命令，启动Odoo及关联的Postgresql数据库，当然根据需要也可以修改 docker-compose.yml 两个容器有关的Volumes的挂载信息。

    docker-compose up -d

#### Odoo通过KBS结合Docker实现在线演示与测试服务器的部署方案（待更新完善）

---

相关:[[Clippings/开源智造论坛/求助台/00-求助台索引.md|← 求助台索引]]
