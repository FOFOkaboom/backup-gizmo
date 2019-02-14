#!/usr/bin/env python
import configparser
import os
import time

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
        self.ssh_port = self.Config.get('sshd', 'port')
        self.ssh_interface = self.Config.get('sshd', 'interface')
        #TODO Remove sudo_pw line below
        self.sudo_pw = self.Config.get('auth', 'password')  # UNSAFE REPLACE AFTER DEBUG WITH LINE BELOW
        # self.sudo_pw = input("Input sudo password: ")

    def config_sshd(self):
        # Configure SSHD
        # First check if a non default ssh_config file is used (based on multiple references of ListenAddress)
        try:
            with open("/etc/ssh/sshd_config", "r") as old_sshd_file:
                if "\nListenAddress" in old_sshd_file.read():
                    print("A non default sshd config file is found, a backup is saved to /etc/ssh/sshd_config.backup")
                    command = "echo '{}' | sudo tee /etc/ssh/sshd_config.backup > /dev/null 2>&1".format(old_sshd_file)
                    os.system('echo %s| sudo -S %s' % (self.sudo_pw, command))
        except FileNotFoundError as e:
            print(e)
            pass

        # Copy SSHD config
        try:
            with open('sshd_config', 'r') as new_sshd_file:
                # Retrieve the sshd config settings
                # Store the config file with sudo permissions and write stdout to /dev/null
                command = "echo '{}' | sudo tee /etc/ssh/sshd_config > /dev/null 2>&1".format(
                    new_sshd_file.read().format(self.ssh_port, self.ssh_interface))
                os.system('echo %s| sudo -S %s' % (self.sudo_pw, command))
        except FileNotFoundError as e:
            print(e)

    def setup_sshd(self):
        """
        Installs and configures the SSHD server.
        :return: void
        """
        # Update apt repository
        command = 'apt update -y > /dev/null 2>&1'
        if self.debug is True:
            print('Executing apt update -y ')
        try:
            os.system('echo %s| sudo -S %s' % (self.sudo_pw, command))
        except:
            print("An error occured during 'apt update -u'")

        # Install ssh package
        command = 'apt install ssh -y > /dev/null 2>&1'
        if self.debug is True:
            print('Executing apt install ssh -y')
        try:
            os.system('echo %s| sudo -S %s' % (self.sudo_pw, command))
        except:
            print("An error occured during 'apt install ssh -y' while installing ssh")

        # Configure sshd using the config
        self.config_sshd()

         # Reload sshd config
        time.sleep(1)
        try:
            command = "service ssh restart > /dev/null 2>&1"
            os.system('echo %s| sudo -S %s' % (self.sudo_pw, command))
            print('SSHD_installed and configured successfully, SSHD listening on port {}'.format(self.ssh_port))
        except:
            print('An error occured during ssh "sudo service ssh reload" while installing ssh')


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


