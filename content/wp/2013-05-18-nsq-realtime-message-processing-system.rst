实时消息处理系统NSQ & Python Worker
###################################
:date: 2013-05-18 18:43
:author: 飞龙
:category: Python
:tags: NSQ, 消息系统, pynsq
:slug: 2013/05/nsq-realtime-message-processing-system
:status: published

NSQ是由知名短链接服务商\ `bitly <https://bitly.com>`__\ 用Go语言开发的实时消息处理系统，具有高性能、高可靠、无视单点故障等优点，是一个非常不错的新兴的消息队列解决方案。nsq现在发展很快，已有多种语言的客户端，Go和Python版本的客户端是官方出的，比较给力，其中Python客户端\ `pynsq <https://github.com/bitly/pynsq>`__\ 的Writer即发布消息部分的代码是我贡献的。

以下是我准备在5.22的上海GDG活动中做的有关NSQ的主题演讲的slideshare，看不到的同学请下载后面的pdf版本，关于nsq更详细的介绍就看我5.22日的主题分享了。

分享过程视频 \ `NSQ & Python Worker视频 <http://video.tudou.com/v/XMjIyMjI3MDk5Ng==.html>`__

因为是支支用手机录的屏幕比较晃，大家凑合下。另外更正讲解过程中的一个口误，不是Go的作者之一follow了我的nsqworker项目而是nsq的主要作者。

`Nsq & python
worker <http://www.slideshare.net/FelinxLee/nsq-python-worker>`__ from
`Felinx Lee <http://www.slideshare.net/FelinxLee>`__

PDF版本 \ `NSQ-Python-Worker.pdf PDF </static/2013/05/NSQ-Python-Worker.pdf>`__

PPT提到的我写的nsqworker的项目地址见：\ https://github.com/felinx/nsqworker
