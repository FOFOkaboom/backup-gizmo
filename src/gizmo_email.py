#!/usr/bin/env python
import smtplib, ssl, configparser

class Email_client():
    """
    This object can email notifications and warnings.
    """
    def __init__(self):
        self.Config = configparser.ConfigParser()
        self.Config.read("config")

    def notification_message(self, notification_lst):
        self_to_lst = [self.Config.get('email','notify_address')]
        self.subject_str = notification_lst[0]
        self.body_str = notification_lst[1]
        self.signature = self.Config.get('email','signature')
        self.email_str = 'Subject: {}\n\n{}\n\n- {}'.format(self.subject_str, self.body_str, self.signature)
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.Config.get('email','mailserver_ip'),self.Config.get('email','mailserver_port'), context=context) as server:
                if __debug__ : print('config passed')
                server.ehlo()
                if __debug__ : print('server ehlo passed') 
                server.login(self.Config.get('email','username'), self.Config.get('email','password'))
                if __debug__ : print('login passed')
                server.sendmail(self.Config.get('email','username'), [self.Config.get('email','notify_address')], self.email_str)
                if __debug__ : print('mail send passed')
                server.close()
                if __debug__ : print('Email sent!')
        except:
            print('Something went wrong...')
