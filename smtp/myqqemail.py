import json
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# type=plain 文本格式 默认
# type=html  网页格式
# type=image 带本地图片的html
# type=file  带附件和图片
# 带图片时，msg为html格式
# 示例:
'''
msg ='<p>Python 邮件发送测试...</p><p>图片演示：</p><p><img src="cid:image1"></p>'
'''


class MyQQEmail:
    __mail_user = ''  # 登陆邮箱
    __mail_pass = ''  # 邮箱授权码
    __senderName = ''  # 发件人

    def __init__(self, user, pas, name) -> None:
        self.__mail_user = user
        self.__mail_pass = pas
        self.__senderName = name

    def sendQQEmail(self, receiver, title, msg, type='plain', filePaths=[], fileNames=[], imagePaths=None):
        if receiver == '':
            return False

        mail_host = 'smtp.qq.com'
        mail_port = 465  # qq smtp端口465
        sender = self.__mail_user

        type = type.lower()
        if type.__eq__('plain') or type.__eq__('html'):
            message = MIMEText(msg, type, 'utf-8')
        elif type.__eq__('file') or type.__eq__('image'):
            message = MIMEMultipart()
        else:
            return False

        try:
            message['From'] = Header(self.__senderName, 'utf-8')
            message['To'] = Header(str(receiver), 'utf-8')
            subject = title
            message['Subject'] = Header(subject, 'utf-8')

            if type.__eq__('file') or type.__eq__('image'):
                # 邮件正文内容
                if imagePaths is not None:
                    message.attach(MIMEText(msg, 'html', 'utf-8'))
                    # 添加图片
                    if imagePaths is not None:
                        for index, imagePath in enumerate(imagePaths, 1):
                            # 指定图片为当前目录
                            fp = open(imagePath, 'rb')
                            msgImage = MIMEImage(fp.read())
                            fp.close()

                            # 定义图片 ID，在 HTML 文本中引用
                            msgImage.add_header('Content-ID', '<image' + str(index) + '>')
                            message.attach(msgImage)
                else:
                    message.attach(MIMEText(msg, 'plain', 'utf-8'))
                # 构造附件，传送filePath制定文件
                for filePath, fileName in zip(filePaths, fileNames):
                    att = MIMEText(open(filePath, 'rb').read(), 'base64', 'utf-8')
                    att["Content-Type"] = 'application/octet-stream'
                    # 邮件中显示文件名
                    att["Content-Disposition"] = 'attachment; filename="' + fileName + '"'
                    message.attach(att)

        except Exception as e:
            print(e)
            return False
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
            smtpObj.login(self.__mail_user, self.__mail_pass)
            smtpObj.sendmail(sender, receiver, message.as_string())
            smtpObj.quit()
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    with open('smtp/user.json') as js:
        jsonStr = js.read()
    user = json.loads(jsonStr)

    qq = MyQQEmail(user['username'], user['vCode'], 'Vove')
    qq.sendQQEmail(['529545532@qq.com'], "标题", '内容')
