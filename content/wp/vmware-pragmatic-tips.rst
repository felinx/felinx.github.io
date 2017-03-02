VMware几个实用技巧
##################
:date: 2011-01-17 13:41
:author: 飞龙非龙
:category: 编程开发
:slug: vmware-pragmatic-tips
:status: published

近日Buzz好友\ `Kyle
Hu <http://www.google.com/profiles/104231231256400902165>`__\ 同学刚碰到一个关于VM的问题（具体见第三条），借此机会整理一下自己使用VM的几个实用技巧与大家分享。

1.VM快照管理
------------

这个功能实在太常用，不用我多废话。这里只是提醒一下还没有用过快照的同学，赶紧的给自己的VM保存点快照吧，这样VM里的系统出了问题或是有其它需要很容易让你还原到原来的某个点，这功能可比Ghost的克隆、恢复真机系统要来的方便的多。快照唯一的毛病就是VM占用的空间大小会急剧增加，是实际增加的空间的好几倍，不知道VMware是怎么搞的。

|image0|

2.扩大硬盘容量
--------------

有时候你可能会遇到原先给定的VM的硬盘空间不够了，这个时候就需要扩大硬盘容量了，如果增加额外的一个硬盘（如下图）能满足需求那问题是比较简单的了。

|image1|

但是有时候可能必须要扩大某个已有的硬盘分区（比如原来D盘只有10G，现在必须把D盘扩大到20G），这个时候就需要用到vmware-vdiskmanager.exe（位于VMware安装路径根目录，如：C:\\Program
Files\\VMware\\VMware
Workstation，有些安装版本可能不自带这个，如果没有就去下一个对应的版本吧），vmware-vdiskmanager.exe的帮助信息非常清楚，如下：

    .. raw:: html

       <div>

    .. raw:: html

       <div>

    VMware Virtual Disk Manager - build 34685.
    Usage: vmware-vdiskmanager.exe OPTIONS diskName \| drive-letter:
    Offline disk manipulation utility
    Options:
    -c                   : create disk; need to specify other create options
    -d                   : defragment the specified virtual disk
    -k                   : shrink the specified virtual disk
    -n <source-disk>     : rename the specified virtual disk; need to
    specify destination disk-name
    -p                   : prepare the mounted virtual disk specified by
    the drive-letter for shrinking
    -q                   : do not log messages
    -r <source-disk>     : convert the specified disk; need to specify
    destination disk-type
    -x <new-capacity>    : expand the disk to the specified capacity
    Additional options for create and convert:
    -a <adapter>      : (for use with -c only) adapter type (ide, buslogic or lsilogic)
    -s <size>         : capacity of the virtual disk
    -t <disk-type>    : disk type id
    Disk types:
    0                 : single growable virtual disk
    1                 : growable virtual disk split in 2Gb files
    2                 : preallocated virtual disk
    3                 : preallocated virtual disk split in 2Gb files
    The capacity can be specified in sectors, Kb, Mb or Gb.
    The acceptable ranges:
    ide adapter : [100.0Mb, 950.0Gb]
    scsi adapter: [100.0Mb, 950.0Gb]
    ex 1: vmware-vdiskmanager.exe -c -s 850Mb -a ide -t 0 myIdeDisk.vmdk
    ex 2: vmware-vdiskmanager.exe -d myDisk.vmdk
    ex 3: vmware-vdiskmanager.exe -r sourceDisk.vmdk -t 0 destinationDisk.vmdk
    ex 4: vmware-vdiskmanager.exe -x 36Gb myDisk.vmdk
    ex 5: vmware-vdiskmanager.exe -n sourceName.vmdk destinationName.vmdk
    ex 6: vmware-vdiskmanager.exe -k myDisk.vmdk
    ex 7: vmware-vdiskmanager.exe -p m:
    (A virtual disk first needs to be mounted at m:
    using the VMware Diskmount Utility.)

    .. raw:: html

       </div>

    .. raw:: html

       </div>

.. raw:: html

   <div>

示例ex
4就是一个扩大硬盘分区的例子，找到对应的你要扩大的.vmdk文件照着做就可以了，比如下面是将我的一个VM的D盘扩大到20G（文件路径有空格得用引号“”括一下）：

