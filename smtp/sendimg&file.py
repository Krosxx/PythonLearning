import json

from smtp.myqqemail import MyQQEmail

with open('smtp/user.json') as js:
    jsonStr = js.read()
user = json.loads(jsonStr)
qqemail = MyQQEmail(user['username'], user['vCode'], 'Vove')
msg = '<p>Python 邮件发送测试...</p><p>图片演示：</p><p><img src="cid:image1"><img src="cid:image2"></p>'
if qqemail.sendQQEmail(
        ['529545532@qq.com'],
        '附件&图片',msg,
        type='file',filePaths=['../two/t.py','B.txt'],
        fileNames=['test.txt','B.txt'],
        imagePaths=['image.jpg','image.jpg']):
    print('Send successful')
else:
    print('Send failed')