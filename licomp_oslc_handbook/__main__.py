#!/bin/env python3

# SPDX-FileCopyrightText: 2025 Henrik Sandklef
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys

from licomp.interface import Provisioning
from licomp.interface import UseCase
from licomp.main_base import LicompParser

from licomp_oslc_handbook.config import cli_name
from licomp_oslc_handbook.config import description
from licomp_oslc_handbook.config import epilog
from licomp_oslc_handbook.oslc_handbook import LicompOslcHandbook

def main():
    lo = LicompOslcHandbook()
    o_parser = LicompParser(lo,
                            cli_name,
                            description,
                            epilog,
                            UseCase.SNIPPET,
                            Provisioning.BIN_DIST)
    return o_parser.run()


if __name__ == '__main__':
    sys.exit(main())
