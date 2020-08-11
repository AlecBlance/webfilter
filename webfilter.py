import requests
import sys 
import argparse
import os
from concurrent.futures import ThreadPoolExecutor
import re

def validate(url):
    pattern = '(.*)\\:\\/\\/'
    if re.match(pattern, url) is None:
        url = 'http://'+url
    return url

def filter(sub, size, code, verbose, clean):
    sub = sub.strip('\n')
    if verbose:
        print(f'Getting {sub}')
    req = requests.get(validate(sub), stream=True)
    req_code = req.status_code
    req_size = len(req.raw.read())
    if size and code and req_size in size and req_code in code: return
    if size and req_size in size: return 
    if code and req_code in code: return
    result = ''
    if not clean:
        result = f'[Code:{req.status_code}, Size: {req_size}] '
    print(result + sub)

def toList(file) :
    with open(file) as subs:
        return subs.readlines()

def args():
    parser = argparse.ArgumentParser(epilog=f'Example: python3 {sys.argv[0]} -s google.txt')
    parser.add_argument('-s', '--subdomains', help='List of subdomains', required=True)
    parser.add_argument('-fs', '--filter-size', help='Filter HTTP response size', default=False, nargs='+', type=int)
    parser.add_argument('-fc', '--filter-code', help='Filter HTTP status codes from response', default=False, nargs='+', type=int)
    parser.add_argument('-t', '--threads', help='Threads of requests', default=10, type=int)
    parser.add_argument('-v', '--verbose', help='Show the process', action='store_true')
    parser.add_argument('-c', '--clean', help='No code and size in output', action='store_true')
    return parser.parse_args()

def main():
    arg = args()
    if not os.path.exists(arg.subdomains):
        print('[ERROR] Please enter a valid path of list of subdomains')
        return
    size = arg.filter_size
    code = arg.filter_code
    verbose = arg.verbose
    clean = arg.clean
    subdomainList = toList(arg.subdomains)
    with ThreadPoolExecutor(max_workers=arg.threads) as executor:
        for sub in subdomainList: 
            executor.submit(filter, sub, size, code, verbose, clean)

if __name__ == '__main__':
    main()