Title: 博客复活
Date: 2017-03-03 17:40
Category: 杂谈
Tags: 杂谈, WordPress, Pelican
Slug: 2017/03/blog-resurrection
Authors: 飞龙

本博客最初于2010年用WordPress搭建开博，初期主要写Python相关的技术为主，逐步演变成变记录工作、生活、学习的碎碎念的地方。WordPress虽然强大但实在太慢，我的vps上还跑了一些站点和服务，后来访问站点经常卡死就想弃用，只一直在线挂着，之后转移到微信公共账号上写了一段时间，不大喜欢微信公共账号相对封闭的体系，陈浩在[为什么我不在微信公众号上写文章](http://coolshell.cn/articles/17391.html)有相似的观点，微信公共号在2016年以后我也停更了，但是我用博客的方式记录的需求一直很强烈，受不了WordPress系统，今天我终于用用Python开发的[Pelican](https://github.com/getpelican/pelican)静态博客系统和[Github Pages](https://pages.github.com)替代了原来的WordPress，博客站点变得清爽和轻量级多了，因为是静态站点了访问速度非常快，重要的是以后的文章可以直接用markdown格式在sublime txt里写，然后提交到github用版本库管理起来，正式发布则只需要一句fabric指令，彻底告别臃肿的WordPress管理后台。

Pelican可以直接导入WordPress站点的文章，迁移到Pelican我只花了少量时间来修复部分文章里面的标签、关键字和文档格式等，几乎是无缝迁移，这也是Pelican的强大之处，目前我已把原站点的所有文章迁移过来并保持了原链接不变。

同时我也把原来在微信公共账号写的一些文章转成了markdown格式迁移了过来，将老的站点文章和微信公共账号的文章合二为一，从此本博客复活，或勤或懒我将继续保持更新。

---
关于Pelican请参考：

- [使用Pelican + Github Pages搭建个人博客](http://www.wengweitao.com/shi-yong-pelican-github-pagesda-jian-ge-ren-bo-ke.html)
- [Pelican Documentation](http://docs.getpelican.com/en/stable/)
- [Migrating from WordPress to Pelican](http://russell.ballestrini.net/migrating-from-wordpress-to-pelican/)
