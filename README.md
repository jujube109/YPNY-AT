# 设备监管平台后台管理AUTO-Test

设备监管UI自动化文件结构说明

* YPNY
    * **lib -----> *使用的第三方文件，以及自定义的方法类***
        * data.json ------------> 包含所有的元素定位参数，用户名密码,以json格式存放。用例文件中所有需要的位置值，账号通过调用此文件，实现参数化。
        * Parametri.py ---------> 调用data.json文件中数据的方法类，调用不同的方法获取不同的数据。
        * HwTestReport.py-------> 生成测试用例报告所需模板 
        * 其余文件均为自定义方法类，根据需求添加
    * **page-----> 所有页面的定位点击操作**
        * page.py-------->主页面的操作点击方法类，主要实现点击左侧菜单栏中的按钮实现页面跳转
        * ......--------->不同的页面类文件均继承page.py中的Page类
    * **report------>执行run.py后在此目录下生成report.html的测试报告**
        * report.html
    * **Script-------->存放执行脚本**
        * Images------>图片上传脚本所需要的图片存放目录
        * upload.exe------>图片上传可执行脚本
        * test.au3-------->autoit文件脚本与upload.exe等价，格式不同
    * **TestCase------>用例文件夹，存放每个页面对应的用例脚本**
        * Login_Case------>登录模块下所有的py用例包 
            * __init__.py------>无代码，主要作用为用例执行时，发现查找py用例文件提供标识
            *login_test.py----------->登录用例