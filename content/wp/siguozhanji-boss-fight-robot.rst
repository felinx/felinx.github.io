四国战记外挂(四国助手)
######################
:date: 2013-08-14 23:50
:author: 飞龙
:category: Python
:slug: siguozhanji-boss-fight-robot
:status: published

`四国战记 <http://sgzj.muhegame.com/>`__\ 是我最近玩过的比较不错的一款卡牌手游，玩四国依稀有点当年大学时代玩英雄无敌的感觉，我先无节操的推荐一下这款手游，邀请码就不放了，以免纯广告之嫌，我的号二区水源精华“灰太龙”，有兴趣的可以游戏里来找我(目测四国GM第一个来找我了，杯具鸟)。

2013/08/31更新:
我开发的外挂已实现自动打魔神、CD一到自动找合适的贼打、自动送和获取好友给的行动力、自动刷塔等辅助功能。

2014/02/07更新: 目前功能已非常齐全，且已正式对外服务，请见:
`四国助手 <%20http://sgzj.shouyouqu.com/>`__
`http://sgzj.shouyouqu.com/ <%20http://sgzj.shouyouqu.com/>`__
和对应的\ `淘宝店 <http://cc2046.taobao.com/index.htm>`__
http://cc2046.taobao.com/index.htm

挂机起因
--------

玩四国的除了大RMB玩家外可能都比较缺钱强化卡牌，而游戏里面一个重要的来钱手段就是7月18号开启的魔神战，全服务器的玩家共同砍魔神获得金币或者卡牌奖励，魔神战每天下午1点和晚9点开始持续2小时(除非魔神提前被砍死)，打魔神战有个要命的CD(俗称冷却时间)，CD根据卡组的COST值有些微小差异，COST越低CD越短，但最少差不多也要1分钟，也就是说为了获得较高的金币奖励，玩家不得不开着四国，魔神CD一到马上开砍，不得不说这招对提高游戏日活和用户停留时间应该是帮助蛮大的。而作为一名懒人的我，没有那个精力也没有那个时间盯着手机砍魔神，于是就琢磨是否可以写个机器人挂机砍魔神，事实证明这完全是可以的，因为四国是基于HTTP的且没有用HTTPS。

挂机程序
--------

挂机程序原理很简单，只需要抓包抓到魔神战的HTTP请求URL地址和用户的Cookie，再在魔神战这个时间点启动程序模拟砍魔神的HTTP请求即可。最简单的其实用CURL就可以实现这个功能，不过为了测试并发和加入一些随机因子让机器人更像真人在玩，我后来用Python写了个简单的程序来做这件事。处于xxx考虑，这里我暂且把部分代码用xxx替代，Python代码如下：

::

    # -*- coding: utf-8 -*-
    #
    # @author: Felinx Lee
    # Created on Jul 24, 2013
    #

    # 四国战记刷魔神boss

    import threading
    import os
    import random
    import time
    from datetime import datetime
    from pytz import timezone
    from tornado.httpclient import HTTPClient, HTTPRequest
    from tornado import escape

    max_threads = 1  #  大于1时会用多线程同时砍，事实证明四国战记服务器程序还是蛮靠谱的，多线程并发会放进队列，不能同时砍两次甚至更多次:)

    url_suffix = "siguozhanji.muhenet.com/boss.php?do=Figxxxxxxxxxxxxxxxxxxxxxx"

    users = (
             {"server": "s2", "cookie": "_sid=cookiexxxxxx1"},  # s2 表 2 区
             {"server": "s3", "cookie": "_sid=cookiexxxxxx2"},  # s2 表 3 区
             )

    log = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sg_boss.log")

    def fight(user):
        time.sleep(random.random())

        client = HTTPClient()

        url = "http://%s.%s" % (user["server"], url_suffix)
        request = HTTPRequest(url, headers={"Cookie": user["cookie"]})
        respone = client.fetch(request)

        r = escape.json_decode(respone.body)

        with open(log, "a+") as f:
            tz = timezone("Asia/Shanghai")  # 因为我的服务器在美国，用的是UTC标准时间，这里为了日志记录方便转成了北京时间
            t = datetime.now(tz).strftime("%Y-%m-%d %X")
            s = "%s %s %s\n" % (t, r.get("message", "OK"), r)
            s = escape.utf8(s)

            f.write(s)

    if __name__ == "__main__":
        for i in xrange(0, 40):
            time.sleep(random.randint(1, 2))  # 1.5 avg + 0.5

            for j in xrange(0, max_threads):
                for user in users:
                    t = threading.Thread(target=fight, args=(user,))
                    t.start()

然后在系统的crontab里添加如下这样的一段定时任务，让程序到点自动运行

::

    * 5 * * * python /home/felinx/temp/sg_boss_bot.py
    0-30 6 * * * python /home/felinx/temp/sg_boss_bot.py

    * 13 * * * python /home/felinx/temp/sg_boss_bot.py
    0-30 14 * * * python /home/felinx/temp/sg_boss_bot.py

注意上面的小时即每行的第二个参数是UTC时间的小时，加8就是北京时间，分别对应到13、14、21、22点，0-30指只前半小时生效，因为通常一个小时以后魔神就被那些大神玩家砍死了......

| 比较有意思的是如果机器人帮你砍过了，如果手机上的四国战记是开着的，它会自动切换到魔神战的打斗场景里去。
| 除了魔神战，其它的事情比如自动刷塔、自动砍盗贼是不是也可以做到呢？原则上也是可以的:)

挂机效果
--------

从7月24号我这个挂机机器人上线以来，我的号每次魔神战(基本都是3冰熊的卡组)大概可以砍10w上下的功勋值拿到24w+的游戏金币，有时候还能混到个强化牌加经验的可口食物，但不得不说有些大RMB玩家太疯狂，我的这机器人也砍的没有他们勤快和多分:)

不得不赞一下四国真是一个良心手游，值得推荐。我没有充过钱(四国团队的人要不喜欢了)依然可以玩的挺high，相比我叫MT我就怎么都玩不下去，而且自我第一天开始玩起到现在每天都在玩，现在每天固定要刷完5、6、7塔，有空时砍砍盗贼，当然魔神战没时间盯这就靠这机器人了，我加的那些好友大部分的等级都跟我同步在上升，四国的日活数据还是很不错的，祝贺四国战记团队。

最后，四国团队的人该有一天会发现我在挂机(我都写这了)，把我的设备给封掉吧，然后就没有然后了...

附：写博客的这个时间机器人砍魔神的结果图

|image0|

转载请注明出处：\ http://feilong.me/2013/08/siguozhanji-boss-fight-robot

.. |image0| image:: /static/2013/08/IMG_1490.png
   :class: alignnone size-full wp-image-833
   :width: 960px
   :height: 640px
   :target: /static/2013/08/IMG_1490.png
