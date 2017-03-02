说说Python获年度Tiobe编程语言大奖这事
#####################################
:date: 2011-01-10 18:36
:author: 飞龙
:category: Python
:tags: Python, 编程语言
:slug: python-wins-tiobe-2010-pro-lang-award
:status: published

今天在reddit的feed里看到了Python获得了2010年编程语言大奖，国外也有不少朋友在讨论这事，我也顺带来说几句。

Python在2010年获得了较大的市场份额增长，2010年1月以来Python的市场份额增长了1.81％，是增长速度最快的，其次是Objective
-
C（1.63％）。排名见下表，详情请见Tiobe原址：\ http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html\ 。

|image0|

再来看一下历年的获奖语言：

|image1|

Python在2007和2010最近的这几年里获得两次年度大奖，确实是很给力。

虽然Tiobe的排名不是非常靠谱，大家对此排行争议也很多，但大体它还是可以反映一个趋势。Python除了保持在后台脚本、测试领域的优势外，最近几年随着Python
web
framework的蓬勃发展，Python在Web领域的运用也越来越多，国外出现了一大批用Python开发的新站、大站，比如大名鼎鼎的：\ `reddit.com <http://www.reddit.com>`__\ 、\ `dropbox.com <http://www.dropbox.com>`__\ 、\ `bitbucket.org <http://bitbucket.org>`__\ 、\ `quora.com <http://www.quora.com>`__\ 、\ `friendfeed.com <http://friendfeed.com>`__\ ，其中reddit代码还是开源的。有趣的是，虽然在Python的Web开发领域\ `Django <http://www.djangoproject.com>`__\ 大红大紫，但是这五个网站中只有bitbucket一个是用Django开发的，而且问题还特多（碰到500错误是常态，最近似乎稳定些了），另外有三个用的是相对小众的\ `Pylons <http://www.pylonshq.com>`__\ ，而friendfeed用的则是friendfeed自己写的\ `Tornado <http://www.tornadoweb.org>`__\ (网站需翻墙)。虽然Python语言的前景一片大好，但我个人认为目前也有一些问题待解决的：

#. Python web
   framework多如牛毛（不完全列表见：\ http://wiki.python.org/moin/WebFrameworks\ ），Python界需要出现一个具有垄断地位的Web
   framework，我认为Django还不够。Web
   framework一多，好处是你可以有更多的选择自由，甚至一个framework本身还是高度可定制的（如：Pylons）；不好的地方则是很多时候你不知道该选哪一个，特别新手往往要在framework之间左右摇摆好久，从我们常常看到“是选Django呢还是Pylons呢”这类的提问和争论就可知一般（不管是国内还是国外），另外这样也不利于知识的分享，因为知识点比较分散。好在现在Python界正在尝试做一些融合，\ `repoze.bfg <http://bfg.repoze.org/>`__\ 已经开始合并到Pylons这个大的project中了。具体可以看看：\ http://lists.repoze.org/pipermail/repoze-dev/2010-November/003619.html
   和
   http://be.groovie.org/post/1558848023/notes-on-the-pylons-repoze-bfg-merger
   （后者要翻墙）。不知道合并后的Pylons能否达到Rails在Ruby的Web开发领域中那样的统治地位，虽然我看好Pylons但是我觉得在Python的世界里这个会很难，因为有了\ `WSGI规范(PEP333) <http://www.python.org/dev/peps/pep-0333/>`__\ 用Python自己造一个Web的轮子实在太简单了，你我都有能力写一个:)
#. Python2.x和Python3.x差异挺大、前后不兼容，虽然有2to3的工具可以转，但不能解决所有的问题。Python3.x尚未完全普及开来，很多第三方的库都没用官方支持Python3.x。考虑到前后版本的这个不兼容性，这会让一些人对采用Python开发项目产生顾忌。而在Web开发领域，WSGI1.0也是不支持Python3.x，支持Python3.x的\ `Web3（PEP444） <http://www.python.org/dev/peps/pep-0444/>`__\ 还处在草案状态。

虽然有上面所说的一些问题，但是可以预见的是，随着Python3.x的普及和Python
web
framework的发展、成熟，Python依然有很大的上涨空间，我认为将来（最多5年吧）超过PHP是很有可能的，祝Python一路走好。

另外，我新注册了域名\ `chinapy.org <http://www.chinapy.org>`__\ （现在还不能访问），准备弄一个开放一点的中国的Python社区，给Python在中国的推广运用做点自己的贡献。

.. |image0| image:: /static/2011/01/python_tiobe_index_2010_winner.jpg
   :class: size-full wp-image-118 aligncenter
   :width: 598px
   :height: 582px
.. |image1| image:: /static/2011/01/python_lang_wins_years.jpg
   :class: size-full wp-image-119 aligncenter
   :width: 144px
   :height: 215px
