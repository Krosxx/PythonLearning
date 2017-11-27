import json

from smtp.myqqemail import MyQQEmail
from urllib import request

with open('smtp/user.json') as js:
    jsonStr = js.read()
user = json.loads(jsonStr)
qqemail = MyQQEmail(user['username'], user['vCode'], 'Vove')

response = request.urlopen("http://www.vove7.cn:800/getCopyright.php")  # 打开网站
htmlContent=response.read()      #获取网站内容
print(htmlContent)

if qqemail.sendQQEmail(['529545532@qq.com'],title="html测试",msg=htmlContent,type='html'):
    print('Send successful')
else:
    print('Send failed')