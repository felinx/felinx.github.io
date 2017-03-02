免输入FTP信息自动升级WordPress
##############################
:date: 2010-12-31 21:04
:author: 飞龙
:category: 编程
:tags: Wordpress
:slug: 2010/12/auto-update-wordpress-without-ftp-auth
:status: published

WordPress的3.0.4
修复了一个严重的\ `安全漏洞 <http://cn.wordpress.org/2010/12/30/3-0-4-update/>`__\ ，所以赶紧着手升级飞龙札记的WordPress版本，在管理后台的“更新”页面点击“自动升级”很快就完成了自动更新，系统已成功升级到了3.04。

但是，同样的等我跑去升级\ `围观网 <http://17weiguan.com>`__\ 的时候，却要求我输入FTP信息（主机、用户名、密码等），什么原因造成两者升级的不同呢？

#. 飞龙札记和围观网是运行在两台不同的服务器上，但都是用nginx
   proxy到后台的PHP
   fastcgi进程进行处理的，服务器的配置基本一致，而两个网站用的WordPress文件是一样的，所以首先就可以排除WordPress版本和服务器配置的差异引起的不同。
#. 两个网站的差别主要体现在主题和插件，这些虽然牵涉到WordPress的设置但是跟WordPress本身及插件升级根本没关系，所以也基本可以排除由WordPres设置差异造成两者升级差异的可能性。
#. 而要求输入FTP信息，目的其实是为了下载WordPress升级文件。两个站一个可以自己下，另一个则要提供FTP账户信息，由此看来应该是文件夹权限问题造成的，仔细对比了一下飞龙札记和围观网的代码文件夹权限，发现飞龙札记的代码文件夹所有者和fastcgi进程的用户是同一个，而围观网的则是两个不同的用户。将围观网的代码文件夹所有者改成fastcgi的进程用户（sudo
   chown -R fastcgi-username
   /home/local/weiguan），问题解决，围观网自动升级不再需要输入FTP信息了，WordPress瞬间自动升级完毕，大功告成，哈哈！！同理，若你的后台是Apache，则让文件夹用户和Apache进程用户保持一致即可。

升级WordPress插件这一问题同理，赶快一键自动升级你的WordPress到3.0.4 吧。

.. raw:: html

   <div id="_mcePaste"
   style="position: absolute; left: -10000px; top: 0px; width: 1px; height: 1px; overflow: hidden;">

.. raw:: html

   </p>

.. rubric:: `*WordPress*\ 的\ *3.0.4*
   修复了一个严重的\ *安全漏洞* <http://geekfiles.altervista.org/zh/wordpress-3-0-4-risolve-un-grave-bug-di-sicurezza/>`__
   :name: wordpress的3.0.4-修复了一个严重的安全漏洞
   :class: r

.. raw:: html

   <p>

.. raw:: html

   </div>
