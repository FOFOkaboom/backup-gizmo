import configparser
from gizmo_email import EmailClient
from gizmo_dropbox import DropboxClient
from gizmo_initializer import Initializer


class Main(object):
    """
    Main class
    """
    def __init__(self):
        """
        Init config
        """
        self.Config = configparser.ConfigParser()
        self.Config.read("config")
        self.debug = self.Config.get('options', 'debug')
        #TODO write a config verification function
        #TODO write a logger class


    # The email client
    #message_lst = ['test', 'this is a test message']
    #EmailClient().notification_message(message_lst)

    # The SSHD initializer
    #Initializer().setup_sshd()

    # The SSHD configuration
    #Initializer().config_sshd()

if __name__ == "__main__":
    Main()

