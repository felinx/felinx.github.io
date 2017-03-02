囧，Amazon AWS EC2硬件故障
##########################
:date: 2011-03-06 12:44
:author: 飞龙非龙
:category: 系统相关
:slug: amazon-aws-ec2-hardware-failure
:status: published

今天早上起来开Gmail又收到一封来自Amazon的邮件，这次不是新功能的Annoucement邮件也不是Billing邮件，而是一封Notice邮件，惊了我一声冷汗，邮件内容如下（部分内容打了马赛克）：

::

    Hello,

     We have noticed that one or more of your instances are running on a host degraded due to hardware failure.

     i-221bdxxx

     The risk of your instances failing is increased at this point. We cannot  determine the health of any applications running on the instances. We  recommend that you launch replacement instances and start migrating to  them.

     Feel free to terminate the instances with the ec2-terminate-instance API when you are done with them.

     Sincerely,

     The Amazon EC2 Team

     Reference: d3941eb8-xxxx-4caa-abc8-db9ae774xxxx

果然，访问我的博客出现502 Bad
Gateway错误，只有nginx还工作正常，我的EC2中的MySQL、mongodb和代码等全部部署在mount进来的一个ebs
volume上，而这个ebs volume居然硬件故障挂了，赶紧进行修复，修复过程如下：

#. 新建一个ebs volume（主要是顺便扩大一下容量，准备给
   `http://www.chinapy.org <http://www.chinapy.org/>`__ 留空间）
#. Attach进来一个备份的snapshot，然后连文件带属性把所有的文件拷贝到新的ebs
   volume里（跟旧的保持一模一样的文件路径和属性）
#. mongodb因为是异常中断的，需要跑--repair修复一下
#. 再重启一下所有相关的进程如MySQL、Python、Fast-CGI进程等
#. OK，一切恢复如初。

如果不是要新建一个ebs
volume的话，只需要Attach进备份的snapshot，再过一下步骤3、4就OK了。

PS:
做好备份很重要，虽然EC2出硬件故障这事很少见，但做好备份是必须的，有备份的snapshot，在AWS上恢复数据是件非常简单的事情。

转载请注明出处：\ http://feilong.me/2011/03/amazon-aws-ec2-hardware-failure
