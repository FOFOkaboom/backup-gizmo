#!/usr/bin/env python
import smtplib
import ssl
import configparser


class EmailClient(object):
    """
    This object can email notifications and warnings.
    """
    def __init__(self):
        """"
        Initialise config
        """
        self.Config = configparser.ConfigParser()
        self.Config.read("config")
        self.debug = True

    def notification_message(self, notification_lst):
        """
        :param notification_lst: List item containing two string items, subject and message for mailing
        :return: none
        """
        assert len(notification_lst) == 2, 'The EmailClient.notification_message list is broken'
        self.subject_str = notification_lst[0]
        self.body_str = notification_lst[1]
        self.signature = self.Config.get('email', 'signature')
        self.email_str = 'Subject: {}\n\n{}\n\n- {}'.format(self.subject_str, self.body_str, self.signature)

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(self.Config.get('email', 'mailserver_ip'), self.Config.get('email', 'mailserver_port'), context=context) as server:
                if self.debug is True:
                    print('configuring the email conenction completed')
                server.ehlo()
                if self.debug is True:
                    print('server ehlo passed')
                server.login(self.Config.get('email', 'username'), self.Config.get('email', 'password'))
                if self.debug is True:
                    print('login passed')
                server.sendmail(self.Config.get('email', 'username'), [self.Config.get('email', 'notify_address')], self.email_str)
                if self.debug is True:
                    print('mail send passed')
                server.close()
                if self.debug is True:
                    print('Email sent!')
        except:
            print('Something went wrong...')
