#coding=utf-8
import os
import sys
import logging
import traceback

this_file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_file_path + '/../')

from jutil_py.common_conf import ConfMgr
from jutil_py.common_code import ErrorCode

class Log:
    handler_list = []

    @staticmethod
    def init(log_type="stdout", log_path="", log_level=10, log_format="[%(asctime)s][%(levelname)s]%(message)s"):
        """
        function: 初始化日志
        log_type: 日志类型(stdout:只打印到stdout;file:只打印到文件;stdout_and_file/file_and_stdout:同时打印到stdout和文件)
        log_path: 日志文件路径,在log_type等于stdout不试用此参数
        log_level: 日志级别(DEBUG:10;INFO:20;WARNING:30;ERROR:40;CRITICAL:50),会打印大于等于当前数值的各级日志
        log_format: 日志打印格式,如[%(asctime)s][%(levelname)s]%(message)s
        return: common_code
        """
        
        # 初始化logger
        logger = logging.getLogger(__name__)
        if logger is None:
            print("common_log.Log.init failed to get logger.")
            return ErrorCode.ERROR

        # handler清空
        for hd in Log.handler_list:
            logger.removeHandler(hd)
            Log.handler_list.remove(hd)
        
        if log_type == "stdout":
            return Log.init_stdout_logger(log_level, log_format, is_append=False)
        elif log_type == "file":
            return Log.init_file_logger(log_path, log_level, log_format, is_append=False)
        elif log_type == "stdout_and_file" or log_type == "file_and_stdout":
            ret1 = Log.init_stdout_logger(log_level, log_format, is_append=True)
            ret2 = Log.init_file_logger(log_path, log_level, log_format, is_append=True)
            return (ret1 == ErrorCode.SUCCESS and ret2 == ErrorCode.SUCCESS)
        else:
            print("common_log.Log.init log_type unknow error. log_type={}".format(log_type))
            return ErrorCode.ERROR

        return ErrorCode.SUCCESS 

    @staticmethod
    def init_stdout_logger(log_level, log_format, is_append):
        """
        function: 初始化函数用于打印到stdout,不同于init的主动调用,次函数会被默认执行以保证日志在任何时候可输出
        log_level: 日志级别(DEBUG:10;INFO:20;WARNING:30;ERROR:40;CRITICAL:50),会打印大于等于当前数值的各级日志
        log_format: 日志打印格式,如[%(asctime)s][%(levelname)s]%(message)s
        is_append: True:追加一种日志打印方式(一般用于同时向多文件和stdout打印);False:替换现有的打印方式
        """
        try:
            # 初始化logger
            logger = logging.getLogger(__name__)
            if logger is None:
                print("common_log.Log.init_stdout_logger failed to get logger.")
                return ErrorCode.ERROR
            
            # 初始化handler
            handler = logging.StreamHandler(sys.stdout)

            # 初始化log打印级别
            if log_level is None:
                print("common_log.Log.init_file_logger failed to get log_level.")
                return ErrorCode.ERROR
            logger.setLevel(log_level)

            # 初始化log打印格式
            formatter = logging.Formatter(log_format)
            handler.setFormatter(formatter)
            
            # handler替换或追加
            if not is_append:
                for hd in Log.handler_list:
                    logger.removeHandler(hd)
                    Log.handler_list.remove(hd)
            logger.addHandler(handler)
            Log.handler_list.append(handler)
        
        except:
            traceback.print_exc()
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print("common_log.Log.init_stdout_logger init log exception.")
            return ErrorCode.ERROR

        return ErrorCode.SUCCESS

    @staticmethod
    def init_file_logger(log_path, log_level, log_format, is_append):
        """
        function: 写入文件的log初始化
        log_path: 日志写文件路径
        log_level: 日志级别(DEBUG:10;INFO:20;WARNING:30;ERROR:40;CRITICAL:50),会打印大于等于当前数值的各级日志
        log_format: 日志打印格式,如[%(asctime)s][%(levelname)s]%(message)s
        is_append: True:追加一种日志打印方式(一般用于同时向多文件和stdout打印);False:替换现有的打印方式
        return: common_code
        """
        try:
            # 初始化logger
            logger = logging.getLogger(__name__)
            if logger is None:
                print("common_log.Log.init_file_logger failed to get logger.")
                return ErrorCode.ERROR

            # 初始化handler并设置log文件路径
            if log_path is None:
                print("common_log.Log.init_file_logger failed to get log_path.")
                return ErrorCode.ERROR;
            if len(log_path) > 0 and log_path[0] != '/':
                log_path = ConfMgr.get_root_path() + log_path
            handler = logging.FileHandler(log_path)

            # 初始化log打印级别
            if log_level is None:
                print("common_log.Log.init_file_logger failed to get log_level.")
                return ErrorCode.ERROR
            logger.setLevel(log_level)

            # 初始化log打印格式
            formatter = logging.Formatter(log_format)
            handler.setFormatter(formatter)

            # handler替换或追加
            if not is_append:
                for hd in Log.handler_list:
                    logger.removeHandler(hd)
                    Log.handler_list.remove(hd)
            logger.addHandler(handler)
            Log.handler_list.append(handler)

        except:
            traceback.print_exc()
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            print("common_log.Log.init_file_logger init log exception.")
            return ErrorCode.ERROR

        return ErrorCode.SUCCESS

    @staticmethod
    def debug(msg):
        """
        function: 打印debug日志
        """
        logging.getLogger(__name__).debug(msg)
        return

    @staticmethod
    def info(msg):
        """
        function: 打印info日志
        """
        logging.getLogger(__name__).info(msg)
        return

    @staticmethod
    def warning(msg):
        """
        function: 打印warning日志
        """
        logging.getLogger(__name__).warning(msg)
        return

    @staticmethod
    def error(msg):
        """
        function: 打印error日志
        """
        logging.getLogger(__name__).error(msg)
        return

    @staticmethod
    def critical(msg):
        """
        function: 打印critical日志
        """
        logging.getLogger(__name__).critical(msg)
        return

# 支持未初始化直接使用的情况
Log.init()

# 测试函数
if __name__ == '__main__':
    print("-------------------------------------")
    # log默认初始化前将日志打到stdout
    Log.debug("debug stdout")
    Log.info("info stdout")
    Log.warning("warning stdout")
    Log.error("error stdout")
    Log.critical("critical stdout")

    # 初始化文件打印
    print("-------------------------------------")
    Log.init(log_type="file", log_path="./jutil_py/example/test.log", log_level=20, log_format="[%(asctime)s][%(levelname)s]%(message)s")
    Log.debug("debug file")      # 等级低于level的日志不打印
    Log.info("info file")
    Log.warning("warning file")
    Log.error("error file")
    Log.critical("critical file")

    # 同时stdout和文件打印
    print("-------------------------------------")
    Log.init(log_type="stdout_and_file", log_path="./jutil_py/example/test.log", log_level=20, log_format="[%(asctime)s][%(levelname)s]%(message)s")
    Log.debug("debug stdout_and_file")      # 等级低于level的日志不打印
    Log.info("info stdout_and_file")
    Log.warning("warning stdout_and_file")
    Log.error("error stdout_and_file")
    Log.critical("critical stdout_and_file")




