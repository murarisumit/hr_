#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2013 Gil Gonçalves
# Copyright (c) 2014 Euan Goddard
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#I've used their work.

import math
import os
import sys
import getopt


def hr(symbol, name=""):
    symbol = symbol or '='
    cols = _get_terminal_size()[0]
    num_of_sym = (cols-len(name)-4)/2  # leave size of "2 space" on either side of text

    if num_of_sym > 4:
        print symbol*num_of_sym,
    else:
        print symbol*cols

    print "", name,

    if num_of_sym > 4:
        print symbol*num_of_sym,
    else:
        print '\n', symbol*cols


def cli():
    argv = sys.argv[1:]
    name = ""
    symbol = ""
    try:
        opts, args = getopt.getopt(argv, "s:n:")
    except getopt.GetoptError, e:
        print e
        _error_state()

    for opt, arg in opts:
        if opt == '-n':
            name = arg
        elif opt == '-s':
            symbol = arg
    hr(symbol, name)


def _error_state():
    print 'Error: provide valid input !'
    print 'Usage: hr -n "Task Name"'
    sys.exit(2)


def _get_terminal_size():
    env = os.environ

    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct
            cr = \
            struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
        except:
            return
        return cr

    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)

    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass

    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

    return int(cr[1]), int(cr[0])


if __name__ == '__main__':
    cli()
