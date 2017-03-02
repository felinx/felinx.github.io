Python兼容性编程
################
:date: 2011-02-21 18:17
:author: 飞龙
:category: Python
:slug: learning-python-follow-felinx-part-one
:status: published

鉴于我前面的博客里，Python相关的文章最受欢迎，我决定再接再厉，多写一些跟Python相关的文章，把我琢磨Python的一点经验拿出来分享，算是抛个砖，欢迎大家\ **讨论、拍砖、献花**\ ！

我将主要结合\ `Tornado的源码 <http://github.com/facebook/tornado>`__\ 来讲解一些Python的编程技巧和相对较高级一点的Python知识，这样大家就可以看到活生生的实际运用而不是枯燥的理论。

为什么选择拿Tornado的源码来讲而不是其它的Python项目呢，主要是因为：

#. Tornado的代码规范且质量很高；
#. 代码总量比较小，比较容易掌握；
#. 飞龙对Tornado多多少少有点研究。

注：\ `Tornado(要翻墙) <http://www.tornadoweb.org/>`__\ 是\ `friendfeed.com <http://friendfeed.com>`__\ （已并入facebook）开源出来的一个高性能的异步非阻塞模式的Web
server，同时又是一个类web.py的web框架，关于Tornado
web框架部分的讨论见我的博客“ `浅谈Python
web框架 <http://feilong.me/2011/01/talk-about-python-web-framework>`__\ ”相应的部分，对于Tornado的web
server的性能，可以参考Tornado官方主页和\ http://nichol.as/benchmark-of-python-web-servers\ 的介绍。

看了本篇标题，有些朋友可能会很好奇，啥不好讲为什么先讲兼容性这个话题？原因其实很简单，因为这部分的代码经常出现在Python文件的开头:)

系统兼容
--------

Python和许多具有虚拟机的语言一样，支持跨平台，基本可以一次编写到处运行，所以大部分时候大家不用考虑系统兼容性的问题，跟系统相关的能用Python现成的API的就用，不要自己去蛮干就行。比如文件路径的拼接，你别自己傻乎乎的去做字符串拼接，而是用已封装好的os.path.join来实现。

如果你要实现的功能跟系统强相关或在不同的系统中实现是完全不一样的，那就需要考虑这个问题了，这个时候一般是把相关的API封装成一致，然后根据系统信息来选择不同的实现模块，Tornado示例代码如下（模块和代码行数见第一行注释，注：代码行可能会随着Tornado的升级而稍有变化，后面不再做特别说明）：

::

    # tornado.httpserver line 32
    try:
        import fcntl
    except ImportError:
        if os.name == 'nt':
            from tornado import win32_support as fcntl
        else:
            raise

在windows上运行和在linux下运行，导入的fcntl模块是不同的，windows下导入的是Tornado的win32\_support这个实验性质的模块，当然API接口做的跟fcntl是一致的，而在具体用到fcntl的部分就不再需要考虑系统兼容性的问题了，更复杂一点的一个例子见：

::

    # tornado.ioloop line 539
    # Choose a poll implementation. Use epoll if it is available, fall back to
    # select() for non-Linux platforms
    if hasattr(select, "epoll"):
        # Python 2.6+ on Linux
        _poll = select.epoll
    elif hasattr(select, "kqueue"):
        # Python 2.6+ on BSD or Mac
        _poll = _KQueue
    else:
        try:
            # Linux systems with our C module installed
            import epoll
            _poll = _EPoll
        except:
            # All other systems
            import sys
            if "linux" in sys.platform:
                logging.warning("epoll module not found; using select()")
                _poll = _Select

其实就是在不同的操作系统上选择不同的poll实现，至于模块在不同操作系统是如何实现那是另一个问题了。

通过这种方式可以有效的屏蔽不同系统下的编程差异，降低系统兼容性编程的复杂度。

向下兼容
--------

软件版本都避免不了升级，版本一多就有了版本向下兼容的问题（特别的，Python3.x是不向下兼容Python2.x的），这个时候代码里就需要一些向下兼容的代码，主要表现有两种，下面分别介绍：

兼容不同的Python版本
~~~~~~~~~~~~~~~~~~~~

这类最常见的就是用try、import、except三者组成的黄金搭档，Tornado代码举例如下：

::

    # tornado.escape line 24
    # json module is in the standard library as of python 2.6; fall back to
    # simplejson if present for older versions.
    try:
        import json
        assert hasattr(json, "loads") and hasattr(json, "dumps")
        _json_decode = json.loads
        _json_encode = json.dumps
    except:
        try:
            import simplejson
            _json_decode = lambda s: simplejson.loads(_unicode(s))
            _json_encode = lambda v: simplejson.dumps(v)
        except ImportError:
            try:
                # For Google AppEngine
                from django.utils import simplejson
                _json_decode = lambda s: simplejson.loads(_unicode(s))
                _json_encode = lambda v: simplejson.dumps(v)
            except ImportError:
                def _json_decode(s):
                    raise NotImplementedError(
                    "A JSON parser is required, e.g., simplejson at "
                    "http://pypi.python.org/pypi/simplejson/")
                _json_encode = _json_decode

