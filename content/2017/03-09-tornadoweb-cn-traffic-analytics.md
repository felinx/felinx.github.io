Title: 国内堪忧的Tornado用户群
Date: 2017-03-09 17:50
Category: Python
Tags: Tornado
Slug: 2017/03/tornadoweb-cn-traffic-analytics
Authors: 飞龙

[tornadoweb.cn](http://www.tornadoweb.cn)是我2011年搭建的[Tornado](http://www.tornadoweb.org)中文站，主要是为传播Tornado web framework：

1. 当时Tornado官网[tornadoweb.org](http://www.tornadoweb.org)放在GAE上，需要翻墙，我提供一个镜像站点给不翻墙的人用。
2. 我找人中文翻译了Tornado 1.2版本的文档，供国人参考

6年来这个站点文档没有再更新过，但每天一直保持有200-300的用户访问量(看来当年做了点小事还有点用)，今天心血来潮时通过Google Analytics细看了下用户访问来源大吃了一惊：

![tornadoweb.cn traffic](/static/2017/03-09-tornadoweb-cn-traffic.jpg)

占绝大部分的流量来自百度搜索，来自Google的搜索只有百度的1/10，用Tornado的筒子们你们想要提升自身技能水平得学会翻墙、远离百度远离百度远离百度啊！！！

我又细追了下其它来源的链接(Referrals)，其中来自51cto的[第一篇：Python高性能Web框架Tornado原理剖析](http://3060674.blog.51cto.com/3050674/1683295)和来自csdn的[windows下安装tornado](http://blog.csdn.net/fjx1173865548/article/details/54023325)非常有趣：

一个把tornadoweb.cn当做官方网站
![tornadoweb cn as org](/static/2017/03-09-tornadoweb-cn-as-org.jpg)

另一个把tornadoweb.cn当下载来源站
![tornadoweb cn download](/static/2017/03-09-tornadoweb-cn-download.jpg)

看到这，有没有一股Xcode Ghost事件的既视感？虽然tornadoweb.cn是正儿八经的网站，上面给的下载地址也是Tornado官方的下载地址，但是Xcode Ghost事件中的受害开发者就是这么轻易相信非官方渠道站点，下了被种了病毒的Xcode版本的。我们就不能从Xcode Ghost事件中长点记性么？
