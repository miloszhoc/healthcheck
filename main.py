from config import EMAIL_HOST, EMAIL_PORT_SSL, SOURCE_EMAIL, EMAIL_PASSWD, TARGET_EMAIL, EMAIL_SUBJECT, EMAIL_MESSAGE
from mail import MailSender
import requests
import argparse
import datetime

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='main',
                                     description="Health check")
    parser.add_argument('-w', help='Names of the websites to check', nargs='*')
    args = parser.parse_args()
    try:
        for website in args.w:
            assert requests.get(website).status_code == 200
        print('Everything works fine! (' + datetime.datetime.now().__str__() + ')')
    except (AssertionError, requests.exceptions.ConnectionError):
        mail = MailSender(EMAIL_HOST, EMAIL_PORT_SSL, SOURCE_EMAIL, EMAIL_PASSWD, TARGET_EMAIL)
        mail.send_email(EMAIL_SUBJECT, '{} \n'.format(website) + EMAIL_MESSAGE)
        print('Message sent (' + datetime.datetime.now().__str__() + ')')
