#!/usr/bin/env Python3

import requests
import optparse
from colorama import Fore


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option('-l', '--list', dest='list', help="List of URLs")
    parser.add_option('-v', '--verbose', help="Enables verbosity", action="store_true")
    (option, arguments) = parser.parse_args()
    if not option.list:
        print("[-] Please specify a list of URLs.")
    return option

options = get_arguments()


urllist = [line.rstrip('\n') for line in open(options.list)]


if options.verbose:
    def verbose():
        for url in urllist:
            response = requests.get('http://' + url)
            if response.status_code == 404:
                print("http://" + url + "\t" + Fore.RED + "Vulnerable")
                print(Fore.RESET)
            else:
                print("http://" + url + "\t" + Fore.BLUE + "Not Vulnerable")
                print(Fore.RESET)
    verbose()
else:
    def notverbose():
        for url in urllist:
            response = requests.get('http://' + url)
            if response.status_code == 404:
                print("http://" + url + "\t" + Fore.RED + "Vulnerable")
                print(Fore.RESET)
    notverbose()
