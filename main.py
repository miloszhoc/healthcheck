from config import EMAIL_HOST, EMAIL_PORT_SSL, SOURCE_EMAIL, EMAIL_PASSWD, TARGET_EMAIL
from mail import MailSender
import requests

if __name__ == '__main__':
    main_page = requests.get('http://miloszhoc.cloud')
    apache = requests.get('http://miloszhoc.cloud:81')
    try:
        assert main_page.status_code == 200
        assert apache.status_code != 200
    except AssertionError:
        mail = MailSender(EMAIL_HOST, EMAIL_PORT_SSL, SOURCE_EMAIL, EMAIL_PASSWD, TARGET_EMAIL)
        mail.send_email('Your website is down!')
        print('message sent')
