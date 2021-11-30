"""
file:           test_L00156282_Q4_File_1.py
created:        29/11/2021 22:24
author:         ciaran mcdevitt
version:        v1.0.0
licensing:      (c) 2021 Ciaran McDevitt, LYIT
                available under the GNU Public License (GPL)
description:
credits:

"""
from unittest import TestCase
from L00156282_Q4.L00156282_Q4_File_1 import PortScanner
import ipaddress

if __name__ == '__main__':
    '''
    Main method of application
    
    Linear programming only presented here demo of lists

    Parameters:
    None    
    '''


class ValidScanParametersPortScanner(TestCase):

    def test_starting_port_valid(self):
        test_port_scanner = PortScanner()
        starting_port = test_port_scanner.starting_port
        self.assertEqual(starting_port, 21)

    def test_finishing_port_valid(self):
        test_port_scanner = PortScanner()
        finishing_port = test_port_scanner.finishing_port
        self.assertEqual(finishing_port, 81)

    def test_ip_address(self):
        test_port_scanner = PortScanner()
        ip_address_value = test_port_scanner.ip_address
        self.assertEqual(ip_address_value, "192.168.178.130")

    def test_ip_address_is_a_valid_ip(self):
        test_port_scanner = PortScanner()
        ip_address_value = test_port_scanner.ip_address
        try:
            ip = ipaddress.ip_address(ip_address_value)
            valid_ip = True
        except ValueError:
            valid_ip = False
        self.assertTrue(valid_ip)

