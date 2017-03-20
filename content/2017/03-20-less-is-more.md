Title: Less is more
Date: 2017-03-20 12:50
Category: 杂谈
Tags: Go
Slug: 2017/03/less-is-more
Authors: 飞龙

如果老子会说英语，那么“Less is more”一定出于其口，老子在《道德经》中早就有云“曲则全，枉则直，洼则盈，敝则新，少则得，多则惑”，真乃字字珠玑。

相比于上一个时代的全键盘手机，iPhone只有一个Home键是诠释“Less is more”最好的一个例子：
![blackberry](/static/2017/03-20-blackberry.jpg) 
![iphone](/static/2017/03-20-iphone.png)  


Golang的发明人之一Rob Pike则更进一步说[“Less is exponentially more”](https://commandcenter.blogspot.jp/2012/06/less-is-exponentially-more.html)并拿Go举例说：

> I made a list of significant simplifications in Go over C and C++:
>
> - regular syntax (don't need a symbol table to parse)
> - garbage collection (only)
> - no header files
> - explicit dependencies
> - no circular dependencies
> - constants are just numbers
> - ...
>
> And yet, with that long list of simplifications and missing pieces, Go is, I believe, more expressive than C or C++. **Less can be more.**

相比于C/C++，Go砍和简化了很多feature，Go却可以做的更好，而C++却一直在堆feature、堆复杂度中，或许C++已经掉进了复杂复杂再复杂的死胡同里出不来了。

> In the span of an hour at that talk we heard about something like 35 new features that were being planned. In fact there were many more, but only 35 were described in the talk. Some of the features were minor, of course, but the ones in the talk were at least significant enough to call out. Some were very subtle and hard to understand, like rvalue references, while others are especially C++-like, such as variadic templates, and some others are just crazy, like user-defined literals.

以致于C++人士会说“没有generic types是什么鬼？”。

> Early in the rollout of Go I was told by someone that he could not imagine working in a language without generic types. As I have reported elsewhere, I found that an odd remark.

“做加法容易，做减法难”，在iPhone出来之前很难想象手机完全可以没有那么多键(九宫格键盘或全键盘)，深谙“Less is more”这也正是乔布斯牛掰之处。

---
题外话：Rob Pike表示本意是想开发Go作为C++的替代语音的，没想到吸引来的却是一大帮Python/Ruby程序员，难怪身边不少Pythoneer都在玩Go，是该学点Go了！

> "What was the biggest surprise you encountered rolling out Go?" I knew the answer instantly: Although we expected C++ programmers to see Go as an alternative, instead most Go programmers come from languages like Python and Ruby. Very few come from C++.
