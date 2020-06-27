# jutil_py
python公共util库,封装通用的错误码、log、配置、检查宏命令、数据库访问、可视化出图、通用编解码、通用系统操作

## Deploy
```
pip3 install configparser   # common_conf
pip3 install logging        # common_log
pip3 install requests       # common_http
pip3 install pymysql        # common_mysql
pip3 install matplotlib     # common_plot
```

## QuickStart
```
# 将jutil_py作为子模块直接引用即可使用,调用函数详见API Document
from jutil_py.common_xxx import XXX
```

## API Document
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

### common_http模块
<strong>- 功能：静态类封装http的get/post/put/delete请求</strong>

<strong>- 使用说明：</strong>
```
# 发送一个http请求
# request_type: 请求类型(get/post/put/delete)
# url: 请求url
# params: dict格参数,追加于url的参数
# data: dict格式data,请求时会自动转为json的data
# headers: dict格式的请求headers
# timeout: 超时秒数
# return: 元组(status_code, return_text如果为josn会自动转为dict)
res = Http.request(request_type="post", url="http://cgi.slightheat.com:8002/abc.AiBrainService/echo", params={}, data={"message": "hello"}, headers={'Content-Type': 'text/plain'}, timeout=3)
```

### common_mysql模块
<strong>- 功能：静态类封装mysql的一次single连接请求</strong>

<strong>- 使用说明：</strong>
```
# 发送一个单连接mysql请求
# host: mysql服务的host
# port: mysql服务的端口
# db: 连接的数据库
# user: mysql用户名
# passwd: mysql密码
# sql: 数据库sql请求
res = Mysql.query("127.0.0.1", 3306, "db_name", "work", "passwd@123", "select * from user_info")
```

### common_plot模块
<strong>- 功能：绘制图片类库封装</strong>

<strong>- 使用说明：</strong>
```
# 绘制曲线到图片中
# x_data: x轴数据列表
# y_data: y轴数据列表(x_data与y_data需要等长)
# file_path: 保存的图片文件路径
# file_format: 图片格式
# title: 图片内部的名称
# x_name: x轴名称
# y_name: y轴名称
# line_style: 曲线的形状
# marker: 采样点的形状
# color: 曲线颜色

# 静态函数用于绘制单个曲线到图片
xData = [0, 1, 2, 3, 4, 5]
yData1 = [0, 2, 4, 6, 8, 10]
yData2 = [0, 3, 6, 9, 12, 15]
Plot.single_plot(xData, yData1, file_path="./example/single_plot.png", file_format="png", title='result', x_name='x-axis', y_name='y-axis', line_style='--', marker='.', color='b')

# 使用实例在一张图中打印多条曲线
pt = Plot()
pt.reset()
pt.add_line(xData, yData1, 'func1', line_style='-', marker='.', color='b')
pt.add_line(xData, yData2, 'func2', line_style='--', marker='o', color='r')
pt.multi_plot(file_path='./example/multi_plot.png', file_format='png', title='result', x_name='x-axis', y_name='y-axis')
```


