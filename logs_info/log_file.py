import logging;
from logging import StreamHandler,FileHandler,Formatter;
from datetime import date;

#获取系统当前时间
file_name = str(date.today());

def get_log():
    #通过logging对象获取logger
    log = logging.getLogger("logs");

    #设置日志的记录级别
    #logging.basicConfig(level=logging.DEBUG)
    log.setLevel(logging.DEBUG)

    #日志的处理方式  logging对象提供了两种日志处理方式: StreamHandler(流处理) 输出在控制台   FileHandler(文件处理)  输出到指定的日志文件中
    stream_h = StreamHandler();
    file_h = FileHandler("../logs_info/"+file_name+".log",encoding="utf-8");

    #在写入日志前，需要对日志信息进行优化
    fomatter = Formatter("=====%(asctime)s - %(filename)s:%(lineno)d - %(message)s");

    #将优化好的日志信息设置金处理器中。
    stream_h.setFormatter(fomatter);
    file_h.setFormatter(fomatter);

    #将日志的两种处理器添加至log对象
    log.addHandler(stream_h);
    log.addHandler(file_h);

    #将配置好的日志对象返回给调用者
    return log;
