from selenium import webdriver;
'''
方法: 通过调用selenium对象的某个方法调用本地浏览器对象，并将嗲用到的浏览器对象返回

参数: 浏览器的名称

返回: 相应的浏览器对象


'''
def get_browser(browser_name):

    if browser_name == "chrome":

        #webdriver.Chrome(r"C:\Users\Administrator\AppData\Local\Google\Chrome\Bin\chromedriver.exe");
        return webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe");
    elif browser_name == "firefox":

        pass;
    elif browser_name == "edge":
        pass;
    else:

        print("本框架暂不支持该浏览器")
