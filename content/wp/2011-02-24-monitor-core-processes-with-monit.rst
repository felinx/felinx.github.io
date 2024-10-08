用monit监控系统关键进程
#######################
:date: 2011-02-24 17:36
:author: 飞龙
:category: IT
:tags: monit
:slug: 2011/02/monitor-core-processes-with-monit
:status: published

`monit <http://mmonit.com/monit/>`__\ 是一款功能强大的系统状态、进程、文件、目录和设备的监控软件，用于\*nix平台，
它可以自动重启那些已经挂掉的程序，非常适合监控系统关键的进程和资源，如：nginx、apache、mysql和cpu占有率等。而监控管理Python进程，常用的是\ `supervisor <http://supervisord.org/>`__\ ，后续会另外撰文介绍。

下面分别介绍monit的安装、配置和启动。

安装
----

在debian或ubuntu上安装monit非常方便，通过下面的命令

::

    sudo apt-get install monit

即可，其它\*nix上也很简单，下载源码走一遍安装三步就OK了。

::

    ./configure
    make
    make install

安装后，默认的配置文件为/etc/monit/monitrc。

配置
----

添加需要监控的进程等信息至monit的配置文件，monit的配置详见下面的示例文件，为了便于理解，关键的配置我都给出了中文的注释。

::

    ##
    ## 飞龙札记 示例monit配置文件，说明：
    ## 1. 域名以example.com为例。
    ## 2. 后面带xxx的均是举例用的名字，需要根据自己的需要修改。
    ##
    ###############################################################################
    ## Monit control file
    ###############################################################################
    #
    # 检查周期，默认为2分钟，对于网站来说有点长，可以根据需要自行调节，这改成30秒。
    set daemon  30

    # 日志文件
    set logfile /var/log/monit.log

    #
    # 邮件通知服务器
    #
    #set mailserver mail.example.com
    set mailserver localhost

    #
    # 通知邮件的格式设置，下面是默认格式供参考
    #
    ## Monit by default uses the following alert mail format:
    ##
    ## --8<--
    ## From: monit@$HOST                         # sender
    ## Subject: monit alert --  $EVENT $SERVICE  # subject
    ##
    ## $EVENT Service $SERVICE                   #
    ##                                           #
    ##  Date:        $DATE                   #
    ##  Action:      $ACTION                 #
    ##  Host:        $HOST                   # body
    ##  Description: $DESCRIPTION            #
    ##                                           #
    ## Your faithful employee,                   #
    ## monit                                     #
    ## --8<--
    ##
    ## You can override the alert message format or its parts such as subject
    ## or sender using the MAIL-FORMAT statement. Macros such as $DATE, etc.
    ## are expanded on runtime. For example to override the sender:
    #
    # 简单的，这只改了一下发送人，有需要可以自己修改其它内容。
    set mail-format { from: webmaster@example.com }

    # 设置邮件通知接收者。建议发到gmail，方便邮件过滤。
    set alert userxxx@gmail.com

    set httpd port 2812 and            # 设置http监控页面的端口
         use address www.example.com   # http监控页面的IP或域名
         allow localhost               # 允许本地访问
         allow 58.68.78.0/24           # 允许此IP段访问
         ##allow 0.0.0.0/0.0.0.0       # 允许任何IP段，不建议这样干
         allow userxxx:passwordxxx     # 访问用户名密码

    ###############################################################################
    ## Services
    ###############################################################################
    #
    # 系统整体运行状况监控，默认的就可以，可以自己去微调
    #
    # 系统名称，可以是IP或域名
    check system www.example.com
        if loadavg (1min) > 4 then alert
        if loadavg (5min) > 2 then alert
        if memory usage > 75% then alert
        if cpu usage (user) > 70% then alert
        if cpu usage (system) > 30% then alert
        if cpu usage (wait) > 20% then alert

    #
    # 监控nginx
    #
    # 需要提供进程pid文件信息
    check process nginx with pidfile /var/run/nginx.pid
        # 进程启动命令行，注：必须是命令全路径
        start program = "/etc/init.d/nginx start"
        # 进程关闭命令行
        stop program  = "/etc/init.d/nginx stop"
        # nginx进程状态测试，监测到nginx连不上了，则自动重启
        if failed host www.example.com port 80 protocol http then restart
        # 多次重启失败将不再尝试重启，这种就是系统出现严重错误的情况
        if 3 restarts within 5 cycles then timeout
        # 可选，设置分组信息
        group server

    #   可选的ssl端口的监控，如果有的话
    #    if failed port 443 type tcpssl protocol http
    #       with timeout 15 seconds
    #       then restart

    #
    # 监控apache
    #
    check process apache with pidfile /var/run/apache2.pid
        start program = "/etc/init.d/apache2 start"
        stop program  = "/etc/init.d/apache2 stop"
        # apache吃cpu和内存比较厉害，额外添加一些关于这方面的监控设置
        if cpu > 50% for 2 cycles then alert
        if cpu > 70% for 5 cycles then restart
        if totalmem > 1500 MB for 10 cycles then restart
        if children > 250 then restart
        if loadavg(5min) greater than 10 for 20 cycles then stop
        if failed host www.example.com port 8080 protocol http then restart
        if 3 restarts within 5 cycles then timeout
        group server
        # 可选，依赖于nginx
        depends on nginx

    #
    # 监控spawn-fcgi进程(其实就是fast-cgi进程)
    #
    check process spawn-fcgi with pidfile /var/run/spawn-fcgi.pid
        # spawn-fcgi一定要带-P参数才会生成pid文件，默认是没有的
        start program = "/usr/bin/spawn-fcgi -a 127.0.0.1 -p 8081 -C 10 -u userxxx -g groupxxx -P /var/run/spawn-fcgi.pid -f /usr/bin/php-cgi"
        stop program = "/usr/bin/killall /usr/bin/php-cgi"
        # fast-cgi走的不是http协议，monit的protocol参数也没有cgi对应的设置，这里去掉protocol http即可。
        if failed host 127.0.0.1 port 8081 then restart
        if 3 restarts within 5 cycles then timeout
        group server
        depends on nginx

