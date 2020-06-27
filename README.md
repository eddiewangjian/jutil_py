# jutil_py
python公共util库,封装通用的错误码、log、配置、检查宏命令、数据库访问、可视化出图、通用编解码、通用系统操作

## Deploy
pip3 install configparser   #common_conf
pip3 install logging        #common_log

## QuickStart
### common_conf模块
<strong>- 功能：管理系统session配置</strong>

<strong>- 配置格式说明：</strong>
1. 配置文件中,分为section和item两级,配置文件格式如下：
```
# 配置文件demo.conf
[section_name1]
key1 = value1
key2 = value2

[section_name2]
key3 = value3
key4 = value4
```

2. 配置读入内存dict结构,分为conf/section/item三级,如下：
```
GLOBAL_CONF = {
    "conf_name1": {
        "section_name1": {
            "key1": value1,
            "key2": value2
        },
        "section_name2": {
            "key3": value3,
            "key4": value4
        }
    },
    "conf_name2": {
        "section_name3": {
            "key5": value5,
            "key6": value6
        },
        "section_name4": {
            "key7": value7,
            "key8": value8
        }
    }
}
```
<strong>- 类库使用说明：</strong>
1. ConfMgr静态类用于读取配置文件中的信息。可指定根目录,并通过绝对路径或相对根路径,解析整个配置为dict格式;也支持读取配置文件中的一个item
```
# 初始化配置管理,根目录设置为当前文件所在路径
this_file_path = os.path.dirname(os.path.abspath(__file__))
ConfMgr.set_root_path(this_file_path)
res = ConfMgr.get_root_path()

# 读取当前路径下的example_conf_file.conf配置,返回格式为dict
res = ConfMgr.parse_conf("example_conf_file.conf")

# 读取当前路径下example_conf_file.conf配置,获取section为section_name,key为key_name的value,并按照str/int/float格式解读,还支持在最后添加一个参数用来设置读取失败或异常下的填充值,缺省时返回None
res = ConfMgr.get_value_str("example_conf_file.conf", "section_name", "key_name")
res = ConfMgr.get_value_int("example_conf_file.conf", "section_name", "key_name")
res = ConfMgr.get_value_float("example_conf_file.conf", "section_name", "key_name",3.14)
```
2. GlobalConf静态类用于管理配置驻留内存的结构。背后依赖一个GLOBAL_DICT全局dict变量,分为conf/section/item三层,每个item为一个key-value
```
# 内存全局配置设置
GlobalConf.set_item("conf_name1", "session_name1", "key1", value1)
# 通过配置文件初始化内存全局配置中的一个conf
this_file_path = os.path.dirname(os.path.abspath(__file__))
ConfMgr.set_root_path(this_file_path + "/example")
conf_dict = ConfMgr.parse_conf("example_conf_file.conf")
GlobalConf.set_conf("conf_name3", conf_dict)

# 获取内存全局配置中的一个item
res = GlobalConf.get_item("conf_name1", "session_name2", "key3")
# 获取内存全局配置中的一个conf_dict
res = GlobalConf.get_conf("conf_name1")
# 获取全局配置
res = GlobalConf.get_all()

# 内存全局配置清空一个指定item
GlobalConf.clear_item("conf_name2", "session_name3", "key5")
# 内存全局配置清空一个指定conf
GlobalConf.clear_conf("conf_name1")
# 内存全局配置清空
GlobalConf.clear_all()
```

### common_log模块
<strong>- 功能：管理系统log。支持stdout或文件打印、日志分级、格式自定义</strong>

<strong>- 使用说明：</strong>
```
# 【注意】系统在引用common_log模块后，会默认初始化stdout模式，以保证日志至少可输出到stdout

# 初始化一个stdout日志
# log_type: 日志类型(stdout:只打印到stdout;file:只打印到文件;stdout_and_file/file_and_stdout:同时打印到stdout和文件)
# log_path: 日志文件路径,在log_type等于stdout不试用此参数
# log_level: 日志级别(DEBUG:10;INFO:20;WARNING:30;ERROR:40;CRITICAL:50),会打印大于等于当前数值的各级日志
# log_format: 日志打印格式,如[%(asctime)s][%(levelname)s]%(message)s
Log.init(log_type="stdout", log_path="", log_level=10, log_format="[%(asctime)s][%(levelname)s]%(message)s")

# 调用打印日志
Log.debug("debug log")
Log.info("info log")
Log.warning("warning log")
Log.error("error log")
Log.critical("critical log")
```

