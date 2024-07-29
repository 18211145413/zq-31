
from appium import webdriver;

import time;
# device_info = {
#   'platformName': 'Android', # 被测手机是安卓
#   'platformVersion': '5.1.1', # 手机安卓版本
#   'deviceName': 'shouji', # 设备名，安卓手机可以随意填写
#   'appPackage': 'com.tencent.mm', # 启动APP Package名称
#   'appActivity': 'com.tencent.mm.recovery.ui.RecoveryUI', # 启动Activity名称
# }


device_info={
'platformName':'Android',
'platformVersion':'5.1.1',
'deviceName':'xuni',
'appPackage':'com.example.jcy.wvtest',
'appActivity':'com.example.jcy.wvtest.MainActivity',
}
weixin = webdriver.Remote("http://127.0.0.1:4723/wd/hub",device_info);

time.sleep(30)







