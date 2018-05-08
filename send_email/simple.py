import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf8').encode(), addr))


from_addr = 'xxx@qq.com'
passwd = 'xxx'
to_addrs = ['xxx@gmail.com']
smtp_server = 'smtp.qq.com'

msg = MIMEMultipart()
msg['From'] = _format_addr(f'Jasonqiao36 <{from_addr}>')
msg['To'] = _format_addr(f'管理员 <{to_addrs}>')
msg['Subject'] = Header('来自Jason的问候..', 'utf8').encode()
msg.attach(MIMEText('<html><body><h1>Hello !</h1>' +
                    '<p>send by<a href="http://www.python.org"> Python</a>...</p>' +
                    '</body></html>', 'html', 'utf8'))

with open('device.xlsx', 'rb') as f:
    mime = MIMEBase('device_list.xlsx', 'xlsx', filename='device.xlsx')
    mime.add_header('Content-Disposition', 'attachment', filename='device.xlsx')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, passwd)
server.sendmail(from_addr, to_addrs, msg.as_string())
server.quit()
