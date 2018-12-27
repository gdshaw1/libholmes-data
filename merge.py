#!/usr/bin/python3

# This file is part of libholmes.
# Copyright 2018 Graham Shaw.
# Distribution and modification are permitted within the terms of the
# GNU General Public License (version 3 or any later version).

import sys
import os
import re
import json

module = sys.argv[1]

ids = []
for filename in os.listdir(os.path.join('src', module)):
    m = re.match('([^-]+)-([0-9]+)[.]json', filename)
    if m and m.group(1) == module:
        ids.append(m.group(2))

signatures = []
for id in sorted(ids):
    infilename = '%s-%s.json' % (module, id)
    inpathname = os.path.join('src', module, infilename)
    with open(inpathname, 'r') as infile:
        signature = json.load(infile)
        signature['_id'] = "%s-%s" % (module, id)
        signatures.append(signature);

if not os.path.exists('target'):
    os.mkdir('target')
outfilename = '%s.json' % module
outpathname = os.path.join('target', outfilename)
with open(outpathname, 'w') as outfile:
    json.dump(signatures, outfile)
