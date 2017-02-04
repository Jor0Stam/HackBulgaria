import smtplib
from email.mime.text import MIMEText


def main():
    content = 'Use this to recover your pass - {}'.format("Test Work !")
    msg = MIMEText(content)

    msg['Subject'] = 'RecoverPass(NoReply)'
    msg['From'] = "g.a.stemenov@gmail.com"
    msg['To'] = "g.a.stemenov@gmail.com"

    me = "g.a.stemenov@gmail.com"
    you = "g.a.stemenov@gmail.com"

    s = smtplib.SMTP('localhost')
    s.sendmail(me, [you], msg.as_string())
    s.quit()


if __name__ == "__main__":
    main()
