#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime


class PortScanner:

    ip_address = "192.168.178.130"
    # set port scan range here
    starting_port = 21
    finishing_port = 81

    # ports dictionary, key = port number, value = protocol
    ports_dictionary = {
        20: "FTP",  # File Transfer Protocol - Data Transfer
        21: "FTP",  # File Transfer Protocol - Command Control
        22: "SSH",  # Secure Shell
        23: "Telnet",  # Remote login service, unencrypted text messages
        25: "SMTP",  # Simple Mail Transfer Protocol - E-mail Routing
        53: "DNS",  # Domain Name System - service
        80: "HTTP",  # Hypertext Transfer Protocol - used in World Wide Web
        110: "POP3",  # Post Office Protocol - used by e-mail clients to retrieve e-mail from a server
        119: "NNTP",  # Network News Transfer Protocol
        123: "NTP",  # Network Time Protocol
        143: "IMAP",  # Internet Message Access Protocol - Management of Digital Mail
        161: "SNMP",  # Simple Network Management Protocol
        194: "IRC",  # Internet Relay Chat
        443: "HTTPS",  # HTTP Secure - HTTP over TLS/SSL
    }

    def port_scan(self, remote_server):
        """
        run a port scan between a starting and ending range, only if a port is open should the protocol be outputted,
        run a timer on the port scan and output the run time at the end.  Handle a scenario where a port might be open but
        has not value in the ports_dictionary

        :param remote_server: ip address of the remote server the port scan will be run on
        """
        # Clear the screen
        subprocess.call("cls", shell=True)
        remote_server_ip = socket.gethostbyname(remote_server)
        # display scanning message and IP address
        print("-" * 60)
        print("Please wait, scanning remote host", remote_server_ip)
        print("-" * 60)
        # Take a reading of the time the scan started
        scan_start_time = datetime.now()
        try:
            print("Open ports")
            for port in range(self.starting_port, self.finishing_port):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remote_server_ip, port))
                if result == 0:
                    if port in self.ports_dictionary:
                        print(" -{}".format(self.ports_dictionary[port]))
                    else:
                        print(f" -Port {port} is open but has no protocol in the ports dictionary")
                sock.close()
        except KeyboardInterrupt:
            print("You pressed Ctrl+C")
            sys.exit()
        except socket.gaierror:
            print('\nHostname could not be resolved. Exiting')
            sys.exit()
        except socket.error:
            print("\nCouldn't connect to server")
            sys.exit()
        # Take a reading of the time the scan completed
        scan_end_time = datetime.now()
        # Calculates the difference of time, to see how long it took to run the script
        time_taken = scan_end_time - scan_start_time
        # Printing the information to screen
        print('\nScanning Completed in: ', time_taken)


if __name__ == "__main__":
    my_port_scan = PortScanner()
    ip_address = my_port_scan.ip_address

    # if no IP is passed then the user should be asked to enter one
    if ip_address is None or ip_address == "":
        ip_address = input("Enter a remote host to scan: ")

    my_port_scan.port_scan(ip_address)
