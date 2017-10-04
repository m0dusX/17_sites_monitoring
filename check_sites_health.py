import sys
import argparse
import datetime
import requests
import whois
from whois.parser import PywhoisError
from dateutil.relativedelta import relativedelta


def load_urls4check(path):
    with open(path, 'r', encoding="UTF-8") as site_list:
        return site_list.read().splitlines()


def is_server_respond_with_200(url):
    try:
        if requests.get(url).ok:
            return True
        else:
            return False
    except requests.ConnectionError:
        return False


def get_domain_expiration_date(domain_name):
    expiration_date = whois.whois(domain_name).expiration_date
    # Check if expiration_date function returns list. If true, actual exp.
    # date will be second element in it.
    if not isinstance(expiration_date, list):
        return expiration_date
    else:
        return expiration_date[1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='sites health checker')
    parser.add_argument(
        'path_to_txt', help='path to txt file with sites')
    args = parser.parse_args()
    site_list = args.path_to_txt
    for idx, site in enumerate(load_urls4check(site_list), 1):
        print("{}) {}".format(idx, site))
        if is_server_respond_with_200(site):
            print("Status: OK (ONLINE)")
        else:
            print("Status: OFFLINE")
        minimum_date = (datetime.datetime.now() + relativedelta(months=+1))
        try:
            expiration_date = get_domain_expiration_date(site)
        except PywhoisError:
            print("Domain name was not found in registry\n")
            continue
        if expiration_date > minimum_date:
            print("Domain name is paid for at least 1 month ahead\n")
        else:
            print("Caution! Domain name will expire less in 1 month\n")
    sys.exit()
