import smtplib
import time
import imaplib
import email
import base64
import ast
import quopri

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "boubq20" + ORG_EMAIL
FROM_PWD    = "cs4everlol"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def read_email_from_gmail():
    M = imaplib.IMAP4_SSL(SMTP_SERVER)
    M.login(FROM_EMAIL,FROM_PWD)
    M.select('SMS')
    while True:
        typ, data = M.search(None, 'from', '"google"')
        if len(data) > 1:
            num = data[0].split()[0]
            print(num)
            #for num in data[0].split():
            typ, data = M.fetch(num, '(RFC822)')  # data is being redefined here, that's probably not right
            num = num.decode()  # should this be (num) rather than (num1) ?
            #subject = data[0][1][0].decode("UTF-8")
            data = data[0][1].decode("UTF-8")
            data = quopri.decodestring(data).decode('utf8')
            #data = ast.literal_eval(data)
            subject = data.split("\r\n")[0][9:]
            content = data.split("\r\n")
            text = ""
            for i in range(23,len(content)):
                text=text + content[i]
            print("subject :\n" + subject)
            print("text :\n"+ text)
            M.store(num, '+FLAGS', '\\Deleted')

    M.close()
    M.logout()


read_email_from_gmail()