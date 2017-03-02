打造完美博客，WordPress插件推荐
###############################
:date: 2010-12-27 16:28
:author: 飞龙非龙
:category: PHP, 互联网络
:slug: recommended-wordpress-plugins
:status: published

拜\ `James <http://netwiser.blogspot.com/>`__\ 所托，今年给洋人写一个小的商用插件\ `ROMI-Calculator <http://www.marketet.com/romi-calculator/>`__\ ，为此研究了下WordPress，之后趁热打铁用WordPress搭建了\ `围观网 <http://17weiguan.com>`__\ ，期间围观网经过两次改版，前后这么一择腾，可以说现在对WordPress算是小有了解了。

WordPress是一款强大的博客平台，即使你不懂PHP、CSS、JavaScript，甚至连基本的HTML也一无所知，通过WordPress，只要挑选一个自己喜欢的主题再加上一帮插件，你就可以打造一个完美的属于自己的博客网站。

不过，到目前为止WordPress网站上就有\ **12,455**\ 插件，民间的更是不计其数，要在这成千上万的插件中找到强大实用的插件是件比较困难的事情，特别是对于刚接触WordPress的同学来说，更是头疼。

我也是花了大量时间摸索这么头疼过来的，为了让后来人不再头疼，我这里分享一下我的经验，推荐一些“标配”的WordPress插件。若你发现这里介绍的某个插件的功能在你选择的主题里已经提供了且非常强大，你大可忽略这个插件，一些主题总是会根据自己的需要定制一些功能的。

在说所有的插件之前，先说一下\ `**Akismet** <http://akismet.com/>`__\ ，Akismet可以说是必装的，Akismet是WordPress标配的的反垃圾留言插件，没有这个你的博客可能会被垃圾留言所淹没，Akismet总的来说效果不错，虽然有时候会有误判和漏判，但大多数情况下可以帮你拦截掉垃圾留言和评论，对于个别误判或漏判的手动处理一下就可以了。使用前需要先申请一个Akismet的API
Key才行，到WordPress.Com注册一个账号就有了。James同学开始没装Akismet就吃了苦头:)

**文章、评论类**

-  `关联文章 －
   YARPP <http://mitcho.com/code/yarpp/>`__\ ，你在一些网站的上可能有看到过“相关阅读”、“你可能还喜欢”这样的功能，YARPP要做的就是这个，它可以根据文章的标题、分类、标签等信息来帮你找到跟其相关联的其它文章并列举出来，因为列出来的文章是有相关性的，它能够帮你提高网站的Pages/Visit。另外YARPP对网站的feeds也有效，不过要输出全文的feeds才管用。
-  `最新评论 － Get Recent
   Comments <http://blog.jodies.de/2004/11/recent-comments/>`__\ ，
   WordPress默认的最新评论比较难看不能列出评论内容（有些主题会定制强化这个功能，这里不讨论），而这个插件可以定制最新评论的显示方式，比如我采用的是
   <li>%gravatar %comment\_author: <a href="%comment\_link"
   title="%post\_title">%comment\_excerpt</a></li> 这个格式， 效果如下：

|image0| 飞龙在天: `太有才了。
|:mrgreen:| <http://17weiguan.com/2010/12/10249#comment-314>`__\ ` <http://17weiguan.com/2010/12/10249#comment-314>`__

-  `访问统计 －
   WP-PostViews <http://lesterchan.net/portfolio/programming/php/>`__\ ，
   WP-PostViews是一个文章计数统计插件，可以在文章中显示浏览数，还提供了一些统计功能，比如一定时间内浏览最多的文章，你所看到的用WordPress做的网站上提供日排行、周排行、月排行、总排行之类的功能都是居于这个插件来做的。类似的有另外一个插件叫\ `Top
   10 <http://ajaydsouza.com/wordpress/plugins/top-10/>`__\ 。
-  社会化分享，如果是针对国外用户的网站，这个首选的当然是\ `Sociable <http://wordpress.org/extend/plugins/sociable/>`__\ ，另外要支持Buzz的分享需要装另外一个插件\ `Google
   Buzz for
   Sociable <http://wordpress.org/extend/plugins/google-buzz-for-sociable/>`__\ 。但是Sociable对中文社区的支持不够好，比如新浪微博等。明河共影的\ `wp-share-list <http://www.36ria.com/2217>`__\ 对中文社区的支持非常给力，基本主流的都支持，另外这个不向bShare之类需要依赖于第三方网站，最后一点这个插件还非常酷。飞龙日志文章最下面的分享功能用的就是wp-share-list这个插件。
-  `随机文章 － Random Posts
   widget <http://www.romantika.name/v2/2007/05/02/wordpress-plugin-random-posts-widget/>`__\ ，
   这个不用过多解释，就是帮你生成随机的文章列表。
-  `同步到Twitter － WP to
   Twitter <http://www.joedolson.com/articles/wp-to-twitter/>`__\ ，
   将你的博客日志同步至你的Twitter上，这个需要在twitter上为你的博客注册一个APP，另外这个最好跟缩短网址结合使用，可以用bit.ly的API来缩短网站，去bit.ly注册个账号就有API
   Key了。
-  文章打分、置顶，\ `WP-PostRatings <http://wordpress.org/extend/plugins/wp-postratings/>`__\ 可以给文章按星级打分，在文章页面或首页都可以，功能比较强大，若只想要简单的顶或踩，\ `Vote
   it
   up <http://wordpress.org/extend/plugins/vote-it-up/>`__\ 就够了，具体看你自己的需求了。
