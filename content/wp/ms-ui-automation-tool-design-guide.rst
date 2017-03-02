基于UI Automation的自动化测试工具设计指南
#########################################
:date: 2011-01-20 17:17
:author: 飞龙非龙
:category: 编程开发
:slug: ms-ui-automation-tool-design-guide
:status: published

说明：以下内容是根据2010年我在公司的一次关于UI
Automation的Workshop上的PPT整理而来，在公司我和几位同事基于UI
Automation开发了一款非常强大的UI自动化测试工具，此工具已经在公司得到广泛运用（有十几个产品采用），用于替代昂贵的、且脚本很难维护的商用软件。此文只探讨UIA相关的一些通用技术和一点点UI自动化测试工具的设计经验，因为保密的需要，涉及到公司的这款测试工具部分此文不做介绍。

在没有MSUIA（Microsoft UI
Automation，以下简称UIA）之前，大家只能通过MSAA（Microsoft Active
Accessibility）、Win32
API等Native的方式来操控Windows控件，要想自己写一个UI自动化测试工具是很难很难的，因此这一领域一直被大厂商所垄断，价格也贵得惊人，不是大的软件公司也是用不起这些工具的（除非盗版），比如QTP、Robot、SilkTest等商用工具。UIA定义了一套全新的、针对UI自动化的接口和模式，以往的Win32和MSAA设计出发点并不是为解决UI自动化（Win32旨在提供的通用开发接口，MSAA技术的初衷则是为了方便残疾人使用Windows
程序），而UIA的设计目的（微软也需要一套技术、工具来自动化测试自己的产品）、以及新引入的模式和接口都完全是针对UI自动化测试的。UIA的出现，让草根UI自动化测试工具成为一种可能，看完本文你若有这样的需求就赶紧自己造一个吧:)

在继续介绍UIA之前，大家需要先熟悉UIA的几个名词术语。

**UIA名词解释**
---------------

Elements
~~~~~~~~

在UIA里，每一个UI控件即是一个Automation
Element，所有的Elements是存储在一个树状结构中的，Windows的桌面是这颗树的根结点（RootElement）。

Tree
~~~~

UIA tree就是上面所指的树，每个Application都可以看作是一棵子树。

Properties
~~~~~~~~~~

Element都有一些属性（Properties），比如Automation
ID、Name、ControlType等，要找到一个控件主要是通过这些的属性来查找的。

Control patterns
~~~~~~~~~~~~~~~~

在找到一个控件后，对一个控件进行操控的时候就需要用到这个控件支持的控制模式（Control
patterns）了，比如：一个TextBox的ValuePattern可以用来获取TextBox里面的文字。

Event
~~~~~

当UI控件有什么变动的时候，可能会触发一些事件（比如：弹出HelpText），如果有Client订阅了这个事件则会收到事件的通知。

**UIA的架构**
-------------

|image0|

