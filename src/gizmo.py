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


    # The email client
    #message_lst = ['test', 'this is a test message']
    #EmailClient().notification_message(message_lst)

    # The SSHD initialiser
    #Initializer().setup_sshd(sudopassword=input("Input your sudo password: "))   # Use this in prod
    Initializer().setup_sshd(sudopassword='thisisnotmypassword')  # Unsafe, do not use in prod


if __name__ == "__main__":
    Main()

