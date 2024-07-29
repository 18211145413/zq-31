import allure
import pytest

from setting_info import excel_setting,requests_strong;

import difflib;

from logs_info import log_file;



#调用log对象
log_info = log_file.get_log()


case_index = [1];
@allure.epic("医院管理系统")
@allure.feature("登录")
@pytest.mark.parametrize("inter_info",excel_setting.read_inter_info(r"C:\Users\Administrator\Desktop\hospital_case.xls","login"))
def test_login_case(inter_info):




    #inter_info =  {'jk_url': 'http://192.168.0.194:8080/hospital_layui/admin/login', 'jk_method': 'post', 'jk_parm': '{"username":"admin","password":""}', 'jk_think': '密码不能为空', 'jk_name': '密码非空验证'}

    inter_url = inter_info.get("jk_url");
    inter_method = inter_info.get("jk_method");
    inter_parm = inter_info.get("jk_parm");
    inter_think = inter_info.get("jk_think");
    inter_name = inter_info.get("jk_name");
    print(inter_name)
    allure.dynamic.title(inter_name)
    allure.dynamic.description("这是一个接口,aaaaaaa")
    allure.dynamic.link("https://www.baidu.com")
    print(inter_url,"-----",inter_think,"-----",inter_parm)
    resp = requests_strong.requests_plus(inter_url,inter_method,inter_parm);
    if resp.status_code == 200 and difflib.SequenceMatcher(None, resp.text, inter_think).ratio() > 0.8:

        result = "√";
        #接口执行通过，在日志中写入一条普通日志信息
        log_info.info(inter_name+"接口测试通过")

    else:

        result = "×";
        # 接口执行不通过，在日志中写入一条错误日志信息
        log_info.error(inter_name+"接口测试失败"+"---响应信息:"+resp.text)

    excel_setting.write_case_info_one(case_index[0],resp.status_code,resp.text,result,r"C:\Users\Administrator\Desktop\hospital_case.xls","login");

    case_index[0] = case_index[0] + 1

@allure.epic("医院管理系统")
@allure.feature("药品")
@pytest.mark.parametrize("inter_info",excel_setting.read_inter_info(r"C:\Users\Administrator\Desktop\hospital_case.xls","goods"))
def test_goods_case(inter_info):

    #inter_info = {'jk_url': 'http://192.168.1.22:8080/login', 'jk_method': 'post', 'jk_parm': '{"uname":"","upwd":"123456"}', 'jk_think': '用户不能为空', 'jk_name': '用户名非空验证'}
    inter_url = inter_info.get("jk_url");
    inter_method = inter_info.get("jk_method");
    inter_parm = inter_info.get("jk_parm");
    inter_think = inter_info.get("jk_think");
    inter_name = inter_info.get("jk_name");
    allure.dynamic.title(inter_name)
    resp = requests_strong.requests_plus(inter_url,inter_method,inter_parm)

    if resp.status_code == 200 and difflib.SequenceMatcher(None,resp.text,inter_think).ratio() > 0.8:

        result = "√";
        log_info.info(inter_name+"接口测试通过");

    else:

        result = "×";
        log_info.error(inter_name+"接口测试失败")

    excel_setting.write_case_info_one(case_index[0],resp.status_code,resp.text,result,r"C:\Users\Administrator\Desktop\hospital_case.xls","goods");
    case_index[0] = case_index[0] + 1;


