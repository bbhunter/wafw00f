#!/usr/bin/env python
'''
Copyright (C) 2024, WAFW00F Developers.
See the LICENSE file for copying permission.
'''

NAME = 'NSFocus (NSFocus Global Inc.)'


def is_waf(self):
    if self.matchHeader(('Server', 'NSFocus')):
        return True

    return False
