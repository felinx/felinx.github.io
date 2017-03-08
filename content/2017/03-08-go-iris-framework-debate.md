Title: 从iris框架撕逼事件看开源
Date: 2017-03-08 16:50
Category: 编程
Tags: github, 开源, Go, web framework
Slug: 2017/03/go-iris-framework-debate
Authors: 飞龙

[iris](https://github.com/kataras/iris)是一个用Go语言写的Web框架(web framework)，我截了下Github上iris项目的首页如下图：

![iris](/static/2017/03-08-iris.jpg)

作者kataras号称iris是“The **fastest** web framework for Go in (THIS) Earth”，我们来对比看一下另一个Go写的以快著称的Web框架[Gin](https://github.com/gin-gonic/gin)，相对没那么狂:

![gin](/static/2017/03-08-gin.jpg)

两个都宣称自己快，那到底谁最快呢？于是引出了下面这个帖子[iris is faster](https://github.com/gin-gonic/gin/issues/560)，有人在Gin的地盘上说iris更快(注：帖子发生在2016年，它并不是一件新鲜事，只是因为本人刚关注Golang才发现)，这个帖子跟我们在技术社区里常看到的“PHP是最好的编程语言”的口水月经撕逼贴几乎如同一辙，但本帖细节非常精彩，我这里简单还原一下：

- 首先dcu说iris更快，建议Gin向iris学
- 接着Gin主要作者manucorporat说“拿出测试证据来”
- CaptainCodeman给出一些测试结果供参考，但说这测试结果并不靠谱
- Gin的另一贡献者appleboy说“show me the code”，让我看看哪里不靠谱
- 第一个转折点来了，CaptainCodeman说“妈蛋，新的iris版本下我的测试代码通不过，iris作者又不认我的测试结果，一怒之下我把代码删了”
> Sorry @appleboy, after the last update it started failing the unit tests and as the author was unwilling to accept the results anyway so I didn't see any point bothering with it anymore so deleted it all.
- joeybloggs站出来说“iris并没有作者说的那么快”
> It's not as fast as the author portrays
- 于是otraore指出了kataras的测试代码不妥的地方
> @kataras The handler for your benchmark (Iris) was still empty and you're comparing different things here. The benchmarks should be comparing routers, not routers with cached enabled.
- CaptainCodeman跟kataras说你应该接受下大家的批评和改进建议
> @kataras You also need to learn to accept criticism or people pointing out errors in your approach - people telling you the results they get doesn't make them liars or "paid" (who do you think is paying them exactly and why?)
- joeybloggs对CaptainCodeman说“你别费这口舌，我试过，kataras这家伙根本不鸟我:(”
> don't waste your breath @CaptainCodeman I gave the same advice in his repo and all he did was "locked and limited conversation to collaborators" then deleted his reddit account and edited his above comment to claim he doesn't have one.
>
> sorry everyone for the noise.
- 一点值得学习的小插曲: robvdl指出大家不要死揪着url地址路由这点小点的性能不放，它根本不是Web应用的性能瓶颈所在。
> This is something I don't really like so much about the Golang community, everyone seems to be obsessed about who has the fastest router. Who cares? Routing is only a tiny portion of the request time, once you start building real application logic on top, it wont matter anymore what router you chose, but the feature set becomes more important. Can we close this issue already... please?
- kataras终于出现了，态度很好说了句感谢的话，结果却引来了另一个神转折，ar3s3ru嘲笑他英语垃圾(kataras是希腊人)，一股骂河南人的地域歧视贴气息扑面而来。
> @kataras I'm falling in love with your broken english
- ar3s3ru也是找骂，raitucarp马上反击了它，到此此贴已彻底变味。
> @ar3s3ru why in this f**ng day, native english speaker people or people that has perfect capability with their english skill, so rude with non native speaker? could you even speak russia? or chinese maybe? I would falling in love if you can speak them perfectly.

回过头细看下文章开头iris和Gin的Github首页截图对比，就会发现一个非常有意思的现象，两个项目的commit、watch、star、fork数等大体相当，看更新频度项目都比较活跃，但贡献者(contributors)这一项就看出明显差异了，iris只有kataras一个贡献者，而Gin有95个贡献者，很明显Gin是一个真正意义上的社区开源项目，而iris可以认为只是kataras一个人在独舞。进一步挖掘发现iris被推荐好的Go项目的awesome-go给除名了，见[Remove iris from listing](https://github.com/avelino/awesome-go/pull/1135)，关键理由是作者对他人贡献的不尊重：

> steals code, editing git history etc. now he removed third-party's licenses. removing it until he understand that third-party's code never stop being third-party's code and can't be stolen and that editing git history to be only contributor while closing users' pull requests is really bad idea. Hope it's temporary.

基于此，有人大声疾呼大家不要去用iris框架[Why you REALLY should stop using Iris](https://www.reddit.com/r/golang/comments/57w79c/why_you_really_should_stop_using_iris/)，从kataras自己所描述的“专注于iris项目”和iris项目代码的更新频度上来看，kataras是确实是一位积极的程序员：

> Iris is a community-driven project, you suggest and I code.
>
> Unlike other repositories, this one is very active. When you post an issue, you get an answer at the next couple of minutes(hours at the worst). If you find a bug, I am obliged to fix that on the same day.

可问题出就出在他自己做着Open source的事却缺乏Open的心态，不虚心接受他人的建议和批评、不尊重他人的代码贡献，于己于项目都是非常不利的。虽然我看完了iris的官方文档觉得iris还不错，但真要我选Go的Web框架，我肯定不会选择iris。

---
PS：iris号称自己是最快(fastest)，若在我朝按新广告法已是违规了。
