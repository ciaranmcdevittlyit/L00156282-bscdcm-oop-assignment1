#!/usr/bin/env python

import paramiko
import time
import re
import credentials as creds


# Open SSH connection to the device
def ssh_connection(ip, command):
    """
    ssh connection function accepts an IP address and a command and connects over SSH to run that command on the
    remote server, USERNAME & PASSWORD are imported from an external 'credentials.py' file

    :param command: (str) command to run on the remote server
    :param ip: (str) - IP address of the remote server

    """
    # placed in a try/except to handle an authentication error
    try:
        # imported credentials
        username = creds.USERNAME
        password = creds.PASSWORD
        print(f"Establishing a connection... \n running: {command}")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        connection.send(command) 
        time.sleep(1)
        vm_output = connection.recv(65535)
        # print(vm_output)
        if re.search(b"% Invalid input", vm_output):
            print("There was an error on vm {}".format(ip))
        else:
            print("Commands successfully executed on {}\n\n".format(ip))
        # close the session at the end
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


def main():
    """
    main method to run the ssh_connection function on a list of commands
    :return:
    """
    # ip address of remote server
    ip_address = "192.168.178.130"

    # commands to run
    dir_contents = "ls > dir_contents.txt"
    apt_update_and_upgrade = "sudo apt-get update && sudo apt-get upgrade -y"
    install_curl = "sudo apt-get install curl -y"
    create_labs_folder = "mkdir Labs"
    create_labs_subfolders = "cd Labs;mkdir Lab1 Lab2;cd ~/"
    get_last_accessed_files = "ls -la --time=atime > accessTime.txt"

    # create a list of the above commands,so they can be run in a loop
    run_commands = [dir_contents, apt_update_and_upgrade, install_curl, create_labs_folder,
                    create_labs_subfolders, get_last_accessed_files]

    for command in run_commands:
        # append a new line to the end of any command that gets run to ensure they run without any problems
        command = f"{command}\n"
        ssh_connection(ip_address, command) 


if __name__ == "__main__":
    main()