虽然在注释里有详细说明，但是我还是要再强调说明几点：

#. start和stop的program参数里的命令必须是全路径，否则monit不能正常启动，比如killall应该是/usr/bin/killall。
#. 对于spawn-fcgi，很多人会用它来管理PHP的fast-cgi进程，但spawn-fcgi本身也是有可能挂掉的，所以还是需要用monit来监控spawn-fcgi。spawn-fcgi必须带-P参数才会有pid文件，而且fast-cgi走的不是http协议，monit的protocol参数也没有cgi对应的设置，一定要去掉protocol
   http这项设置才管用。
#. 进程多次重启失败monit将不再尝试重启，收到这样的通知邮件表明系统出现了严重的问题，要引起足够的重视，需要赶紧人工处理。

当然monit除了管理进程之外，还可以监控文件、目录、设备等，本文不做讨论，具体配置方式可以去参考\ `monit的官方文档 <http://mmonit.com/monit/documentation/monit.html>`__\ 。

启动、停止、重启
----------------

标准的start、stop、restart

::

    sudo /etc/init.d/monit start
    sudo /etc/init.d/monit stop
    sudo /etc/init.d/monit restart

看到正确的提示信息即可，若遇到问题可以去查看配置里指定的日志文件，如/var/log/monit.log。

从我的服务器这几年的运行情况（monit发了的通知邮件）来看，nginx挂掉的事几乎没有，但apache或fast-cgi出问题的情况还是比较多见，赶快用上monit来管理你的服务器以提高服务器稳定性，跟502
Bad Gateway之类错误说拜拜吧。

附件：\ `monit示例配置文件 </static/2011/02/monitrc.txt>`__
(注：下载后请去掉.txt文件后缀)
