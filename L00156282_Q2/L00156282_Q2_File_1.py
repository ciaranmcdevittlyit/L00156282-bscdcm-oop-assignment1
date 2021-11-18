#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import re


def format_url(url):
    """
    Using regex - confirm that the url has either http:// or https:// protocol and prepend http:// if not

    :param url:
    :return: url (formatted)
    """
    if not re.match('(?:http|https)://', url):
        return 'http://{}'.format(url)
    return url


def get_all_headers_on_the_default_page(soup):
    """
    assignment_2_1
        This method will extract all the headers from the Apache Server default page running on the remote server
        at the IP address given in the main method

    :param soup: beautiful soup page scrape contents
    """
    # print(type(soup))
    print("\n" + "-"*60)
    print("Assignment Q2.1 - (Headers)\n")
    default_header = soup.find_all(class_="page_header")
    section_headers = soup.find_all(class_="section_header")
    headers = default_header + section_headers
    for header in headers:
        output = header.getText()
        print(output.strip())


def count_occurrences_of_search_term(soup, search_for):
    """
    assignment_2_2
        This method will count the number of occurrences of a given search term on the Apache Server default
        page running on the remote server at the IP address given in the main method

    :param search_for: (str) string to search the scrape for matches of
    :param soup: beautiful soup page scrape contents
    """
    print("\n" + "-"*60)
    print("Assignment Q2.2 - (Number of apaches on the default page)\n")
    all_text = soup.get_text()
    all_text_lower = all_text.lower() 
    num_of_apaches = all_text_lower.count(search_for.lower())
    print(f"There are {str(num_of_apaches)} occurrences of: {search_for.lower()} on the default page")


def get_all_id_tags(soup):
    """
    assignment_2_3
        This method will output all the tags with an 'ID' on the Apache Server default page running on the remote
        server at the IP address given in the main method

    :param soup: beautiful soup page scrape contents
    """
    print("\n" + "-"*60)
    print("Assignment Q2.3 - (All tags with an id)\n")
    id_tags = soup.find_all(id=True)
    for counter, id_tag in enumerate(id_tags):
        string_counter = str(counter + 1)
        value_to_pass = f"#{string_counter}: {id_tag}"
        print(value_to_pass)
    
    print("\n")


def main():
    """
    main method
        use a hardcoded url or accept a user inputted url and then run the three beautiful soup assignment methods
    """
    # url = None
    url = "http://192.168.178.130"
    if url is None or url == "":
        url = input("Please pass in a valid url...\n")
        url = format_url(url)
    homepage = requests.get(url)
    soup = BeautifulSoup(homepage.content, "html.parser")

    # assignment_2_1
    get_all_headers_on_the_default_page(soup)

    # assignment_2_2
    search_term = "apache"
    count_occurrences_of_search_term(soup, search_term)

    # assignment_2_3
    get_all_id_tags(soup)


if __name__ == "__main__":
    main()


