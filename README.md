######## 生产测试报告 ########

# 在工程目录下运行
pytest -s -q --alluredir report
# 将allure-2.7.0下面的bin文件夹路径放到环境变量的path中
allure generate report/ -o report/html



###### 使用unittest的测试报告生成器 #######

# 在底部加上下面的代码
# def suite():
#     test_login_case = unittest.makeSuite(TestLogin, 'test')
#
#     all_test = unittest.TestSuite((test_login_case,))
#
#     return all_test

# current_time = time.strftime('%Y%m%d%H:%M:%S', time.localtime(time.time()))
# report_file = '履职PC接口' + current_time + '.html'
# file_name = os.path.abspath(os.path.dirname(os.getcwd())
#                             + os.path.sep + ".." + '\\Report\\' + report_file)
# fp = open(file_name, 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="智慧人大宁波人大履职PC接口测试报告",description="详情",)
# runner.run(suite())
# fp.close()