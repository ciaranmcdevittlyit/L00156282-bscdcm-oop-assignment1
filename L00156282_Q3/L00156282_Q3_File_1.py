#!/usr/bin/env python

import paramiko
from datetime import datetime
import credentials as creds

ip_address = "192.168.178.130"


def ssh_connection(ip, datetime_string):
    """
    ssh connection function accepts an IP address and a datetime_string and connects over SSH to create a
    connection.txt file containing the text "Connection Made" and also containing the time of the creation/overwriting
    USERNAME & PASSWORD are imported from an external 'credentials.py' file

    :param ip: (str) - IP address
    :param datetime_string: (str) - date & time string

    """
    try:
        # please add username and password on the credentials.py file to run
        username = creds.USERNAME
        password = creds.PASSWORD
        print("Establishing a connection...")
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        session.invoke_shell()
        # using the ssh connection create a new file named 'connection.txt' with the current date included
        session.exec_command(f"echo Connection Made - {datetime_string} > connection.txt\n")
        session.close()
    except paramiko.AuthenticationException:
        print("Authentication Error")


def get_datetime_string():
    """
    Function to retrieve the current date and time in a neatly formatted layout

    :return: (str) datetime - formatted date & time

    """
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")


def main():
    """
    main method calls the get_datetime_string function and passes the datetime_string and the IP address to the
    ssh_connection function

    """
    datetime_string = get_datetime_string()
    ssh_connection(ip_address, datetime_string)


if __name__ == "__main__":
    main()
