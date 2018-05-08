import smtplib
from email.mime.text import MIMEText

smtp_server = 'smtp.qq.com'


def send_mail(from_addr, to_addrs, msg, passwd):
    """

    :param from_addr:发送方
    :param to_addrs:接受方（list类型）
    :param msg:正文
    :param passwd:邮箱密码（授权码）
    :return:
    """
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, passwd)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()


if __name__ == '__main__':
    from_addr = 'xxx@qq.com'
    passwd = 'xxx'
    to_addrs = ['xxx@qq.com']
    msg = MIMEText('main content ...', 'plain', 'utf8')
    send_mail(from_addr, to_addrs, msg, passwd)
