#!/usr/bin/env python
# coding: utf-8

import re

class MD(object):
    def __init__(self, text):
        self.indent = 0
        self.text = text
        self.lines = text.split('\n')

        self.rules = [
                (r'#', _header), 
                (r'```', _code_block),
                (r'-', _list_item),
                (r'\d\.', _list_item),
        ]

        self.tree = []

        self.parse_lines(self.lines)

    def parse_lines(self, lines, indent=0):

        for line in lines:
            line = line.rstrip()

            curr_indent = self.get_indent(line)

            text = line[curr_indent:]

            if text.startswith('#'):
                self.tree.append(self._header(text))
                continue

            self.tree.append(self._paragraph(text))

    def block_iter(self, lines, indent=0):

        for line in lines:
            line = line.rstrip()

            curr_indent = self.get_indent(line)

            if curr_indent < indent:
                break

            text = line[curr_indent:]

            for regex, handler = 

            if text.startswith('#'):
                self.tree.append(self._header(text))
                continue

            self.tree.append(self._paragraph(text))


    def get_indent(self, line):
        spaces = re.match(r'\s*', line).group(0)
        return len(spaces)


    def _header(self, text):
        sharps = re.match(r'##*', text).group(0)
        lvl = len(sharps)

        return { 'type': 'header',
                 'level': lvl,
                 'text': text[lvl:].strip(),
        }

    def _paragraph(self, text):
        return {
                'type': 'paragraph', 
                'text': text,
        }
