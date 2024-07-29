
import xlrd;
import xlutils.copy as cp
'''

方法: 通过传入该方法的路径读取指定的用例文件，将文件中的接口信息存为字典，最后将多个接口组成的接口列表返回

参数:  用例文件的路径    用例的sheet名称

返回值: 接口组成的列表

'''

def read_inter_info(casefileurl,casesheet):

    inter_list = [];
    #首先通过xlrd对象的openworkbook方法读取excel表格
    case_file = xlrd.open_workbook(casefileurl);

    #通过读取到的用例文件获取响应的sheet
    case_sheet = case_file.sheet_by_name(casesheet);

    #通过获取的sheet的nrows属性获取用例的条数
    case_num = case_sheet.nrows;

    #通过for循环获取sheet表格中每一行的用例信息
    for i in range(1,case_num):

        #case_sheet.row(i) = [text:'login_user_002', text:'密码非空验证', text:'登录', text:'http://192.168.0.194:8080/hospital_layui/admin/login', text:'post', text:'{"username":"admin","password":""}', text:'密码不能为空', number:200.0, text:'{"code":500,"msg":"没有此权限，请联系超管！","count":0,"data":null}', text:'×']
        inter_url = case_sheet.row(i)[3].value;
        inter_method = case_sheet.row(i)[4].value;
        inter_parm = case_sheet.row(i)[5].value;
        inter_think = case_sheet.row(i)[6].value;
        inter_name = case_sheet.row(i)[1].value;

        #将获取到的接口的路径，请求方式和参数方式封装成字典形式的接口
        inter_info = {};
        #将信息进行封装
        inter_info["jk_url"] = inter_url;
        inter_info["jk_method"] = inter_method;
        inter_info["jk_parm"] = inter_parm;
        inter_info["jk_think"] = inter_think;
        inter_info["jk_name"] = inter_name;

        #将接口信息存放在接口列表中
        inter_list.append(inter_info)

    #在for执行完毕后，将接口列表返回
    return inter_list

'''
方法: 将测试结果写入excel表格，写入内容包括响应状态码集合，报文集合，结果集合

参数: 响应状态码集合   报文集合   结果集合  用例文件路径  sheet名称

返回值: 无
'''

def write_case_info(resp_code_list,resp_text_list,results,case_url,case_sheet):

    #获取要编辑的用例文件
    case_file = xlrd.open_workbook(case_url);

    #通过xlutils对象的copy方法将要操作的文件读到缓存中。
    new_case_file = cp.copy(case_file);

    #通过缓存文件对象获取要操作的sheet
    case_sheet = new_case_file.get_sheet(case_sheet);

    for i in range(len(resp_code_list)):

        case_sheet.write(i+1,7,resp_code_list[i]);
        case_sheet.write(i+1,8,resp_text_list[i])
        case_sheet.write(i+1,9,results[i]);

    #保存缓存中的内容至用例文件中
    new_case_file.save(case_url);


'''
方法: 将测试结果写入excel表格，写入内容包括响应状态码，报文，结果

参数: 响应状态码   报文   结果  用例文件路径  sheet名称

返回值: 无
'''

def write_case_info_one(case_num,resp_code,resp_text,result,case_url,case_sheet):

    #获取要编辑的用例文件
    case_file = xlrd.open_workbook(case_url);

    #通过xlutils对象的copy方法将要操作的文件读到缓存中。
    new_case_file = cp.copy(case_file);

    #通过缓存文件对象获取要操作的sheet
    case_sheet = new_case_file.get_sheet(case_sheet);

    case_sheet.write(case_num,7,resp_code);
    case_sheet.write(case_num,8,resp_text)
    case_sheet.write(case_num,9,result);

    #保存缓存中的内容至用例文件中
    new_case_file.save(case_url);