这段这么长的代码的目的其实只有一个，就是导入可用的json模块，分别尝试用Python2.6+自带的json模块、simplejson第三方包、django环境里的simplejson（其实和前面的simplejson是一个东西，不过django把它集成到它自己的utils里去了），若都缺的话最后会抛一个常用来表功能未实现的异常（NotImplementedError）。有了这段代码，在Python2.6+、Python2.5+simplejson、Python2.5+django的Python环境下，Tornado的json编解码的功能都能够正常使用。
更常见一点的例子，如：

::

    # tornado.httpserver line 40
    try:
        import ssl # Python 2.6+
    except ImportError:
        ssl = None

    try:
        import multiprocessing # Python 2.6+
    except ImportError:
        multiprocessing = None

然后后面一般会有针对性的处理，如：

::

    if multiprocessing is not None:
        # do something

兼容API的变化
~~~~~~~~~~~~~

无论事先有多好的设计，API的变化多多少少总是不可避免的，API的变化必然会带来软件兼容性的问题，在Python的世界里，因为Python特殊的变量机制（如下图，详见：\ `学好Python必读的几篇文章 <../2011/01/recommended-entries-for-you-to-master-python>`__
里推荐的第二篇文章 `Code Like a Pythonista: Idiomatic
Python <http://python.net/%7Egoodger/projects/pycon/2007/idiomatic/handout.html>`__\ ），

|image0|

这个问题通常变得异常的简单，Tornado示例如下：

::

    # tornado.httpclient line 367
    # For backwards compatibility: Tornado 1.0 included a new implementation of
    # AsyncHTTPClient that has since replaced the original.  Define an alias
    # so anything that used AsyncHTTPClient2 still works
    AsyncHTTPClient2 = AsyncHTTPClient

你没有看错，除了注释，代码其实就那么一行。
Tornado最早的版本就有一个AsyncHTTPClient实现，但是在中间又引人了一个实验性质的AsyncHTTPClient把它命名为AsyncHTTPClient2以示区别，AsyncHTTPClient2比AsyncHTTPClient更强劲，后来功能稳定了Tornado就把AsyncHTTPClient2的代码移到了AsyncHTTPClient中当作默认的实现。

接下来问题就来了，如果直接把AsyncHTTPClient2的代码都去掉，还在用AsyncHTTPClient2的同学一旦升级了Tornado就糟了，而如果继续保持AsyncHTTPClient2的全部代码不动，那就会有两份几乎一模一样的冗余代码，优雅的解决这个问题实际上只需要上面这么一行代码，AsyncHTTPClient2的代码可以全部撤下，因为这样无论用户在用AsyncHTTPClient还是AsyncHTTPClient2，实际用的会是同一个API。

这一解决方案非常实用的，许多地方都可以看到它的影子，再给大家举个例子，旧的多线程模块threading的实现其命名规范是不符合现在的PEP8标准的，而它提供符合PEP8标准的API的方式也很简单，示例代码片段如下：

::

    # python2.6 threading line 799
    # Global API functions

    def currentThread():
        try:
            return _active[_get_ident()]
        except KeyError:
            ##print "current_thread(): no current thread for", _get_ident()
            return _DummyThread()

    current_thread = currentThread

    def activeCount():
        _active_limbo_lock.acquire()
        count = len(_active) + len(_limbo)
        _active_limbo_lock.release()
        return count

    active_count = activeCount

向上兼容
--------

向上兼容这个可能少有人听过，但在Python这奇妙的世界里，还真有这事，这就是神秘的\_\_future\_\_模块，你可能看到过下面这样的代码：

::

    # tornado.httpclient line 19
    from __future__ import with_statement

这就是在消费Python未来的成果（将来或说较新的版本才有的特性），在较低的版本里就可以使用较高版本里才会正式成为Python一部分的新特性，这里是后面的代码有用到with表达式（关于它将来会另外写博客介绍），深入进\_\_future\_\_模块的代码，里面有这么几行：

::

    with_statement = _Feature((2, 5, 0, "alpha", 1),
                              (2, 6, 0, "alpha", 0),
                              CO_FUTURE_WITH_STATEMENT)

前两行tuple分别表示首次引入的版本和预测的即将成为Python正式的一部分的版本信息，针对with表达式，这里的意思就是说with是在Python2.5的版本才实验性引入的，但需要用前面那句import才能够正常使用，而在Python2.6中可能会（实事已经）成为正式Python的一部分，即可以不用import那句就可以直接用了。
\_\_future\_\_里引入的特性都将成为未来版本里实事上的标准，但是在一些实验性引入该特性的低版本里通过\_\_future\_\_也可以用，将来升级了Python版本，用了新特性的代码也不会有兼容性的问题了。

总之，Python很容易写出兼容性很好的程序，可是杯具的是Python3.x不完全兼容2.x，导致Python3.x推出来这么久了迟迟没有得到大规模的运用。

转载请注明出处：\ http://feilong.me/2011/02/learning-python-follow-felinx-part-one

.. |image0| image:: /static/2011/02/ab2tag.jpg
   :width: 153px
   :height: 88px
