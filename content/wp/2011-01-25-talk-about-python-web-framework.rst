浅谈Python web框架
##################
:date: 2011-01-25 19:01
:author: 飞龙
:category: Python
:tags: Python, web framework, Django, Tornado
:slug: 2011/01/talk-about-python-web-framework
:status: published

说到web
framework，Ruby的世界Rails一统江湖，而Python则是一个百花齐放的世界，各种micro-framework、framework不可胜数，不完全列表见：\ http://wiki.python.org/moin/WebFrameworks\ 。虽然另一大脚本语言PHP也有不少框架，但远没有Python这么夸张，也正是因为Python
web framework（Python
web开发框架，以下简称Python框架）太多，所以在Python社区总有关于Python框架孰优孰劣的话题，讨论的时间跨度甚至长达3-5年。

Python这么多框架，能挨个玩个遍的人不多，坦白的说我也只用过其中的三个开发过项目，另外一些稍微接触过，所以这里只能浅谈一下，欢迎懂行的朋友们补充、拍砖。

`Django <http://www.djangoproject.com>`__
-----------------------------------------

|image0|
--------

Python框架虽然说是百花齐放，但仍然有那么一家是最大的，它就是Django。要说Django是Python框架里最好的，有人同意也有人坚决反对，但说Django的文档最完善、市场占有率最高、招聘职位最多估计大家都没什么意见。Django为人所称道的地方主要有：

-  完美的文档，Django的成功，我觉得很大一部分原因要归功于Django近乎完美的官方文档（包括Django
   book）。
-  全套的解决方案，Django象Rails一样，提供全套的解决方案（full-stack
   framework + batteries
   included），基本要什么有什么（比如：cache、session、feed、orm、geo、auth），而且全部Django自己造，开发网站应手的工具Django基本都给你做好了，因此开发效率是不用说的，出了问题也算好找，不在你的代码里就在Django的源码里。
-  强大的URL路由配置，Django让你可以设计出非常优雅的URL，在Django里你基本可以跟丑陋的GET参数说拜拜。
-  自助管理后台，admin
   interface是Django里比较吸引眼球的一项contrib，让你几乎不用写一行代码就拥有一个完整的后台管理界面。

而Django的缺点主要源自Django坚持自己造所有的轮子，整个系统相对封闭，Django最为人诟病的地方有：

-  系统紧耦合，如果你觉得Django内置的某项功能不是很好，想用喜欢的第三方库来代替是很难的，比如下面将要说的ORM、Template。要在Django里用SQLAlchemy或Mako几乎是不可能，即使打了一些补丁用上了也会让你觉得非常非常别扭。
-  Django自带的ORM远不如SQLAlchemy强大，除了在Django这一亩三分地，SQLAlchemy是Python世界里事实上的ORM标准，其它框架都支持SQLAlchemy了，唯独Django仍然坚持自己的那一套。Django的开发人员对SQLAlchemy的支持也是有过讨论和尝试的，不过最终还是放弃了，估计是代价太高且跟Django其它的模块很难合到一块。
-  Template功能比较弱，不能插入Python代码，要写复杂一点的逻辑需要另外用Python实现Tag或Filter。关于模板这一点，一直以来争论比较多，最近有两篇关于Python模板的比较有意思的文章可供参考：

    #. http://pydanny.blogspot.com/2010/12/stupid-template-languages.html\ （需翻墙）
    #. http://techspot.zzzeek.org/2010/12/04/in-response-to-stupid-template-languages/

-  URL配置虽然强大，但全部要手写，这一点跟Rails的Convention over
   configuration的理念完全相左，高手和初识Django的人配出来的URL会有很大差异。
-  让人纠结的auth模块，Django的auth跟其它模块结合紧密，功能也挺强的，就是做的有点过了，用户的数据库schema都给你定好了，这样问题就来了，比如很多网站要求email地址唯一，可schema里这个字段的值不是唯一的，纠结是必须的了。
-  Python文件做配置文件，而不是更常见的ini、xml或yaml等形式。这本身不是什么问题，可是因为理论上来说settings的值是能够动态的改变的（虽然大家不会这么干），但这不是最佳实践的体现。

