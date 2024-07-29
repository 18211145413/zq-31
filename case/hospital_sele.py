'''
登录功能自动化
'''
import pytest
from logs_info import log_file;
from setting_info import selenium_setting;
from selenium.webdriver.common.by import By
import time;
import random;
import allure;
from selenium.webdriver.support.select import Select

chr_obj = selenium_setting.get_browser("chrome")

log_obj = log_file.get_log();
@allure.epic("医院信息管理系统")
@allure.feature("登录")
@pytest.mark.parametrize("case_name,username,pwd,think_content,case_type",[("用户名非空验证","","","登录","false_case"),("密码非空验证","wh","","登录","false_case"),("用户名或者密码正确性校验","who","123","登录","false_case")
    ,("登录成功校验","wh","123456","医院信息管理系统","true_case")])
def test_hz_login(case_name,username,pwd,think_content,case_type):
    allure.dynamic.title(case_name);
    chr_obj.get("http://192.168.0.177:8080/hospital_layui");
    time.sleep(3)
    chr_obj.find_element(by=By.XPATH,value="/html/body/div/form/div[1]/div/div/input").click();
    time.sleep(3)
    chr_obj.find_element(by=By.XPATH,value="/html/body/div/form/div[1]/div/dl/dd[3]").click();
    time.sleep(3)
    chr_obj.find_element(by=By.ID,value="username").send_keys(username);
    time.sleep(3)
    chr_obj.find_element(by=By.ID,value="password").send_keys(pwd);
    time.sleep(10)
    chr_obj.find_element(by=By.ID,value="loginBt").click();

    time.sleep(5);

    print(chr_obj.find_element(by=By.XPATH,value='//div[@class="layui-layer-content"]').text)

    if case_type == "false_case":

        assert_content = chr_obj.title

    else:

        assert_content = chr_obj.find_element(by=By.LINK_TEXT,value="医院信息管理系统").text

    if assert_content == think_content:

        log_obj.info(case_name+case_type+"执行成功")

    else:

        log_obj.error(case_name+case_type+"执行失败")

    assert assert_content == think_content



def test_sel_self_reservation():
    chr_obj = test_hz_login();
    time.sleep(3)
    chr_obj.find_element(by=By.LINK_TEXT, value="我的预约").click();
    time.sleep(3)
    chr_obj.find_element(by=By.LINK_TEXT, value="预约医生列表").click();

def test_del_self_reservation():
    chr_obj = test_hz_login();
    time.sleep(3)
    chr_obj.find_element(by=By.LINK_TEXT, value="我的预约").click();
    time.sleep(3)
    chr_obj.find_element(by=By.LINK_TEXT, value="预约医生列表").click();
    time.sleep(3);
    chr_obj.switch_to_frame(chr_obj.find_element(by=By.XPATH,value='//*[@id="top_tabs_box"]/div/div[2]/iframe'));
    time.sleep(3);
    reservation_table = chr_obj.find_element(by=By.ID,value="myReservationList");
    time.sleep(3)
    tbody = chr_obj.find_element(by=By.TAG_NAME,value="tbody");
    time.sleep(3)
    table_trs = tbody.find_elements_by_tag_name("tr");
    #将行中的第2行的列获取到
    nums = len(table_trs)
    index = random.randint(0,nums)
    tds_list = table_trs[index].find_elements_by_tag_name("td");

    tds_list[5].click();

    chr_obj.find_element(by=By.XPATH,value='//*[@id="layui-layer1"]/div[3]/a[1]').click();










