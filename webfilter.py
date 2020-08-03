import requests
import sys 
import argparse
import os
import concurrent.futures
import re

SIZE = []
CODE = []

def validate(url):
    pattern = '(.*)\\:\\/\\/'
    if re.match(pattern, url) is None:
        return 'http://'+url

def filter(sub):
    sub = sub.strip('\n')
    isPrint = False
    req = requests.get(validate(sub), stream=True)
    req_code = req.status_code
    req_size = len(req.raw.read())
    if SIZE and CODE:
        if req_size not in SIZE and req_code not in CODE:
            isPrint = True
    elif SIZE and req_size not in SIZE:
        isPrint = True
    elif CODE and req_code not in CODE:
        isPrint = True
    elif not SIZE and not CODE:
        isPrint = True 
    if isPrint:
        print(f'[Code:{req.status_code}, Size: {req_size}]',sub)

def toList(file) :
    with open(file) as subs:
        return subs.readlines()

def args():
    parser = argparse.ArgumentParser(epilog=f'Example: python3 {sys.argv[0]} -s google.txt')
    parser.add_argument('-s', '--subdomains', help='List of subdomains', required=True)
    parser.add_argument('-fs', '--filter-size', help='Filter HTTP response size', default=False, nargs='+', type=int)
    parser.add_argument('-fc', '--filter-code', help='Filter HTTP status codes from response', default=False, nargs='+', type=int)
    parser.add_argument('-t', '--threads', help='Threads of requests', default=10, type=int)
    return parser.parse_args()

def main():
    global SIZE, CODE
    arg = args()
    if not os.path.exists(arg.subdomains):
        print('[ERROR] Please enter a valid path of list of subdomains')
        return
    SIZE = arg.filter_size
    CODE = arg.filter_code
    subdomainList = toList(arg.subdomains)
    with concurrent.futures.ThreadPoolExecutor(max_workers=arg.threads) as executor:
        executor.map(filter, subdomainList)

if __name__ == '__main__':
    main()