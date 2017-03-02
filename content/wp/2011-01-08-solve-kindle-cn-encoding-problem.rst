Kindle中文乱码问题(TXT、PDF)解决办法
####################################
:date: 2011-01-08 11:46
:author: 飞龙
:category: 读书
:tags: Kindle
:slug: 2011/01/solve-kindle-cn-encoding-problem
:status: published

**问题一：文件名、TXT文档、上网等中文变成一个个“口”字问题**\ （已解决的请直接跳到第二条，我这主要记录一下给自己留个底，这部分的内容主要来自网络）

Amazon官方说kindle支持简体中文和繁体中文，事实上也算支持了，但中文支持还是很差，简体中文却大部分无法正常显示，变成“口”字了。这个是因为语言设置（locale）的问题，解决办法很简单，就是改变默认的语言设置，输入以下命令即可：

| ;debugOn
| ~changeLocale zh-CN
| ;debugOff

输入时要注意大小写，具体输入步骤是：在home页面，先按下回车（也就是方向键旁边那个弯弯箭头键），会出现一个输入框，输入第一条命令后，回车，再输入第二条，再回车，再第3条回车。这样就设置成功了，然后重启kindle。

重启步骤：home -> Menu -> Settings -> Menu -> Restart

也就是进入设置那里再按MENU选择restart重启，或者直接滑动那个关机键按住15秒左右就重启了。

重启之后没问题的话，中文显示应该没问题了，不过txt文件支持还是会有些问题，只有utf-8编码的文件能正常显示并打开，但读了几页后就又出现乱码了，这个问题似乎没能够解决。只能发送邮件到name@kindle.com（name是你的kindle账号）来转换格式了，或者用calibre等转换工具转换成MOBI格式了。

**问题二：部分中文PDF文档乱码或是空白**

这个则是因为Kindle里缺少该PDF文件所采用的字体，解决的办法是加入软字体重新打印生成新PDF文件，具体做法如下：

1. 打开PDF文档后选择打印，注意要选择选择\ **打印到PDF而不是打印机**

|image0|

2.打印选项设置(进打印后选择属性)，然后在纸张/质量（Paper/Quality）里选择高级选项（Advanced），再选择下载软字体，如下：

|image1|

3.
开始打印，选择保存文件的路径，打印开始后会有打印页面进度显示，打印生成新的PDF文件就OK了，新的文件传Kindle里就不再乱码了。

BTW：

#. 如果PDF文档锁定了，不允许打印（打印按钮是灰的），这个时候你需要用工具将PDF文件解锁，SysTools
   PDF
   Unlocker（\ http://www.piaoxu.net/12949.html\ ）可以解决这个问题。
#. 有个别文档打印到文件时会出现异常无法打印全部页面的情况，比如共600页，打印出来（生成）的PDF文件只有400页，解决办法就是选择打印页面重新打印后面一部分内容（401－600页），然后用Adobe
   Acrobat Pro将两个文件重新合成为一个文件。

.. |image0| image:: /static/2011/01/pdf_print-265x300.jpg
   :class: alignnone size-medium wp-image-100
   :width: 265px
   :height: 300px
.. |image1| image:: /static/2011/01/224_59455_0478d4526e287dc-288x300.jpg
   :class: alignnone size-medium wp-image-101
   :width: 288px
   :height: 300px
