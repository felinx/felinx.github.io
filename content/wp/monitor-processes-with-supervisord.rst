用Supervisord管理Python进程
###########################
:date: 2011-03-29 11:51
:author: 飞龙非龙
:category: Python, 系统相关
:slug: monitor-processes-with-supervisord
:status: published

Supervisord是用Python实现的一款非常实用的进程管理工具，类似于\ `monit <http://mmonit.com/monit/>`__\ (关于monit见我的博客:`用monit监控系统关键进程 <http://feilong.me/2011/02/monitor-core-processes-with-monit>`__)，monit和supervisord的一个比较大的差异是supervisord管理的进程必须由supervisord来启动，monit可以管理已经在运行的程序；supervisord还要求管理的程序是非daemon程序，supervisord会帮你把它转成daemon程序，因此如果用supervisord来管理nginx的话，必须在nginx的配置文件里添加一行设置daemon
off让nginx以非daemon方式启动。

Supervisord安装
---------------

Supervisord可以通过\ ``sudo easy_install supervisor``\ 安装，当然也可以通过\ `Supervisord官网 <http://supervisord.org/>`__\ 下载后setup.py
install安装。

Supervisord配置
---------------

Supervisord默认的配置文件路径为/etc/supervisord.conf，通过文本编辑器修改这个文件，下面是一个示例的配置文件：

::

    ;/etc/supervisord.conf
    [unix_http_server]
    file = /var/run/supervisor.sock
    chmod = 0777
    chown= root:felinx

    [inet_http_server]
    # Web管理界面设定
    port=9001
    username = admin
    password = yourpassword

    [supervisorctl]
    ; 必须和'unix_http_server'里面的设定匹配
    serverurl = unix:///var/run/supervisord.sock

    [supervisord]
    logfile=/var/log/supervisord/supervisord.log ; (main log file;default $CWD/supervisord.log)
    logfile_maxbytes=50MB       ; (max main logfile bytes b4 rotation;default 50MB)
    logfile_backups=10          ; (num of main logfile rotation backups;default 10)
    loglevel=info               ; (log level;default info; others: debug,warn,trace)
    pidfile=/var/run/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
    nodaemon=true              ; (start in foreground if true;default false)
    minfds=1024                 ; (min. avail startup file descriptors;default 1024)
    minprocs=200                ; (min. avail process descriptors;default 200)
    user=root                 ; (default is current user, required if root)
    childlogdir=/var/log/supervisord/            ; ('AUTO' child log dir, default $TEMP)

    [rpcinterface:supervisor]
    supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

    ; 管理的单个进程的配置，可以添加多个program
    [program:chatdemon]
    command=python /home/felinx/demos/chat/chatdemo.py
    autostart = true
    startsecs = 5
    user = felinx
    redirect_stderr = true
    ；这对这个program的log的配置，上面的logfile_maxbytes是supervisord本身的log配置
    stdout_logfile_maxbytes = 20MB
    stdoiut_logfile_backups = 20
    stdout_logfile = /var/log/supervisord/chatdemo.log

    ; 配置一组进程，对于类似的program可以通过这种方式添加，避免手工一个个添加
    [program:groupworker]
    command=python /home/felinx/demos/groupworker/worker.py
    numprocs=24
    process_name=%(program_name)s_%(process_num)02d
    autostart = true
    startsecs = 5
    user = felinx
    redirect_stderr = true
    stdout_logfile = /var/log/supervisord/groupworker.log

Supervisord管理
---------------

Supervisord安装完成后有两个可用的命令行supervisor和supervisorctl，命令使用解释如下：

-  supervisord，初始启动Supervisord，启动、管理配置中设置的进程。
-  supervisorctl stop
   programxxx，停止某一个进程(programxxx)，programxxx为\ ``[program:chatdemon]``\ 里配置的值，这个示例就是chatdemon。
-  supervisorctl start programxxx，启动某个进程
-  supervisorctl restart programxxx，重启某个进程
-  supervisorctl stop groupworker:
   ，重启所有属于名为groupworker这个分组的进程(start,restart同理)
-  supervisorctl stop
   all，停止全部进程，注：start、restart、stop都不会载入最新的配置文件。
-  supervisorctl
   reload，载入最新的配置文件，停止原有进程并按新的配置启动、管理所有进程。
-  supervisorctl
   update，根据最新的配置文件，启动新配置或有改动的进程，配置没有改动的进程不会受影响而重启。
-  注意：显示用stop停止掉的进程，用reload或者update都不会自动重启。

转载请注明出处：\ http://feilong.me/2011/03/monitor-processes-with-supervisord
