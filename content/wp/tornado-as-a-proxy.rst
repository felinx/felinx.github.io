用Tornado实现简单的在线代理
###########################
:date: 2011-09-10 23:13
:author: 飞龙
:category: Python
:slug: 2011/09/tornado-as-a-proxy
:status: published

实现代理的方式很多种，流行的web服务器也大都有代理的功能，比如\ http://www.tornadoweb.cn\ 用的就是nginx的代理功能做的tornadoweb官网的镜像。

最近，我在开发一个移动运用(以下简称APP)的后台程序(Server)，该运用需要调用到另一平台产品(Platform)的API。对于这个系统来说，可选的一种实现方式方式是APP同时跟Server&Platform两者交互；另一种则在Server端封装掉Platform的API，APP只和Server交互。显然后一种方式的系统架构会清晰些，APP编程时也就相对简单。那么如何在Server端封装Platform的API呢，我首先考虑到的就是用代理的方式来实现。碰巧最近Tornado邮件群组里有人在讨论\ `using
Tornado as a
proxy <http://groups.google.com/group/python-tornado/browse_thread/thread/4c1ffaa0a0667650?pli=1>`__\ ，贴主提到的运用场景跟我这碰到的场景非常的相似，我把原帖的代码做了些整理和简化，源代码如下：

::

    # -*- coding: utf-8 -*-
    #
    # Copyright(c) 2011 Felinx Lee & http://feilong.me/
    #
    # Licensed under the Apache License, Version 2.0 (the "License"); you may
    # not use this file except in compliance with the License. You may obtain
    # a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
    # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
    # License for the specific language governing permissions and limitations
    # under the License.

    import logging

    import tornado.httpserver
    import tornado.ioloop
    import tornado.options
    import tornado.web
    import tornado.httpclient
    from tornado.web import HTTPError, asynchronous
    from tornado.httpclient import HTTPRequest
    from tornado.options import define, options
    try:
        from tornado.curl_httpclient import CurlAsyncHTTPClient as AsyncHTTPClient
    except ImportError:
        from tornado.simple_httpclient import SimpleAsyncHTTPClient as AsyncHTTPClient

    define("port", default=8888, help="run on the given port", type=int)
    define("api_protocol", default="http")
    define("api_host", default="feilong.me")
    define("api_port", default="80")
    define("debug", default=True, type=bool)

    class ProxyHandler(tornado.web.RequestHandler):
        @asynchronous
        def get(self):
            # enable API GET request when debugging
            if options.debug:
                return self.post()
            else:
                raise HTTPError(405)

        @asynchronous
        def post(self):
            protocol = options.api_protocol
            host = options.api_host
            port = options.api_port

            # port suffix
            port = "" if port == "80" else ":%s" % port

            uri = self.request.uri
            url = "%s://%s%s%s" % (protocol, host, port, uri)

            # update host to destination host
            headers = dict(self.request.headers)
            headers["Host"] = host

            try:
                AsyncHTTPClient().fetch(
                    HTTPRequest(url=url,
                                method="POST",
                                body=self.request.body,
                                headers=headers,
                                follow_redirects=False),
                    self._on_proxy)
            except tornado.httpclient.HTTPError, x:
                if hasattr(x, "response") and x.response:
                    self._on_proxy(x.response)
                else:
                    logging.error("Tornado signalled HTTPError %s", x)

        def _on_proxy(self, response):
            if response.error and not isinstance(response.error,
                                                 tornado.httpclient.HTTPError):
                raise HTTPError(500)
            else:
                self.set_status(response.code)
                for header in ("Date", "Cache-Control", "Server", "Content-Type", "Location"):
                    v = response.headers.get(header)
                    if v:
                        self.set_header(header, v)
                if response.body:
                    self.write(response.body)
                self.finish()

    def main():
        tornado.options.parse_command_line()
        application = tornado.web.Application([
            (r"/.*", ProxyHandler),
        ])
        http_server = tornado.httpserver.HTTPServer(application)
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()

    if __name__ == "__main__":
        main()

运行上面的代码后，访问 http://localhost:8888/
将会完整显示飞龙博客的首页，即代理访问了http://feilong.me/的内容。

我考虑用程序的方式来做代理而不是直接用Nginx来做代理，其中一点是考虑到用程序可以很容易的控制Platform的哪些API是需要代理的，而哪些是要屏蔽掉的，还有哪些可能是要重写的(比如Server的login可能不能直接代理Platform的login，但却要调用到Platform的login
API)。

以上这段代码只是做了简单的页面内容代理，并没有对页面进行进一步的解析处理，比如链接替换等，这些就交个有兴趣的朋友去开发了。基于以上这段代码，将其扩展一下，是完全可以实现一个完整的在线代理程序的。

这段代码我已放到了我的实验项目里，见\ https://bitbucket.org/felinx/labs\ ，我将会放更多类似于这样的实验性质的小项目到这个repository里来，有兴趣的朋友可以关注一下。
