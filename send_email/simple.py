import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf8').encode(), addr))


from_addr = 'xxx@qq.com'
passwd = 'xxx'
to_addrs = ['xxx@gmail.com']
smtp_server = 'smtp.qq.com'

msg = MIMEText('hello, send by python ...', 'plain', 'utf8')
msg['From'] = _format_addr(f'Jasonqiao36 <{from_addr}>')
msg['To'] = _format_addr(f'管理员 <{to_addrs}>')
msg['Subject'] = Header('来自Jason的问候..', 'utf8').encode()

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, passwd)
server.sendmail(from_addr, to_addrs, msg.as_string())
server.quit()
