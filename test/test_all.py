#!/usr/bin/env python
# coding: utf-8

import md
import os
from pykit import utfyaml
from pykit import fsutil

this_base = os.path.dirname(__file__)
case_dir = os.path.join(this_base, 'cases')

def test_all():

    cases = os.listdir(case_dir)

    for fn in cases:
        case_path = os.path.join(case_dir, fn)
        cont = fsutil.read_file(case_path)
        case = utfyaml.load(cont)

        res = md.MD(case['text']).tree

        print '     res:', res
        print 'expected:', case['yaml']

        assert case['yaml'] == res

