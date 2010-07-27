#!/usr/bin/env python

import base64
import sys
import os

fn_base64 = 'patterns.base64'
fn_plain = 'patterns.txt'

with open(fn_base64, 'r') as fbase64:
    encoded = fbase64.read()

decoded = base64.b64decode(encoded)

with open(fn_plain, 'w') as fplain:
    fplain.write(decoded)

print 'File "{0}" has been created and ready to be edit'.format(fn_plain)

# edit
editor = os.environ['EDITOR']
if editor == '':
    editor = 'vi'
os.system('{0} {1}'.format(editor, fn_plain))

# encode
with open(fn_plain, 'r') as fplain:
    decoded = fplain.read()

encoded = base64.b64encode(decoded)

with open(fn_base64, 'w') as fbase64:
    fbase64.write(encoded)

print 'File "{0}" has been created and ready to be commit'.format(fn_base64)

