#!/bin/env python3

# SPDX-FileCopyrightText: 2025 Henrik Sandklef
#
# SPDX-License-Identifier: GPL-3.0-or-later

from licomp_oslc_handbook.license import license_compatibility
from licomp_reclicense.reclicense import LicompReclicense
lr = LicompReclicense()
from licomp.interface import Licomp
from licomp.interface import Provisioning
from licomp.interface import UseCase

def checker(outbound, inbound):
    compats = license_compatibility(outbound, inbound)
    if compats == []:
        compat = "yes"
    else:
        compat = "no"
    lr_ret = lr.outbound_inbound_compatibility(outbound,
                                               inbound)["compatibility_status"]
    same = (compat==lr_ret)
    return compat

#checker('LGPL-2.1-only', 'LGPL-3.0-only')
#checker('LGPL-2.1-only', 'LGPL-3.0-or-later')
#checker('LGPL-2.1-or-later', 'LGPL-3.0-only')
#checker('LGPL-2.1-or-later', 'LGPL-3.0-or-later')
checker('AGPL-3.0-only', 'AGPL-3.0-or-later')

