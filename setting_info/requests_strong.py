import requests;
import json;
def requests_plus(inter_url,inter_method,inter_parm):

    if inter_method == "get" or inter_method == "delete":

        resp = requests.get(url=inter_url,params=inter_parm,verify=False);

    elif inter_method == "post" or inter_method == "put":

        resp = requests.post(url=inter_url,data=json.loads(inter_parm),verify=False);

    else:

        print("接口请求类型错误!");

    #将接口测试结果返回
    return resp;