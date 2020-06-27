#coding=utf-8
import os
import sys
import traceback
import requests
import json

this_file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_file_path + '/../')

from jutil_py.common_log import Log

class Http:
    common_headers = {
        "Content-Type": "text/plain",
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
    }

    @staticmethod
    def request(request_type, url, params={}, data={}, headers=common_headers, timeout=3):
        '''
        function: http请求
        request_type: 请求类型(get/post/put/delete)
        url: 请求url
        params: dict格参数,追加于url的参数
        data: dict格式data,请求时会自动转为json的data
        headers: dict格式的请求headers
        timeout: 超时秒数
        return: (status_code, return_text如果为josn会自动转为dict)
        '''
        if request_type == "get":
            return Http.get(url, params, headers, timeout)
        elif request_type == "post":
            return Http.post(url, params, data, headers, timeout)
        else:
            Log.error("common_http.Http.request unknow request_type error. type={} url={} params={} data={} headers={} timeout={}".format(
                    request_type, url, params, data, headers, timeout))
            return None

    @staticmethod
    def get(url, params={}, headers=common_headers, timeout=3):
        '''
        function: get请求
        url: 请求url
        params: dict格参数,追加于url的参数
        headers: dict格式的请求headers
        timeout: 超时秒数
        return: (status_code, return_text如果为josn会自动转为dict)
        '''
        try:
            res = requests.get(url=url, params=params, headers=headers)
            try:
                res_dict = json.loads(res.text)
                return (res.status_code, res_dict) 
            except:
                return (res.status_code, res.text) 
        except:
            traceback.print_exc()
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            Log.error("common_http.Http.get exception. url={} headers={} params={}".format(url, headers, params))
            return None
    
    @staticmethod
    def post(url, params={}, data={}, headers=common_headers, timeout=3):
        '''
        function: post请求
        url: 请求url
        params: dict格参数,追加于url的参数
        data: dict格式data,请求时会自动转为json的data
        headers: dict格式的请求headers
        timeout: 超时秒数
        return: (status_code, return_text如果为josn会自动转为dict)
        '''
        try:
            data_json = json.dumps(data)
            res = requests.post(url=url, params=params, data=data_json, headers=headers)
            try:
                res_dict = json.loads(res.text)
                return (res.status_code, res_dict) 
            except:
                return (res.status_code, res.text) 
        except:
            traceback.print_exc()
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            Log.error("common_http.Http.post exception. url={} headers={} params={} data={}".format(url, headers, params, data))
            return None 

    @staticmethod
    def put(url, params={}, data={}, headers=common_headers, timeout=3):
        '''
        function: put请求
        url: 请求url
        params: dict格参数,追加于url的参数
        data: dict格式data,请求时会自动转为json的data
        headers: dict格式的请求headers
        timeout: 超时秒数
        return: (status_code, return_text如果为josn会自动转为dict)
        '''
        try:
            data_json = json.dumps(data)
            res = requests.put(url=url, params=params, data=data_json, headers=headers)
            try:
                res_dict = json.loads(res.text)
                return (res.status_code, res_dict) 
            except:
                return (res.status_code, res.text) 
        except:
            traceback.print_exc()
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            Log.error("common_http.Http.put exception. url={} headers={} params={} data={}".format(url, headers, params, data))
            return None 

    @staticmethod
    def delete(url, params={}, data={}, headers=common_headers, timeout=3):
        '''
        function: delete请求
        url: 请求url
        params: dict格参数,追加于url的参数
        data: dict格式data,请求时会自动转为json的data
        headers: dict格式的请求headers
        timeout: 超时秒数
        return: (status_code, return_text如果为josn会自动转为dict)
        '''
        try:
            data_json = json.dumps(data)
            res = requests.delete(url=url, params=params, data=data_json, headers=headers)
            try:
                res_dict = json.loads(res.text)
                return (res.status_code, res_dict) 
            except:
                return (res.status_code, res.text) 
        except:
            traceback.print_exc()
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])
            Log.error("common_http.Http.delete exception. url={} headers={} params={} data={}".format(url, headers, params, data))
            return None 


if __name__ == '__main__':
    print("get_res={}".format(Http.request("get", "http://www.baidu.com")));
    print("post_res={}".format(Http.request("post", "http://cgi.slightheat.com:8002/abc.AiBrainService/echo", data={"message": "hello"})));

    print("get_res={}".format(Http.get("http://www.baidu.com")));
    print("post_res={}".format(Http.post("http://cgi.slightheat.com:8002/abc.AiBrainService/echo", data={"message": "hello"})));




