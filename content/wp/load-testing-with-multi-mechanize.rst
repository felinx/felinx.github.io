介绍一款Web Performance & Load 测试工具multi-mechanize
######################################################
:date: 2013-02-19 19:21
:author: 飞龙
:category: Python
:slug: load-testing-with-multi-mechanize
:status: published

对Web服务做Performance & Load测试，最常见的工具有\ `Apache
Benchmark <http://httpd.apache.org/docs/2.2/programs/ab.html>`__\ 俗称ab和商用工具LoadRunner。ab简单直接，功能也相对较弱，但我们经常看到的对一些Web
server或者Framework的性能测试用的ab做的，而LoadRunner功能也确实很强大，各种大型软件公司、软件外包企业几乎是必备了，用起来很High，当然其价格也确实很High
:)

这里要介绍的\ `multi-mechanize( <https://github.com/cgoldberg/multi-mechanize>`__\ 这名忒难记)是一款用Python开发的Performance
&
Load测试工具，是由\ `Pylot <http://pylot.org/>`__\ 的作者新近开发的，算是升级换代的产品。用multi-mechanize可以通过编写Python脚本来实现较复杂的测试逻辑，其并发测试是通过multiprocessing(多进程)和多线程机制来实现的。

**1. 安装**
-----------

万能的pip&easy\_install
-----------------------

pip install multi-mechanize mechanize numpy matplotlib
------------------------------------------------------

-  mechanize是一个模拟browser行为的一个库，当然你也可以用其它的如urllib2、request、tornado.httpclient等等库，不是必须。
-  后面两个numpy和matplotlib也是可选的，当你需要它自动生成图形化报表时才会用到，安装matplotlib你的系统有可能需要安装libpng和freetype库。

2. 使用方法
-----------

-  创建项目

::

        multimech-newproject my_project

自动创建一个my\_project目录，子目录test\_scripts用来放测试脚本，config.cfg是测试配置，主要要配的是测试时间、测试脚本和并发threads量。

-  脚本编写，借用官方的一个简单例子：

::

    #
    #  Copyright (c) 2010 Corey Goldberg (corey@goldb.org)
    #  License: GNU LGPLv3
    #
    #  This file is part of Multi-Mechanize
    #

    import mechanize
    import time

    class Transaction(object):
        def __init__(self):
            self.custom_timers = {}

        def run(self):
            br = mechanize.Browser()
            br.set_handle_robots(False)

            start_timer = time.time()
            resp = br.open('http://www.example.com/')
            resp.read()
            latency = time.time() - start_timer

            self.custom_timers['Example_Homepage'] = latency

            assert (resp.code == 200), 'Bad HTTP Response'
            assert ('Example Web Page' in resp.get_data()), 'Failed Content Verification'

    if __name__ == '__main__':
        trans = Transaction()
        trans.run()
        print trans.custom_timers

注意：按multi-mechanize的默认规则，每个脚本必须有一个Transaction的类，类要有一个run方法，在run里面写测试业务逻辑。这个例子是打开http://www.example.com，记录访问所耗时长，非常简单明了，而实际的场景你可能需要有用户登录、然后测试某个或多个页面(API)，只是测试业务复杂一些，写法是类似的。一个脚本文件只能有一个Transaction的类、类也只能有一个run方法，写起case来是不是觉得非常不方便？不用急，针对这点，后面的小技巧部分会另辟蹊径给你指条明路。

-  运行项目的测试脚本

::

    multimech-run my_project

测试结果报表和原始数据将放到results目录下按测试时间生成的子目录中，生产的html版本的结果统计如下图所示:

|image0|

3. 使用小技巧
-------------

-  Cookie：

如果使用的是mechanize，可以通过下面的方式，从上面的browser对象br里获取到cookie信息。

br.\_ua\_handlers["\_cookies"].cookieja

-  单个脚本多个测试用例的支持：这个思路来源于testsuite的概念，同一个testsuite里的case作为一组相关的case可以共享一些代码逻辑和资源(如browser对象)，而multi-mechanize默认的方式是不支持的，要实现这一点，只需要一点小小的技巧即可，上代码：

-  真实的并发量计算：multi-mechanize使用了multiprocessing库，会同时起多个进程，且每个进程按config里的配置起多个线程来实现并发测试，但真正的单位时间内的并发量并不是config里设置threads=10这样的表示每秒10个并发，真实的并发量需要根据最终完成的transaction数和这些transaction里面包含多少次http请求和总的完成时间来计算得知，这点不是很直观。
-  自定义统计数据：你可以往self.custom\_timers这个内建的字典里塞任意的自定义统计数据，他们在报表中都能够得到体现。

更多的文档和一手资料请参考文档\ http://testutils.org/multi-mechanize/\ 和git代码库\ `https://github.com/cgoldberg/multi-mechanize <https://github.com/cgoldberg/multi-mechanize%20>`__\ 。最后multi-mechanize还不是很好用，一是使用过程中发现有一些情况会抛异常，导致不能正确生成报表，另一个别扭的是case的编写不是unittest那一套，是作者自创Transaction流:)

转载请注明出处：\ http://feilong.me/2013/02/load-testing-with-multi-mechanize

.. |image0| image:: /static/2013/02/multi-mechanize-report.jpg
   :width: 881px
   :height: 942px
   :target: /static/2013/02/multi-mechanize-report.jpg
