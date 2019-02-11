import configparser
from gizmo_email import Email_client

# Init config
Config = configparser.ConfigParser()
Config.read("config")
print(type(Config))

class Main():
    def __init__(self):
        self.Config = configparser.ConfigParser()
        self.Config.read("../config")
        self.name = 'test'
    message_lst = ['test','this is a test message']
    Email_client().notification_message(message_lst)
#    message_lst = ['Test-subject','Test-message']
#    Email_client().notification_message()



if __name__ == "__main__":
    Main()

