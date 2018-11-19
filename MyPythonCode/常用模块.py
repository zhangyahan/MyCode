# 常用模块之time模块
# import time
# # 时间戳 计算
# print(time.time())
# # 时间对象(本地时间)
# print(time.localtime(time.time()))
# t = time.localtime(time.time())
# print(t.tm_year)  # 获取年份
# print(t.tm_wday)  # 获取星期天
# 
# # 时间对象(UTC时间)
# print(time.gmtime(time.time()))
# 
# # 将结构化时间转换成时间戳
# print(time.mktime(time.localtime()))
# 
# # 将结构化时间转换成字符串时间
# print(time.strftime('%Y-%m%d %H:%M:%S',
#                     time.localtime()))
# 
# # 将字符串时间转换成结构化时间
# print(time.strptime('2016:12:24:15:22:36',
#                     '%Y:%m:%d:%H:%M:%S'))
# 
# print(time.asctime())
# print(time.ctime())



# 常用模块之logging模块
# import logging
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename='loging.log',
#     filemode='w',
#     format='%(asctime)s \
#             %(filename)s \
#             [%(lineno)d]  \
#             %(message)s'
# )
# logging.debug('debug message')
# logging.info('info message')
# logging.warning('warning message')
# logging.error('error message')
# logging.critical('critical message')


# def logger():
#     logger = logging.getLogger()
#     
#     # 向文件发送内容
#     fh = logging.FileHandler('loging.log')
#     # 向屏幕发送内容
#     ch = logging.StreamHandler()
#     
#     fm = logging.Formatter('%(asctime)s %(message)s')
#     
#     fh.setFormatter(fm)  # 向文件输出
#     ch.setFormatter(fm)  # 向屏幕输出
#     
#     logger.addHandler(fh)
#     logger.addHandler(ch)
#     logger.setLevel(logging.DEBUG)
#     return logger
# # ------上设置,下操作---------
# 
# 
# 
# logger = logger()
# 
# logger.debug('hello')
# logger.info('hello')
# logger.warning('hello')
# logger.error('hello')
# logger.critical('hello')


# 常用模块之configparser模块
# import configparser
# 
# 
# # 空字典 config = {}
# config = configparser.ConfigParser()
# 
# config['DEFAULT'] = {
#     'Server': '45',
#     'Server': '45',
# }


# 常用模块之hashlib
# import hashlib
# 
# 
# obj = hashlib.md5('sb'.encode('utf-8'))
# 
# obj.update('hello'.encode('utf-8'))
# 
# print(obj.hexdigest())
# # 5d41402abc4b2a76b9719d911017c592


# os模块常用方法
# os.getcwd(): 获取










