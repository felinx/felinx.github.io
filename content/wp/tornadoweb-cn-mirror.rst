发布Tornado镜像站点tornadoweb.cn
################################
:date: 2011-05-19 15:06
:author: 飞龙
:category: Python
:slug: 2010/05/tornadoweb-cn-mirror
:status: published

鉴于\ `Tornado官网 <http://www.tornadoweb.org>`__\ 架设在GAE上，而GAE在国内被墙，如果不爬墙大家访问不了Tornado官网，这个让很多国内Tornado用户不爽，也影响了Tornado在国内的推广。而我手头一直持有\ `tornadoweb.cn <http://www.tornadoweb.cn>`__\ 和tornadoweb.com.cn两个域名，之前是想开发个Tornado的中文站的，但在目前闲置的情况下，还不如先做一个官方网站的镜像，故今天特配置了一下我EC2上的nginx，做了一个Tornado官方网站的镜像站点\ `tornadoweb.cn <http://www.tornadoweb.cn>`__\ ，以造福国内Tornado用户，以后国内用户就可以直接通过\ `tornadoweb.cn <http://www.tornadoweb.cn/>`__\ 查阅Tornado的文档了。

此举已致信Tornado的Ben：

Hi, Ben,

I have tried to create a mirror
site(\ `http://www.tornadoweb.cn <http://www.tornadoweb.cn/>`__, just
proxy the origin content) of `tornadoweb.org <http://tornadoweb.org/>`__
for Chinese because `tornadoweb.org <http://tornadoweb.org/>`__ is
blocked by GFW in China, so Chinese guys can not view Tornado
documentation online if they do not use any VPNs.

Can I do that? If it is ok, I would like to announce this site to
Tornado uses in China, it's a good news for them really, thanks a lot.

Ben很快回复了，但他希望最好能在头上说明下这是原站的镜像：

Yeah, I think that's fine.  Maybe just add a disclaimer at the top of
the home page that this is a mirror and the official home page is
`tornadoweb.org <http://tornadoweb.org/>`__.

因此，我接着就把tornado的logo文件代理到一个本地新制作的文件，在原logo上加上了是镜像的备注信息(A
mirror of tornadoweb.org)，再次给Ben去了封信，Ben立马就回了。

Yeah, looks good.

OK，此事搞定！

呱唧呱唧，大家还不给飞龙鼓掌:)

转载请注明出处：\ http://feilong.me/2011/05/tornadoweb-cn-mirror