总的来说，Django大包大揽，用它来快速开发一些Web运用是很不错的。如果你顺着Django的设计哲学来，你会觉得Django很好用，越用越爽；相反，你如果不能融入或接受Django的设计哲学，你用Django一定会很痛苦，趁早放弃的好。所以说在有些人眼里Django无异于仙丹，但对有一些人来说它又是毒药且剧毒。

Django案例有\ `disqus.com <http://disqus.com>`__\ 、\ `bitbucket.org <http://bitbucket.org>`__\ 、\ `海报网 <http://www.haibao.cn>`__\ 等。

`Pylons <http://www.pylonshq.com>`__ & `TurboGears <http://turbogears.org/>`__ & `repoze.bfg <http://bfg.repoze.org/>`__
------------------------------------------------------------------------------------------------------------------------

|image1|

除了Django另一个大头就是Pylons了，因为TurboGears2.x是基于Pylons来做的，而repoze.bfg也已经并入Pylons
project里这个大的项目里，后面不再单独讨论TurboGears和repoze.bfg了。

Pylons和Django的设计理念完全不同，Pylons本身只有两千行左右的Python代码，不过它还附带有一些几乎就是Pylons御用的第三方模块。Pylons只提供一个架子和可选方案，你可以根据自己的喜好自由的选择Template、ORM、form、auth等组件，系统高度可定制。我们常说Python是一个胶水语言(glue
language)，那么我们完全可以说Pylons就是一个用胶水语言设计的胶水框架:)

选择Pylons多是选择了它的自由，选择了自由的同时也预示着你选择了噩梦：

-  学习噩梦，Pylons依赖于许多第三方库，它们并不是Pylons造，你学Pylons的同时还得学这些库怎么使用，关键有些时候你都不知道你要学什么。Pylons的学习曲线相对比Django要高的多，而之前Pylons的官方文档也一直是人批评的对象，好在后来出了\ `The
   Definitive Guide to
   Pylons <http://pylonsbook.com/en/1.1/>`__\ 这本书，这一局面有所改观。因为这个原因，Pylons一度被誉为只适合高手使用的Python框架。
-  调试噩梦，因为牵涉到的模块多，一旦有错误发生就比较难定位问题处在哪里。可能是你写的程序的错、也可能是Pylons出错了、再或是SQLAlchemy出错了、搞不好是formencode有bug，反正很凌乱了。这个只有用的很熟了才能解决这个问题。
-  升级噩梦，安装Pylons大大小小共要安装近20个Python模块，各有各自的版本号，要升级Pylons的版本，哪个模块出了不兼容的问题都有可能，升级基本上很难很难。至今reddit的Pylons还停留在古董的0.9.6上，SQLAlchemy也还是0.5.3的版本，应该跟这条有关系。所以大家玩Pylons一定要结合virtualenv来玩，给自己留条后路，不然会死得很惨。

Pylons和repoze.bfg的融合可能会催生下一个能挑战Django地位的框架。

Pylons的案例有\ `reddit.com <http://www.reddit.com>`__\ 、\ `dropbox.com <http://www.dropbox.com>`__\ 、\ `quora.com <http://www.quora.com>`__\ 等。

`Tornado <http://www.tornadoweb.org>`__\ & `web.py <http://webpy.org/>`__
-------------------------------------------------------------------------

|image2|

Tornado即是一个web
server（对此本文不作详述），同时又是一个类web.py的micro-framework，作为框架Tornado的思想主要来源于web.py，大家在web.py的网站首页也可以看到Tornado的大佬\ `Bret
Taylor <http://bret.appspot.com>`__\ 的这么一段话（他这里说的FriendFeed用的框架跟Tornado可以看作是一个东西）：

    "[web.py inspired the] web framework we use at FriendFeed [and] the
    webapp framework that ships with App Engine..."

因为有这层关系，后面不再单独讨论Tornado。

web.py的设计理念力求精简（Keep it simple and
powerful），总共就没多少行代码，也不像Pylons那样依赖大量的第三方模块，而是只提供的一个框架所必须的一些东西，如：URL路由、Template、数据库访问，其它的就交给用户自己去做好了。

