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
    Main method of unit tests for BScDCM OOP Assignment1   
    '''


class ValidScanParametersPortScanner(TestCase):
    """
    Testing class for PortScanner class in Question 4
    """

    def test_starting_port_valid(self):
        """
        Test should fail if the starting port is not what is expected
        """
        test_port_scanner = PortScanner()
        starting_port = test_port_scanner.starting_port
        # lower range limit from the program is the same as the hardcoded value
        self.assertEqual(starting_port, 21)

    def test_finishing_port_valid(self):
        """
        Test should fail if the finishing port is not what is expected
        """
        test_port_scanner = PortScanner()
        finishing_port = test_port_scanner.finishing_port
        # upper range limit from the program is the same as what is hardcoded below
        self.assertEqual(finishing_port, 81)

    def test_ip_address(self):
        """
        Test should fail if the default IP address is not used.
        """
        test_port_scanner = PortScanner()
        ip_address_value = test_port_scanner.ip_address
        # assert that the IP address value in PortScanner is a match for the hardcoded value below
        self.assertEqual(ip_address_value, "192.168.178.130")

    def test_ip_address_is_a_valid_ip(self):
        """
        Test should fail if the IP address is not valid
        """
        test_port_scanner = PortScanner()
        ip_address_value = test_port_scanner.ip_address
        try:
            # attempting to assign the ip_address_value from the PortScanner class to validated_ip using the
            # ipaddress module, this is done within a try/except as it will crash if the IP is not valid

            validated_ip = ipaddress.ip_address(ip_address_value)

            # if the code gets this far then the IP address must be valid and can be set to True
            valid_ip = True
        except ValueError:
            # if this code is reached then it is a fair assumption that the IP was not valid
            valid_ip = False
        # assert that valid_ip is True for a passing test
        self.assertTrue(valid_ip)

