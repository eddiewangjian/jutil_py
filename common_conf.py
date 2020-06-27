#coding=utf-8
import os
import sys
import traceback
import configparser

global GLOBAL_CONF
GLOBAL_CONF = {}

class GlobalConf:
    """
    支持dict结构全局配置,分成conf/section/item共3个级别,每个item是一个key-value对
    """

    @staticmethod
    def set_item(conf_name, section_name, key, value):
        """
        function: 设置一个全局item
        conf_name: item所在的conf名称
        section_name: item所在的section名称
        key: item的键
        value: 为item赋值
        """
        if conf_name not in GLOBAL_CONF:
            GLOBAL_CONF[conf_name] = {}
        if section_name not in GLOBAL_CONF[conf_name]:
            GLOBAL_CONF[conf_name][section_name] = {}
        GLOBAL_CONF[conf_name][section_name][key] = value
            
    # 获得一个全局变量,不存在则返回默认值
    @staticmethod
    def get_item(conf_name, section_name, key, default_value=None):
        """
        function: 获取全局配置中指定item的值
        conf_name: item所在的conf名称
        section_name: item所在的section名称
        key: item的键
        default_value: 取值失败时返回值
        """
        try:
            return GLOBAL_CONF[conf_name][section_name][key]
        except KeyError:
            return default_value

    @staticmethod
    def clear_item(conf_name, section_name, key):
        """
        function: 删除全局配置中指定的item
        conf_name: item所在的conf名称
        section_name: item所在的section名称
        key: item的键
        """
        if conf_name in GLOBAL_CONF:
            if section_name in GLOBAL_CONF[conf_name]:
                if key in GLOBAL_CONF[conf_name][section_name]:
                    del GLOBAL_CONF[conf_name][section_name][key]

    @staticmethod
    def set_conf(conf_name, conf_dict):
        """
        function: 为全局配置中设置一个conf
        conf_name: conf的名称
        conf_dict: 参数需要满足section和item两层结构,且item为key-vaue结构,该值可由ConfMgr通过parse_conf获取
        """
        GLOBAL_CONF[conf_name] = conf_dict

    @staticmethod
    def get_conf(conf_name):
        """
        function: 获取全局配置中指定的conf
        conf_name: conf名称
        """
        if conf_name in GLOBAL_CONF:
            return GLOBAL_CONF[conf_name]
        return None
        
    @staticmethod
    def clear_conf(conf_name):
        """
        function: 清空全局变量中指定的conf配置
        """
        if conf_name in GLOBAL_CONF:
            del GLOBAL_CONF[conf_name]

    @staticmethod
    def get_all():
        """
        function: 获取全局变量中所有conf配置
        """
        return GLOBAL_CONF
        
    @staticmethod
    def clear_all():
        """
        function: 清空全局变量中所有conf配置
        """
        GLOBAL_CONF.clear()


class ConfMgr:
    """
    完成conf配置文件的读取和解析
    """
    def __init__(self, root_path):
        """
        初始化时配置根目录
        """
        self.root_path = root_path

    def get_root_path(self):
        """
        返回根目录
        """
        return self.root_path

    def parse_conf(self, conf_path):
        """
        function: 根据读取绝对路径或相对根路径，解析配置文件为section/item两层dict
        conf_path: 配置文件相对根路径或绝对路径
        """
        if len(conf_path) > 0 and conf_path[0] != '/':
            conf_path = self.root_path + "/" + conf_path
            #print("conf_path={}".format(conf_path))

        ret = {}
        confMgr = configparser.ConfigParser()
        try:
            confMgr.read(conf_path)
            for section in confMgr.sections():
                ret[section] = {}
                for item in confMgr.items(section):
                    ret[section][item[0]] = item[1]

            return ret
        except:
            traceback.print_exc()
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print("parse_conf exception.")
            return None

    def get_value_str(self, conf_path, section, key, default_value=None):
        """
        function: 实时读取配置文件,返回str格式的配置value
        conf_path: 配置文件相对根路径或绝对路径
        section: 配置文件的分段名
        key: section内的配置key
        default_value: 不存在或者异常时返回默认值,缺省为None
        return: str格式的配置value
        """
        if len(conf_path) > 0 and conf_path[0] != '/':
            conf_path = self.root_path + "/" + conf_path
            #print("conf_path={}".format(conf_path))

        confMgr = configparser.ConfigParser()
        try:
            confMgr.read(conf_path)
            value = confMgr.get(section, key)
            return value
        except:
            traceback.print_exc()
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print("get_value_str exception.")
            return default_value

    def get_value_int(self, conf_path, section, key, default_value=None):
        """
        function: 实时读取配置文件,返回int格式的配置value
        conf_path: 配置文件相对根路径或绝对路径
        section: 配置文件的分段名
        key: section内的配置key
        default_value: 不存在或者异常时返回默认值,缺省为None
        return: int格式的配置value
        """
        value_str = self.get_value_str(conf_path, section, key)
        if value_str is None:
            return default_value
        try:
            value_int = int(value_str)
            return value_int
        except:
            traceback.print_exc()
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print("get_value_int exception.")
            return default_value
     
    def get_value_float(self, conf_path, section, key, default_value=None):
        """
        function: 实时读取配置文件,返回float格式的配置value
        conf_path: 配置文件相对根路径或绝对路径
        section: 配置文件的分段名
        key: section内的配置key
        default_value: 不存在或者异常时返回默认值,缺省为None
        return: float格式的配置value
        """
        value_str = self.get_value_str(conf_path, section, key)
        if value_str is None:
            return default_value
        try:
            value_float = float(value_str)
            return value_float
        except:
            traceback.print_exc()
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print("get_value_float exception.")
            return default_value
            
#测试函数
if __name__ == "__main__":
    pass
    # test GlobalConf
    print("----------------------------------------")
    GlobalConf.set_item("conf_name1", "session", "port", 8001)
    GlobalConf.set_item("conf_name2", "session", "port", 8002)
    GlobalConf.set_item("conf_name2", "session", "addr", "127.0.0.1")
    print("global_conf={}".format(GlobalConf.get_all()))
    print("conf1={}".format(GlobalConf.get_conf("conf_name1")))
    print("item2={}".format(GlobalConf.get_item("conf_name2", "session", "port")))
    GlobalConf.clear_item("conf_name2", "session", "port")
    print("global_clear_item2={}".format(GlobalConf.get_all()))
    GlobalConf.clear_conf("conf_name1")
    print("global_clear_conf1={}".format(GlobalConf.get_all()))
    GlobalConf.clear_all()
    print("global_clear_all={}".format(GlobalConf.get_all()))
    this_file_path = os.path.dirname(os.path.abspath(__file__))
    conf_mgr = ConfMgr(this_file_path + "/example")
    GlobalConf.set_conf("conf_name3", conf_mgr.parse_conf("example_conf_file.conf"))
    print("global_set_conf={}".format(GlobalConf.get_all()))

    # test ConfMgr 
    print("----------------------------------------")
    this_file_path = os.path.dirname(os.path.abspath(__file__))
    conf_mgr = ConfMgr(this_file_path + "/example")
    print("root_dir={}".format(conf_mgr.get_root_path()))
    print("conf_dict={}".format(conf_mgr.parse_conf("example_conf_file.conf")))
    print("value_str={}".format(conf_mgr.get_value_str("example_conf_file.conf", "section_name", "key_name")))
    print("value_int={}".format(conf_mgr.get_value_int("example_conf_file.conf", "section_name", "key_name")))
    print("value_float={}".format(conf_mgr.get_value_float("example_conf_file.conf", "section_name", "key_name")))


