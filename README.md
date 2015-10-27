含源文件如下：

    1.rule_zhuanyeke.py             专业课查询字段集
    2.spider_base.py                获取验证码；模拟登入
    3.spider_gongxuanke.py          公选课爬虫
    4.spider_gongbike.py            公必课爬虫
    5.spider_zhuanyeke.py           专业课爬虫
    6.checker.py                    检查基本合法性
    7.sender.py                     发送至掌上武大空教室API接口

在spider_base.py中填写_id和pwd，作为教务登入的账号密码
运行python spider_gongxuanke.py（或其他两个），根据获得的验证码图片img.jpg，在命令行输入验证码
爬虫获得数据储存至data_gongxuanke（或其他两个）
使用python check.py检查是否符合空教室数据格式
使用python sender.py发送数据
