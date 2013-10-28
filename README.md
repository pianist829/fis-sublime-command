###支持FIS编译的sublime插件

###功能

* 支持文件保存时进行模块编译
* 支持文件内容右键功能进行模块编译

###配置
preferences->package setting->fis->setting Default

* 修改cmd对应数组参数，进行fis编译命令修改。
* 修改fis_on_save,启动或关闭文件保存编译功能，默认开启

###注意事项

* 配置cmd时，建议参数必须加上--no-color,以及mac下用户必须每个命令为一个数组元素，不能带空格。
* mac用户需要在 /etc/launchd.conf 中加入 PATH 环境配置，如setenv PATH /usr/local/bin:/usr/local/sbin:/usr/local/share/npm/bin:/usr/bin:/bin:/usr/sbin:/sbin