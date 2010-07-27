#!/usr/bin/env python

import base64
import sys
import os

fn_base64 = 'patterns.base64'
fn_plain = 'patterns.txt'

def decode():
    with open(fn_base64, 'r') as fbase64:
        with open(fn_plain, 'w') as fplain:
            base64.decode(fbase64, fplain)
    print 'File "{0}" has been created and ready to be edit'.format(fn_plain)

def edit():
    editor = os.environ['EDITOR']
    if editor == '':
        editor = 'vi'
    os.system('{0} {1}'.format(editor, fn_plain))

def encode():
    with open(fn_plain, 'r') as fplain:
        with open(fn_base64, 'w') as fbase64:
            base64.encode(fplain, fbase64)
    print 'File "{0}" has been created and ready to be commit'.format(fn_base64)

def main():
    decode()
    edit()
    encode()

if __name__ == "__main__":
    main()