.. raw:: html

   </div>

    .. raw:: html

       <div>

    vmware-vdiskmanager.exe -x 20Gb
    “D:\\09.VM\\build\_vm\\vm\_40\\Windows XP Professional-000001.vmdk”

    .. raw:: html

       </div>

.. raw:: html

   <div>

对于Windows系统的VM来说，新增的这部分磁盘空间在VM里暂时是看不到的，需要到系统管理工具里的磁盘管理工具里去分配一下就OK了。

.. raw:: html

   </div>

3.释放硬盘空间
--------------

VM用的时间一长，有个大毛病就是占用的文件空间越来越大，而实际使用的空间并没有那么多（比如Kyle
Hu遇到的问题：VM分区大小是80GB，使用27GB，虚拟机文件夹为41.9GB，困惑！）。具体原因未明，我的理解可能是因为虚拟硬盘在占用某块空间后，即使这块空间后面被释放了（如：文件删除），VM占用的空间也不能完全缩回去。对于这种情况，如果硬盘吃紧心疼这些被吃掉的空间，就需要用到VM的disk
shrink功能来释放这些空间，关于disk
shrink具体见官方的文档：\ http://www.vmware.com/support/ws5/doc/ws_disk_shrink.html\ ，不过disk
shrink有很多限制条件，比如不能有快照、空间不能被预分配等。要使用disk
shrink需要先安装VMware Tools，安装VMware
Tools需要先将你的VM打开，然后按下图选择安装VMware Tools，

|image2|

这样在VM里面就会自动插入一张VMware
Tools的安装盘，VM是Windows系统的话进入光盘安装即可，如果是linux的话，操作步骤大致如下：

    | # 到光驱目录
    | cd /media/cdrom0
    | # 找到VMware Tools压缩文件
    | ls
    | # 解压到TMP文件夹下
    | tar xvfz VMwareTools-8.1.3-203739.tar.gz -C /tmp
    | cd /tmp
    | # 找到VMwareTools安装文件夹
    | ls
    | cd vmware-tools-distrib
    | # 用root权限安装
    | sudo ./vmware-install.pl
    | # 输入密码，一路回车，然后就安装完毕了。
    | #
      这个时候应该有\ ``vmware-toolbox这个命令了，``\ 如果还没有再运行一下vmware-tools-config.pl就OK了。

VMware Tools 安装完成后就可以在VM里按上面提供的链接里讲的那样进行disk
shrink了，做完disk
shrink后VM的使用空间和VM文件实际占用的空间基本能保持一致了。

4.磁盘碎片整理
--------------

跟真机一样，VM使用时间一长，就会产生很多磁盘碎片，VM的性能会有所下降，这个时候可以通过VM的Defragment来整理磁盘碎片。

|image3|

磁盘碎片整理结合上面介绍的disk shrink来使用（在disk
shrink之后）效果更佳。

5.命令行启动VM
--------------

除了通过界面来操作VM，其实也是可以通过命令行来启动一个VM的（这个可能很少有人用到），比如下面的批处理命令能启动并全屏vm-40这个VM：

    start vmware -X “D:\\09.VM\\build\_vm\\vm\_40\\winxppro.vmx”

你还可以在VM的启动项（如：windows的startup，linux的init.d等）里面预先加入一些自定义的任务，这样就可以自动控制一些VM去做一些事情，完成一些自动化的任务了。

转载请注明出处：\ http://feilong.me/2011/01/vmware-pragmatic-tips

.. |image0| image:: /static/2011/01/vm-take-snapshot.jpg
   :class: size-full wp-image-181 aligncenter
   :width: 675px
   :height: 249px
.. |image1| image:: /static/2011/01/vm-add-hd.jpg
   :class: size-full wp-image-182 aligncenter
   :width: 659px
   :height: 474px
.. |image2| image:: /static/2011/01/vm-install-vm-tools.jpg
   :class: size-full wp-image-184 aligncenter
   :width: 449px
   :height: 293px
.. |image3| image:: /static/2011/01/vm-defragment.jpg
   :class: size-full wp-image-186 aligncenter
   :width: 644px
   :height: 555px