| 一个框架精简的好处在于你可以聚焦在业务逻辑上，而不用太多的去关心框架本身或受框架的干扰，同时缺点也很明显，许多事情你得自己操刀上。
| 我个人比较偏好这种精简的框架，因为你很容易通过阅读源码弄明白整个框架的工作机制，如果框架那一块不是很合意的话，我完全可以Monkey
  patch一下按自己的要求来。

早期的reddit是用web.py写的，Tornado的案例有\ `friendfeed.com <http://friendfeed.com>`__\ 、\ `bit.ly <http://bit.ly>`__\ 、\ `quora.com <http://www.quora.com>`__\ 和我的开源站点\ `poweredsites.org <http://poweredsites.org>`__\ 等。

`Bottle <http://bottle.paws.de/>`__ & `Flask <http://flask.pocoo.org/>`__
-------------------------------------------------------------------------

|image3|

Bottle和Flask作为新生一代Python框架的代表，挺有意思的是都采用了decorator的方式配置URL路由，如：

.. code-block:: python

    from bottle import route, run

    @route('/:name')
    def index(name='World'):
        return '<b>Hello %s!</b>' % name

    run(host='localhost', port=8080)

Bottle、Flask跟web.py一样，都非常精简，Bottle甚至所有的代码都在那一个两千来行的.py文件里。另外Flask和Pylons一样，可以跟Jinja2、SQLAlchemy之类结合的很好。

不过目前不管是Bottle还是Flask成功案例都还很少。

`Quixote <http://www.quixote.ca/>`__
------------------------------------

之所以要特别说一下Quixote，是因为国内的最大的用Python开发的网站“\ `豆瓣网 <http://www.douban.com>`__\ ”是用Quixote开发的。我只简单翻了一下源代码，没有做过研究，不发表评论，有经验的来补充下。我只是在想，如果豆瓣网交到现在来开发，应该会有更多的选择。

其它（web2py、uliweb、Karrigell、Werkzeug ...）
-----------------------------------------------

欢迎大家补充...

最后关于框架选择的误区
----------------------

在框架的选择问题上，许多人很容易就陷入了下面两个误区中而不自知：

#. 哪个框架最好 －
   世上没有最好的框架，只有最适合你自己、最适合你的团队的框架。编程语言选择也是一个道理，你的团队Python最熟就用Python好了，如果最熟悉的是Ruby那就用Ruby好了，编程语言、框架都只是工具，能多、快、好、省的干完活就是好东西，管TMD是日本鬼子还是美帝造呢！
#. 过分关注性能 －
   其实大部分人是没必要太关心框架的性能的，因为你开发的网站根本就是个小站，能上1万的IP的网站已经不多了，上10万的更是很少很少。在没有一定的访问量前谈性能其实是没有多大意义的，因为你的CPU和内存一直就闲着呢。而且语言和框架一般也不会是性能瓶颈，性能问题最常出现在数据库访问和文件读写上。PHP的Zend
   Framework是出了名的慢，但是Zend
   Framework一样有大站，如：digg.com；常被人说有性能问题的Ruby和Rails，不是照样可以开发出twitter吗？再者现在的硬件、带宽成本其实是很低的，特别有了云计算平台后，人力成本才是最贵的，没有上万的IP根本就不用太在意性能问题，流量上去了花点钱买点服务器空间好了，简单快速的解决性能问题。

注：前面有网友质疑我“Quora是用Pylons开发的”这样的说法不客观，特说明一下，这里所说的某个网站A是用B开发的，只是指A主要或部分是由B开发的，大家就不要再去纠结A还用C了。

.. |image0| image:: /static/2011/01/hdr_logo.gif
   :class: alignnone size-full wp-image-225
   :width: 117px
   :height: 41px
.. |image1| image:: /static/2011/01/pylons_logo.jpg
   :class: alignnone size-full wp-image-226
   :width: 346px
   :height: 102px
.. |image2| image:: /static/2011/01/tornado.png
   :class: alignnone size-full wp-image-227
   :width: 286px
   :height: 72px
.. |image3| image:: /static/2011/01/bottle-logo.png
   :class: alignnone size-full wp-image-228
   :width: 276px
   :height: 100px
