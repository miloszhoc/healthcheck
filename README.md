# healthcheck

Check if website is online. When it is down script sends an email.

### Example usage

`python3.8 /healthcheck/main.py -w https://google.com https://facebook.com`   
The example checks if https://google.com and https://facebook.com websites work.

After -w flag provide a list of websites to check separated by spaces.

### Running in crontab

1. Install crontab and git.
2. Run `systemctl enable corn.service` in order to automatically start cron after system reboot.
3. Clone this repository.
4. Create log file using `touch /healthcheck/log.txt` command
5. Install required packages using `pip install -r requirements.txt` command.
6. Into `.profile` file insert environmental variables:
- export EMAIL_HOST=""
- export SOURCE_EMAIL=""
- export EMAIL_PASSWD=""
- export EMAIL_PORT_SSL=""
- export TARGET_EMAIL=""
- export EMAIL_SUBJECT=""
- export EMAIL_MESSAGE=""
7. run `crontab -e` command and in new line
   insert `0 8 * * * . $HOME/.profile; python3.8 /healthcheck/main.py -w https://google.com https://facebook.com >> /healthcheck/log.txt`

### Gmail SMTP

- [Allow access to Google accounts](https://accounts.google.com/b/0/DisplayUnlockCaptcha)
- [Turn off less secure apps](https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-on-for-your-account)
- [Gmail SMTP configuration](https://support.google.com/mail/answer/7126229?hl=en#zippy=%2Cstep-change-smtp-other-settings-in-your-email-client)