###支持FIS编译的sublime插件

##功能

* 支持文件保存时进行模块编译
* 支持文件内容右键功能进行模块编译
* 支持模板文件javascript语法高亮和自动完成


## Installation :

![install](http://c.hiphotos.bdimg.com/album/s%3D1000%3Bq%3D90/sign=a744d2ca3b01213fcb334adc64d70da0/eac4b74543a98226e5a8cd348882b9014a90ebbc.jpg)
### Using [Package Control](https://sublime.wbond.net/) (*Recommended*)

For all Sublime Text 2/3 users we recommend install via [Package Control][3].

1. [Install](https://sublime.wbond.net/installation) Package Control if you haven't yet.
2. Use `cmd+shift+P` then `Package Control: Install Package`
3. Look for `FIS` and install it.

### Manual Install

1. Click the `Preferences > Browse Packages…` menu
2. Browse up a folder and then into the `Installed Packages/` folder
3. Download [fis.sublime-package](http://pan.baidu.com/s/1oXKCK) and copy it into the `Installed Packages/` directory
4. Restart Sublime Text

##配置
preferences->package setting->fis->setting Default

* 修改cmd对应数组参数，进行fis编译命令修改。
* 修改fis_on_save,启动或关闭文件保存编译功能，默认开启
* 模板文件修改语法类型为Fis-tpl


##注意事项

* 配置cmd时，建议参数必须加上--no-color,以及mac下用户必须每个命令为一个数组元素，不能带空格。
* mac用户需要在 /etc/launchd.conf 中加入 PATH 环境配置，如setenv PATH /usr/local/bin:/usr/local/sbin:/usr/local/share/npm/bin:/usr/bin:/bin:/usr/sbin:/sbin
