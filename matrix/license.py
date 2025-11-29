# SPDX-FileCopyrightText: 2025 Henrik Sandklef
#
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import yaml
import os

from conditions import conditions
from conditions import condition_matrix

import logging

LICENSE_FILES = [
    'MIT',
    'Apache-2.0',
    'GPL-3.0',
    'BSD-3-Clause',
    'AGPL-3.0',
    'GPL-2.0',
    'ISC',
    'BSD-2-Clause',
    'LGPL-3.0',
    'MPL-2.0',
    'LGPL-2.1',
    '0BSD',
    'EPL-2.0',
    'BSL-1.0'
]

LICENSES = [
    'MIT',
    'Apache-2.0',
    'GPL-3.0-only',
    'GPL-3.0-or-later',
    'BSD-3-Clause',
    'AGPL-3.0-only',
    'AGPL-3.0-or-later',
    'GPL-2.0-only',
    'GPL-2.0-or-later',
    'ISC',
    'BSD-2-Clause',
    'LGPL-3.0-only',
    'LGPL-3.0-or-later',
    'MPL-2.0',
    'LGPL-2.1-only',
    'LGPL-2.1-or-later',
    '0BSD',
    'EPL-2.0',
    'BSL-1.0'
]

# global license list
_licenses = None

SCRIPT_DIR = os.path.dirname(__file__)
TOP_DIR = os.path.join(SCRIPT_DIR, '..')
DATA_DIR = os.path.join(TOP_DIR, 'licenses')

def general_conditions(term):
    for condition_name in conditions:
        condition = conditions[condition_name]
        for alias in condition['aliases']:
            if alias == term['description']:
                return condition_name

def build_license(license_name, data):
    _conditions = []
    for term in data['terms']:
        general_condition = general_conditions(term)
        if general_condition:
            _conditions.append(general_condition)

    data['general_conditions'] = _conditions
    return data

def read_license(license_name):
    license_file = os.path.join(DATA_DIR, f'{license_name}.yaml')
    with open(license_file) as fp:
        return build_license(license_name, yaml.safe_load(fp)[0])

def read_licenses():
    global _licenses
    licenses = {}
    for license_name in LICENSE_FILES:
        license_object = read_license(license_name)
        license_id = license_object['licenseId']
        keys = []
        if isinstance(license_id, str):
            keys = [license_id]
        else:
            keys = license_id

        license_obj = read_license(license_name)
        for key in keys:
            licenses[key] = read_license(license_name)

    licenses['LGPL-3.0-only']['general_conditions'] += licenses['GPL-3.0-only']['general_conditions']
    licenses['LGPL-3.0-or-later']['general_conditions'] += licenses['GPL-3.0-or-later']['general_conditions']
    licenses['LGPL-2.1-only']['general_conditions'].remove('copyleft_strong')
    licenses['LGPL-2.1-or-later']['general_conditions'].remove('copyleft_strong')
    licenses['LGPL-3.0-only']['general_conditions'].remove('copyleft_strong')
    licenses['LGPL-3.0-or-later']['general_conditions'].remove('copyleft_strong')
    _licenses = licenses
    return licenses

def license_object(license_name):
    if license_name in _licenses:
        return _licenses[license_name]
    assert False

def relicense_allowed(license_name):
    return 'other_license' in _licenses[license_name]['general_conditions']

def relicense_licenses(license_name):
    if not relicense_allowed(license_name):
        return []

    licenses = conditions['other_license']['licenses'].get(license_name)
    if not licenses:
        return []

    return licenses
    
    
def condition_compatibility(outbound_condition, inbound_condition, outbound, inbound):
#    if inbound_condition == 'copyleft_module':
#        logging.debug("val: CL module")
        
#    if inbound_condition == 'copyleft_file':
#        logging.debug("val: CL file")
        
    if inbound_condition == 'copyleft_strong':
        # if the inbound and outbound license(s) are the same, then "yes"
        same = (outbound == inbound)

        general_conditions = _licenses[outbound]['general_conditions']

        # See if we can relicense the outbound
        if 'other_license' in general_conditions:
            other_license_cond = conditions['other_license']
            other_license = other_license_cond['licenses'].get(outbound)

            if other_license == inbound:
                logging.debug("other_license found RESOLVED")
                return "yes", None

        if inbound in ['LGPL-2.0-only', 'LGPL-2.0-or-later', 'LGPL-2.1-only', 'LGPL-2.1-or-later', 'LGPL-3.0-only', 'LGPL-3.0-or-later']:
            logging.debug("LFC")
            # TODO: this is a hack need since both LGPL and GPL says "Modifications or derivative work must be licensed under same license"
            return "yes", None
        elif same:
            return "yes", None
        else:
            reason = f'The condition "{inbound_condition}" of the inbound license "{inbound}" requires the outbound license to be "{inbound}" instead of "{outbound}".'

            if outbound.startswith('AGPL-3') and inbound.startswith('AGPL-3'):
                if not (outbound.endswith('-or-later') and inbound.endswith('-only')):
                    return "yes", None
            if outbound.startswith('GPL-2') and inbound.startswith('GPL-2'):
                if not (outbound.endswith('-or-later') and inbound.endswith('-only')):
                    return "yes", None
            if (outbound.startswith('GPL-3') or outbound.startswith('AGPL-3')) and inbound.startswith('GPL-3'):
                if not (outbound.endswith('-or-later') and inbound.endswith('-only')):
                    return "yes", None
                
            
            return "no", reason

    # outbound_condition is None when the license has no conditions, e.g. 0BSD
    if not outbound_condition:
        return "yes", None
    
    oc_value = condition_matrix[outbound_condition]
    if oc_value == None:
        return "yes", None


    if outbound_condition == 'no_further_restriction' :
        # if the inbound and outbound license(s) are the same, then "yes"
        same = (outbound == inbound)
        if same:
            return "yes", None

        
        outbound_conditions = license_object(outbound)['general_conditions']
        inbound_conditions = license_object(inbound)['general_conditions']
        restriction = conditions[inbound_condition].get('restriction', False)
        if (not inbound_condition in outbound_conditions) and restriction:
            reason = f'Condition "{outbound_condition}" does not allow adding condition "{inbound_condition}"'
            logging.debug(f'RETURN {reason}" ... since the condition is a restriction')
            return "no", reason

    return "yes", None


def license_compatibility(outbound, inbound):
    condition_compats = []

    if license_object(outbound)['general_conditions'] == []:
        outbound_conditions = [None]
    else:
        outbound_conditions = license_object(outbound)['general_conditions']
    
    for outbound_condition in outbound_conditions:
        for inbound_condition in license_object(inbound)['general_conditions']:
            val, reason = condition_compatibility(outbound_condition, inbound_condition, outbound, inbound)
            if val != "yes":
                condition_compats.append((val, reason))

    if len(condition_compats) != 0:
        if relicense_allowed(outbound):
            logging.debug(f'incompat - {outbound} relicensable')
        if relicense_allowed(inbound):
            if outbound in relicense_licenses(inbound):
                logging.debug(f'incompat {outbound} <--- {inbound}, but inbound relicensable, match found')
                condition_compats = []
                

    return list(set(condition_compats))

