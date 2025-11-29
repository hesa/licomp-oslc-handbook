#!/bin/env python3

# SPDX-FileCopyrightText: 2025 Henrik Sandklef
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json

from matrix.license import read_licenses
from matrix.license import license_compatibility

licenses = read_licenses()
license_matrix = {}
for outbound in licenses:
    license_matrix[outbound] = {}
    for inbound in licenses:
        compats = license_compatibility(outbound, inbound)
        if compats == []:
            compat = "yes"
        else:
            compat = "no"
        license_matrix[outbound][inbound] = compat



print(json.dumps({'meta': {}, 'licenses': license_matrix}))