上图左边那部分叫Client，本文指的是UI自动化测试工具，右边叫Application，指的是被测运用程序。Client和Application在启动的时候都会载入UI
Automation Core(UIAutomationCore.dll），UI自动化测试工具就是通过UI
Automation
Core来操控运用程序的。从这个架构图上也可以看到UIA封装了一些MSAA和Win32的接口、屏蔽了Win32和.NET运用程序的差异，UI
Automation Core对外提供了统一的接口，这也就大大简化了Client这边的实现。

基于UIA这套体系实现UI自动化需要解决的两个核心的问题，一是控件查找（Find
Controls）；二是控件操作（Control manipulation），下面对此分别进行介绍。

**控件查找（Find Controls）**
-----------------------------

UIA除了提供了最基本的遍历整个UIA
tree的API（TreeWalker）外，另外也提供了一些Build-in的控件查找API。

TreeWalker
~~~~~~~~~~

-  GetFirstChild
-  GetNextSibling
-  GetParent
-  …

TreeWalker是标准的对UIA tree的遍历API，它是一切控件查找API的基础。

Build-in Finding（基于scope和filting condition的查找API）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  FindFirst(TreeScope, Condition)
-  FindAll(TreeScope, Condition)
-  ...

UIA自带的这些Build-in的查找API是基于TreeScope和Filting
Condition的，查找控件需要定义一个查找范围和过滤条件。

-  查找范围（TreeScope）是子结点、子孙结点、父结点等这样的树中的范围定义。
-  过滤条件（Filting Condition）可以是逻辑条件（AndCondition、
   OrCondition、NotCondition等）也可以是属性条件（PropertyCondition）

下面是一个最简单的示例，在RootElement桌面下查找子结点里Name属性是“Simple
App”的一个控件，因为是在桌面的子结点（一级），它会是一个Application:

::

    Condition winNameCond = new PropertyCondition(AutomationElement.NameProperty, "Simple App");

    AutomationElement app = AutomationElement.RootElement.FindFirst(TreeScope.Children, winNameCond)

**控件操作（Control manipulation）**
------------------------------------

通过上面的Find
Controls找到一个控件后，接下来就是如何操作它实现UI自动化的问题了，比如：点击一个Button，选择一个TreeViewItem等等。下面是一个已做好封装的UITextBox这个控件类里获取TextBox的文字的参考实现：

::

    public virtual string GetText()
    {
        object o = new object();
        if (this.Element.TryGetCurrentPattern(ValuePattern.Pattern, out o))
        {
            ValuePattern pattern = o as ValuePattern;
            return pattern.Current.Value;
        }
        else
        {
            return "";
        }
    }

如上面的代码所示，控件操作有一个固定的模式，首先尝试获取控件的Control
Pattern，如果控件存在这样的Control
Pattern就通过这个Pattern来操控控件，如果没有则需要自定义这个操作或抛出异常等。

**UI自动化测试工具设计**
------------------------

直接基于UIA来实现UI自动化不是不可以，但没有人会这么蛮干。为了获取一个Textbox里的文字这样简单的事情，得到处拷贝上面那段的代码，这是不可取的。所以针对上面说的两个核心的问题，我们需要在UIA上进行一些简化、封装（当然光有这两点是不够的，比如还需要提供一些Native的支持、UI同步、Log等功能，本文对此不做讨论）：

简化、强化控件查找
~~~~~~~~~~~~~~~~~~

#. 简化是指简化控件查找API，为了找一个控件就需要写一大堆的Code来定义这样那样的过滤条件（见控件查找部分的示例代码），如果能用一个简单的字符串就统一所有这些那就方便多了，很负责的说我们就是这么干的，Automation
   ID、Name、ControlType、Point、Index、或逻辑、与逻辑、通配符、正则表达式、关键路径查找等杂七杂八的各种数据类型统统放到一个字符串里搞定，这也是我们开发的这个工具非常强大的一个地方。
#. 强化是指强化控件查找功能，UIA
   Build-in的查找功能的过滤条件是比较简单的，功能也是非常有限的，比如没有对根据通配符、正则表达式来查找的支持，但是我们可以通过最基本的TreeWalker的API来扩展实现这样的查找功能。

封装控件的操控
~~~~~~~~~~~~~~

封装常用控件的基本操作，如：Button的Click、TreeView的Expand和Collapse、Datagrid的操作等等，使控件的操作变成一个简单的API调用，可以考虑把UIA
ControlType里定义的30几种控件中最常用的控件基本操作都实现了，这样写测试脚本的时候就很安逸了。一些产品中可能会使用一些非标的控件，对于这些自定义的控件，用标准控件的操控API可能不管用，通常通过下面两种方式来解决这个问题，一是继承标准控件，重写操控API的实现，如果能够实现的话；二是让开发人员改代码，尽量不要使用非标控件:)

**UI自动化测试framework设计**
-----------------------------

当有了应手的测试工具后，测试脚本的维护依然是个老大难的问题，这个需要有一个好的自动化测试framework来隔离UI的变化，尽量减少维护成本，一个好的framework大体需要有下面几级的分层：

#. Core －
   framework的核心和通用模块，比如：TestCaseBase、Config、WatchDog、Env、OS、DB操作的封装等等。
#. Dialogs － UI Application、Dialog、Control属性的定义，对于一个大的UI
   dialog，为了方便组织是可以考虑切片成一些小的虚拟的Dialogs的。在Dialogs尽量不要涉及操作逻辑，只放属性的定义就可以了。
#. Key words 或者叫 Wrapper － Key
   words是按case（测试用例）层面的需求抽象出来的，大体对应到case里的一个操作步骤，这一个操作步骤实际上可以包含在一个或多个UI
   dialogs上的操作组合，比如：用户登录可以是一个Key
   word，但它实际上包含了输入用户名、输入密码、点击登录按钮等操作步骤。有了Key
   words对UI
   Dialog的封装，基本上可以做到在UI变化的时候，只修改Dialogs的定义，Key
   words的实现代码很少改动，cases的代码则无需修改（只要case的逻辑没有发生变化）。
#. Test cases － 到了cases层面问题就变得简单了，就是一些Key
   words的简单组合，再加上一些测试结果的验证就OK了。

总之，通过UIA实现一套自己的强大的UI自动化测试工具不是不可能，希望本文对一些从事UI自动化测试的同学有所帮助。

扩展资料：\ ` <http://blogs.msdn.com/b/lixiong/archive/2009/12/05/ui-automation-under-the-hood.aspx>`__

-  http://en.wikipedia.org/wiki/Microsoft_UI_Automation
-  http://blogs.msdn.com/b/lixiong/archive/2009/12/05/ui-automation-under-the-hood.aspx

转载请注明出处：\ http://feilong.me/2011/01/ms-ui-automation-tool-design-guide

.. |image0| image:: /static/2011/01/UI_Automation.jpg
   :width: 804px
   :height: 452px
