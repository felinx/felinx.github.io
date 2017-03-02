nginx反向代理配置(附：tornadoweb.cn的nginx配置)
###############################################
:date: 2011-06-11 11:41
:author: 飞龙
:category: IT
:tags: nginx, 反向代理
:slug: 2011/06/nginx-reverse-proxy
:status: published

GAE的Hosting站点
`appspot.com <http://appspot.com/>`__\ 在国内被墙，因此架设在GAE上的运用没法直接访问，需要曲线救国，其中一招比较有效的方式即是通过nginx反向代理来实现，不过这个要求你在国外有一个可用的nginx。下面以\ `tornadoweb.cn <http://www.tornadoweb.cn>`__\ 为例讲述如何用nginx配置反向代理(注：tornadoweb.cn为\ `tornadoweb.org <http://www.tornadoweb.org/>`__\ 的镜像站点，原站就是在GAE上，因此国内无法直接访问)。关于nginx的基本配置部分请参考我在poweredsites上的博客\ `how-to-setup-nginx <http://blog.poweredsites.org/entry/how-to-setup-nginx>`__\ ，本文只讨论如何配置tornadoweb.cn这个站点，配置说明详见配置中的注释。

::

    server {
    　  # 监听80端口，通常可以省略。
        listen   80;

    　  # 要配置的站点域名，即用来曲线访问GAE上的原站点的域名。
        server_name  www.tornadoweb.cn;

        # Ben老大要求tornadoweb.cn有说明是镜像站点以区别于原站tornadoweb.org，
        # 因此我走巧将头上的LOGO采用修改过的本地文件，在原logo上加了mirror的声明
        location /static/tornado.png {
            # LOGO文件tornado.png所在文件夹目录
            root /mnt/ebs/sites/tornadoweb;
        }

        location / {
            # 配置反向代理到 www.tornadoweb.org，对于没有绑定域名的GAE运用来说，会是http://python-tornado.appspot.com这样的。
            proxy_pass http://www.tornadoweb.org;
            # 关闭重定向跳转
            proxy_redirect off;
            # 转发IP等HTTP头信息
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }

    # 下面几个是将www.tornadoweb.com.cn也跳转到www.tornadoweb.cn，并且将域名根目录tornadoweb.cn这样的访问也跳转到www下，
    # 这个反之亦然(现在多是这种，即www跳转到域名根目录)。
    server {
        server_name  tornadoweb.com.cn;
        rewrite ^(.*)$ http://www.tornadoweb.cn$1 permanent;
    }

    server {
        server_name  www.tornadoweb.com.cn;
        rewrite ^(.*)$ http://www.tornadoweb.cn$1 permanent;
    }

    server {
        server_name  tornadoweb.cn;
        rewrite ^(.*)$ http://www.tornadoweb.cn$1 permanent;
    }

配置好后reload/restart一下nginx就妥了，本例的结果即是访问tornadoweb.cn将看到tornadoweb.org一样网站，除了采用了本地文件的那个LOGO不同外。
