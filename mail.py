from smtplib import SMTP


class MailSender():

    def __init__(self, host, port, source_email, passwd, target_email) -> None:
        self.__host = host
        self.__port = port
        self.__source_email = source_email
        self.__passwd = passwd
        self.__target_email = target_email
        self.__smtp: SMTP = None

    def __quit(self):
        self.__smtp.quit()

    def __start_connection(self):
        self.__smtp = SMTP(self.__host, int(self.__port))
        self.__smtp.ehlo()
        self.__smtp.starttls()
        self.__smtp.login(self.__source_email, self.__passwd)

    def send_email(self, message):
        content = "\r\n".join([
            "From: {}".format(self.__source_email),
            "To: {}".format(self.__target_email),
            "Subject: Website is down!",
            "",
            "{}".format(message)
        ])
        self.__start_connection()
        self.__smtp.sendmail(self.__source_email, [self.__target_email, ], content)
        self.__quit()


