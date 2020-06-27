#coding=utf-8

class ErrorCode:
    # ------------------ 通用基础类型(自定义) -------------
    SUCCESS                 = 0         #处理成功
    ERROR                   = 1         #处理错误
    FAIL                    = 2         #业务失败
    EXCEPTION               = 3         #处理异常

    # --------------------- 框架错误类型 ------------------
    FRAMEWORK_ERROR         = 10001     #框架内部错误
    FRAMEWORK_EXCEPTION     = 10002     #框架内部异常

    # --------------------- 服务错误类型 ------------------
    SERVER_ERROR            = 20001     #服务内部错误
    SERVER_EXCEPTION        = 20002     #服务内部异常

    # --------------------- 网络错误类型 ------------------
    NETWORK_ERROR           = 30001     #网络异常

    # --------------------- 客户端错误类型 ------------------
    CLIENT_ERROR            = 40001     #客户端内部错误
    CLIENT_EXCEPTION        = 40002     #客户端内部异常

    # ------------------ 业务错误类型(自定义) -------------
    BUSINESS_ERROR          = 50001     #业务逻辑错误
    BUSINESS_EXCEPTION      = 50002     #业务异常
    BUSINESS_FAIL           = 50003     #业务失败

class StatusCode:
    # ------------------ 通用基础类型(自定义) -------------
    STOPPED                 = 1         #停止
    PENDING                 = 2         #等待(条件阻塞)
    WAITING                 = 3         #待处理(条件满足)
    INITING                 = 4         #初始化中
    RUNNING                 = 5         #处理中
    SUCCESS                 = 6         #处理成功
    ERROR                   = 7         #处理错误
    INTERRUPTED             = 8         #中断
    GRACE_STOPPING          = 9         #优雅停止中
    FORCE_STOPPING          = 10        #强制停止中
    RELATE_ERROR            = 11        #其他问题导致连带失败