-  页面导航（翻页），一般主题都会带页面导航功能的，如果不能让你满意的话，就上\ `WP-PageNavi <http://wordpress.org/extend/plugins/wp-pagenavi/>`__\ 吧，一般主题也都会推荐你用这个插件的。
-  联系页面，\ `Contact Form
   7 <http://contactform7.com/>`__\ ，帮你做一个联系XX页面的，不用多解释，看一下\ `联系飞龙 <http://feilong.me/contact>`__\ 就明白了。另外这个也可以用来做其它用途，比如投稿页面。
-  标签云，标签云的插件非常多，这里介绍一个非常酷的用Flash做的标签云插件\ `WP-Cumulus <http://wordpress.org/extend/plugins/wp-cumulus/>`__\ ，标签云生成后看起来象一个3D的球，你在上面移动鼠标时，这个球会跟着转，就像玩地球仪一样，挺吸引眼球的。不过原生的WP-Cumulus是不支持中文的，你可以下载\ http://feilong.me/wp-content/plugins/wp-cumulus/tagcloud.swf\ 替换默认的这个文件就可以完美支持中文了，下面这张图是围观网上的例子。

|image2|

**SEO类**

-  `Google XML
   Sitemaps <http://www.arnebrachhold.de/redir/sitemap-home/>`__
   它可以帮你自动生成XML格式的网站地图(Sitemaps)文件，并且会并将文件路径加到robots.txt文件中去，有利于Google的搜索收录，当然你也可以登录到\ `Google
   Webmasters <http://www.google.com/webmasters/tools/>`__\ 中手动提交生成的网站地图地址。
-  `All in One SEO
   Pack <http://wordpress.org/extend/plugins/all-in-one-seo-pack/>`__
   一般WordPress主题都会提供对SEO的支持，但各主题对SEO支持的好坏良莠不齐。使用All
   in One SEO
   Pack可以在不修改模板的情况下对WordPress进行SEO搜索引擎优化，定义关键字、页面摘要等信息的生成规则，还可以给每篇页面添加独立的关键词和摘要，加速和优化Google等搜索引擎的索引。注意这个插件不要使用过当，如：优化过当造成过多的关键字堆积，这样可能会被搜索引擎当作作弊而给予降权惩罚。

**广告&流量统计类**

-  `AdSense
   Integrator <http://www.mywordpressplugin.com/adsense-integrator>`__
   广告插件我试了好多个，这个是比较让我满意的，它有一个比较形象的设置界面，让你选择你的广告所在的位置，因为插入的广告其实就是一段HTML代码，你甚至也可以拿它当别的用:)。
-  `Google Analytics for
   WordPress <http://wordpress.org/extend/plugins/google-analytics-for-wordpress/>`__\ ，它可以让你不用手动修改模板文件就可以添加Google
   Analytics的代码到页面中去。

**性能优化类**

-  `WP Super
   Cache <http://ocaoimh.ie/wp-super-cache/>`__\ ，将页面静态化缓存下来，它可以大大降低网站的数据库查询操作，节省系统资源，提高访问速度，结合mod\_rewrite来用的话性能更佳。如果你的网站页面很多这个是必装的了。它还提供了一个preload的功能，可以帮你主动的预先生成一些页面的缓存。
-  页面压缩，压缩页面多余的空格和换行和注释，\ `WP-Compress-HTML <http://www.mandar-marathe.com/wp-compress-html>`__\ 或\ `WP-HTML-Compression <http://www.svachon.com/wp-html-compression/>`__\ 都可以实现这个功能，不过这里面有一点小道道，不能把所有的换行都压缩掉，不然写在CDATA里的Javascripts脚本可能不管用了。
-  `WP Gravatar Mini
   Cache <http://wordpress.org/extend/plugins/wp-gravatar-mini-cache/>`__\ ，缓存Gravatar的头像文件，能否优化性能是个问号。其实它的最大用处是解决Gravatar头像不能正常显示的问题的（拜GFW所赐，现在Gravatar的大头像网站是被墙了的）。不过这个要求你的服务器在国外，若服务器在国内这个插件无效。

**网站后台类**

-  `WordPress Database
   Backup <http://austinmatzko.com/wordpress-plugins/wp-db-backup/>`__\ ，备份博客数据库数据到本地或服务器，也可以设定定时任务发送备份数据文件到你的邮箱。
-  `Regenerate
   Thumbnails <http://www.viper007bond.com/wordpress-plugins/regenerate-thumbnails/>`__\ ，可以帮你重新生成上传图片的特色图片文件，如果你修改过上传图片大小的设置的话。
-  邮件后台，\ `WP-Mail-SMTP <http://wordpress.org/extend/plugins/wp-mail-smtp/>`__\ 可以自定义博客后台邮件地址，让你用SMTP服务器发送系统邮件。而\ `New
   User Email
   Setup <http://wordpress.org/extend/plugins/new-user-email-set-up/>`__\ 是用来自定义注册、找回密码等系统邮件内容的。

希望上面的这些插件介绍能够对你有所帮助，助你打造一个属于自己的完美的WordPress博客。这里介绍的插件我都用过，如果有任何问题或疑问可以直接回帖或\ `联系飞龙 <http://feilong.me/contact>`__\ 。

转载请注明出处：\ http://feilong.me/2010/12/recommended-wordpress-plugins

.. |image0| image:: http://www.gravatar.com/avatar.php?gravatar_id=f34dec9007a004876f7a6c47c100524d&size=20&rating=G
   :class: alignnone
   :width: 20px
   :height: 20px
.. |:mrgreen:| image:: http://17weiguan.com/wp-includes/images/smilies/icon_mrgreen.gif
.. |image2| image:: /static/2010/12/wptagcloud.jpg
   :class: alignnone size-full wp-image-44
   :width: 268px
   :height: 281px
