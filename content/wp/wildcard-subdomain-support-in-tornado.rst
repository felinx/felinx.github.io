Tornado对子域名和泛域名的支持
#############################
:date: 2012-08-20 12:42
:author: 飞龙
:category: Python
:tags: Tornado, 泛域名
:slug: 2012/08/wildcard-subdomain-support-in-tornado
:status: published

其实Tornado对子域名和泛域名(除了特别说明外，以下子域名和泛域名均简称为泛域名)的支持并不是什么新鲜事，两年多前我用Tornado写的开源网站
http://poweredsites.org
就有了对泛域名的支持，但是Tornado的官方文档里并没有明确对此功能进行说明，虽然源代码里是有注释的，终是有点隐晦，这不，近日mywaiting同学就遇到了这个问题，我应邀特撰此博文，分享下我对此的一点点经验。

通常，用Tornado添加url映射路由表是直接传handlers给Application这种方式的，比如官方的chatdemo：

.. code-block:: python

    class Application(tornado.web.Application):
        def __init__(self):
            handlers = [
                (r"/", MainHandler),
                (r"/auth/login", AuthLoginHandler),
                (r"/auth/logout", AuthLogoutHandler),
                (r"/a/message/new", MessageNewHandler),
                (r"/a/message/updates", MessageUpdatesHandler),
            ]
            settings = dict(
                cookie_secret="43oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
                login_url="/auth/login",
                template_path=os.path.join(os.path.dirname(__file__), "templates"),
                static_path=os.path.join(os.path.dirname(__file__), "static"),
                xsrf_cookies=True,
                autoescape="xhtml_escape",
            )
            tornado.web.Application.__init__(self, handlers, **settings)

这种方式其实添加的是一个域名通配的url映射表，即域名&子域名不限，只要访问能够解析到这个chatdemo上，“/auth/login”
“/auth/login”这些url就都能够正常运行。假设www.feilong.me、abc.feilong.me、feilong2.me这个三个(子)域名均配置为可由这个chatdemo程序来host，那么访问这三个(子)域名均可以正常使用这个chatdemo，总之域名是无关的。

实际上，这种方式它的内部是通过Application里的这个add\_handlers来实现的(原码注释如下)：

.. code-block:: python

    def add_handlers(self, host_pattern, host_handlers):
        """Appends the given handlers to our handler list.

        Note that host patterns are processed sequentially in the
        order they were added, and only the first matching pattern is
        used.  This means that all handlers for a given host must be
        added in a single add_handlers call.
        """

只不过它是隐式的调用这个add\_handlers而已，其关键点就在于第一个参数host\_pattern(匹配域名的)上，上面那种方式，默认添加的host\_pattern是".\*$"，即域名通配，若要支持泛域名，只需要显式的调用add\_handlers来添加相应的host\_pattern和handlers即可。

接下来就以\ `poweredsites的源码 <https://bitbucket.org/felinx/poweredsites>`__\ 来介绍Tornado对泛域名的支持，app.py里的Application里面有这么几句：

.. code-block:: python

    super(Application, self).__init__(handlers, **settings)

    # add handlers for sub domains
    for sub_handler in sub_handlers:
        # host pattern and handlers
        self.add_handlers(sub_handler[0], sub_handler[1])

常见的方式super(Application, self).\_\_init\_\_(handlers,
\*\*settings)添加的是根域名poweredsites的handlers，接着用for循环显式添加的是子域名和泛域名的handlers。这里的sub\_handlers依次放有各子域名的handlers，其最后一个是泛域名的handlers：

.. code-block:: python

    sub_handlers.append(site.sub_handlers)
    sub_handlers.append(blog.sub_handlers)
    sub_handlers.append(admin.sub_handlers)
    # wildcard subdomain handler for project should be the last one.
    sub_handlers.append(project.sub_handlers)

指定的子域名的sub\_handlers(site.sub\_handlers)是这个样子的，这里的第一个元素就是host\_pattern：

.. code-block:: python

    sub_handlers = ["^sites.poweredsites.org$",
                    [
                     (r"/", _WebsiteIndexHandler),
                     (r"/feeds", _WebsitesFeedsHandler),
                     (r"/([a-z0-9]{32})", _WebsiteHandler),
                     (r"/([^/]+)", WebsiteHandler),
                     ]
                    ]

泛域名(project.sub\_handlers)的区别也就在于这第一个元素，即用来做host\_pattern的是通配一些子域名的：

.. code-block:: python

    sub_handlers = ["^[a-zA-Z_\-0-9]*\.poweredsites.org$",
                    [(r"/", ProjectIndexHandler),
                     (r"/top", ProjectTopHandler),
                     (r"/opensource", ProjectOpensourceHandler),
                     ]
                    ]

在用到了泛域名的ProjectIndexHandler里，运行时具体的子域名就可以通过下面这样的方式获得：

.. code-block:: python

    class ProjectIndexHandler(ProjectBaseHandler):
        def get(self):
            subdomain = self.request.host.split(".")[0]

需要说明的是，Tornado里面的url映射表和Django一样是有顺序的，即url依次序由上到下匹配，只要匹配到就立即结束，不再往下匹配，而带子域名和泛域名的url路由其匹配优先级是要高于通配域名".\*$"的(这个不用你操心，add\_handlers会自动为你做到这一点)。同样的，对于泛域名，因为其子域名是通配的，因此指定子域名的handlers需要放到泛域名前添加，如admin、blog这类子域名的handlers要放在泛域名之前，这就是poweredsites里sub\_handlers.append(project.sub\_handlers)放到最后一条的原因，project这条是对应泛域名的，\ http://tornado.poweredsites.org
就是靠这一条来实现的。

备注：需要支持泛域名，首先要你的域名解析支持泛域名。
