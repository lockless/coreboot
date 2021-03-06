#!/usr/bin/env python2
#
# Copyright (C) 2013 Google Inc.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

"""
This utility computes and fills Exynos ROM checksum (for BL1 or BL2).
(Algorithm from U-Boot: tools/mkexynosspl.c)

Input: IN OUT

Output:

  Checksum header added to IN and written to OUT.
  Header: uint32_t size, checksum, reserved[2].
"""

import struct
import sys

def main(argv):
  if len(argv) != 3:
    exit('usage: %s IN OUT' % argv[0])

  in_name, out_name = argv[1:3]
  header_format = "<IIII"
  with open(in_name, "rb") as in_file, open(out_name, "wb") as out_file:
    data = in_file.read()
    header = struct.pack(header_format,
                         struct.calcsize(header_format) + len(data),
                         sum(map(ord, data)),
                         0, 0)
    out_file.write(header + data)


if __name__ == '__main__':
  main(sys.argv)
