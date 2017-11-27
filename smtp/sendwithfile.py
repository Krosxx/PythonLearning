import json

from smtp.myqqemail import MyQQEmail

with open('smtp/user.json') as js:
    jsonStr = js.read()
user = json.loads(jsonStr)
qqemail = MyQQEmail(user['username'], user['vCode'], 'Vove')
if qqemail.sendQQEmail(
        ['529545532@qq.com'],
        '附件',msg='附件测试',
        type='file',filePaths=['../two/t.py','B.txt'],
        fileNames=['test.txt','B.txt']):
    print('Send successful')
else:
    print('Send failed')