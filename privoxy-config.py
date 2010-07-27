#!/usr/bin/env python

import sys
from optparse import OptionParser
import string
import re

def main():
    parser = OptionParser()
    parser.add_option('-t', '--type',
            dest='type', default='forward-socks5',
            help='forwarding type. "forward" for http proxy or "forward-socks" for socks5.'\
                    ' "forward-socks" if omit.')
    parser.add_option('-u', '--upstream', 
            dest='upstream', default='127.0.0.1:9050',
            help='the address of upstream in "host:port" format.'\
                    ' "127.0.0.1:9050" if omit.')

    (options, args) = parser.parse_args()

    with open('patterns.txt', 'r') as f:
        p = re.compile('#.*', )
        for line in f:
            line = string.strip(p.sub('', line))
            if (line == ''):
                continue
            print options.type, line, options.upstream, '.'

if __name__ == "__main__":
    main()
