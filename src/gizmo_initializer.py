#!/usr/bin/env python
import configparser
import os

class Initializer(object):
    """
    This class can facilitate configuration of server and clients.
    """

    def __init__(self):
        """"
        Initialise config
        """
        self.Config = configparser.ConfigParser()
        self.Config.read("config")
        #TODO Modify debug value, is str should be boolean.
        self.debug = True

    def setup_sshd(self, sudopassword):
        """
        Installs and configures the SSHD server
        :return: void
        """
        sudo_pw = self.Config.get('auth', 'password')  # UNSAFE REMOVE AFTER DEBUG
        #sudo_pw = sudopassword

        # Update apt repository
        command = 'apt update -y'
        os.system('echo %s| sudo -S %s' % (sudo_pw, command))

        # Install ssh package
        command = 'apt install ssh -y'
        try:
            os.system('echo %s| sudo -S %s' % (sudo_pw, command))
        except OSError as e:
            print('An error occured during "$ sudo apt install ssh -y" [{}]').format(e)

        # Configure SSHD
        # TODO Configure SSHD
        # TODO autostart SSH service on boot
        # TODO restart SSH service
        # TODO Host based firewall activation/verification?

        # pkg_name = "ssh"
        #
        # cache = apt.cache.Cache()
        # cache.update()
        # cache.open()
        #
        # pkg = cache[pkg_name]
        # if pkg.is_installed:
        #     print("{} already installed").format(pkg_name=pkg_name)
        # else:
        #     pkg.mark_install()
        # try:
        #     cache.commit()
        # except OSError as e:
        #     print('During the SSH installation the SSH installation failed [{}]').format(e)

        # Configureren van SSHD
        pass

    def setup_ssh(self):
        pass

    def setup_sftpd(self):
        pass

    def setup_sftp(self):
        pass


