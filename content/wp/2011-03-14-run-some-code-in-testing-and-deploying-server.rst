如何在开发测试和生产环境下跑同一套Python代码
####################################################
:date: 2011-03-14 13:27
:author: 飞龙
:category: Python
:tags: Python, tips
:slug: 2011/03/run-some-code-in-testing-and-deploying-server
:status: published

通常在开发测试和生产环境下，程序的配置和系统环境等会有所差异，比如最常见的调试DEBUG选项本地一般是开的，而在生产环境这个肯定是要关闭的。手动维护两套配置显然是不明智的，下面介绍一点小技巧，让你可以轻松实现一套代码同时跑在开发测试和生产环境下。

下面以Django为例(Tornado、Pylons等类似)

首先需要判断当前环境是开发环境还是生产环境，常见的方式是检测机器名。

.. code-block:: python

    import platform
    if platform.node() == "FELINX": # FELINX is the name of felinx' EC2 server.
        DEBUG = False
    else:
        DEBUG = True

不清楚机器名的话，可以通过hostname命令来查询和修改，下面是修改的命令。

.. code-block:: python

    sudo hostname xxx

这样在开发环境和生产环境的DEBUG选项就不一样了，接下来对有需要区别对待的配置或代码就可以通过检测DEBUG来进行选择了，比如在\ http://www.chinapy.org\ 的\ `settings\_local.py <https://bitbucket.org/felinx/chinapy/src/tip/chinapy/settings_local.py>`__\ 中有这么一段代码：

.. code-block:: python

    if DEBUG:
        CACHE_BACKEND = 'file://%s' % os.path.join(os.path.dirname(__file__), 'cache').replace('\\', '/')
        SESSION_ENGINE = 'django.contrib.sessions.backends.db'
    else:
        CACHE_BACKEND = 'memcached://127.0.0.1:11211'
        SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

上面就实现了自动选择相应的CACHE和SESSION配置，这样相同的代码就可以跑在开发环境和生产环境了。
