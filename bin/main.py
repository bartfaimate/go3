

import argparse
from pathlib import Path
import os
import string
from typing import OrderedDict

HOME = '/home/mate/'

def parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-s', '--search', dest='search', required=True,
                        help='Pattern for search')
    parser.add_argument('-b', '--base',  dest='base', required=False,
                        help='Base path')
    return parser

def main():
    args = parser().parse_args()
    results = OrderedDict()
    max_results = 10
    index = 0
    home = Path(args.base) if args.base else Path().home()
    
    ignore_case = False
    print(args)

    search = args.search.lower() if ignore_case else args.search
    for path in home.glob('**/*'):
        name = path.name.lower() if ignore_case else path.name
        if path.is_dir() and name.endswith(search):
            results[string.ascii_lowercase[index]] = path.as_posix()
            index += 1
            if len(results) >= max_results:
                break
    
    if len(results) < 1:
        print(f'No such directory for <{args.search}>')
        return -1
    for index, elem in results.items():
        print(index, '--', elem)
    keys = list(results.keys())
    wrong_key = True 
    while wrong_key:
        choice = input(f'Please enter a key between \'{keys[0]}\' and \'{keys[-1]}\'\n')
        try:
            print(f'Entering directory {results[choice]} ...')
            wrong_key = False
        except KeyError :
            print(f'Wrong key. Please chose acorrect one between {keys[0]} and {keys[-1]}')
            wrong_key = True



if __name__ == '__main__':
    main()
    