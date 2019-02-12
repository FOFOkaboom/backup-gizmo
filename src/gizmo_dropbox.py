#!/usr/bin/env python
import configparser


class DropboxClient(object):
    """
    This object can push and pull files to Dropbox.
    """
    def __init__(self):
        """"
        Initialise config
        """
        self.Config = configparser.ConfigParser()
        self.Config.read("config")
        self.debug = True

    def push_files(self):
        print('Do stuff')



