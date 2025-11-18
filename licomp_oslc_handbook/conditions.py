conditions = {
    'provide_license': {
        'aliases': [ 'Provide copy of license',
                     'Provide license' ],
    },
    'provide_copyright':  {
        'aliases': [ 'Provide copyright notice' ]
    },
    'provide_source_code':  {
        'aliases': [
            "Provide corresponding source code",
            "Provide corresponding source code for modified versions to users interacting with the program remotely through a computer network (see section 13 for more details). For more information about AGPL-3.0 compliance and this condition in particular, see the references provided or consult your open source legal counsel.",
            "Provide source code"
        ]
    },
    'retain_notices': {
        'aliases': [
            'Retain all notices',
            'Retain notices',
            'Retain notices on all files',
        ]
    },
    'include-notice-file': {
        'aliases': [
            'Include NOTICE file with distribution'
        ]
    },
    'modification-notification': {
        'aliases': [
            'Notice of modifications'
        ]
    },
    'no-further-restriction': {
        'aliases': [
            'No additional restrictions',
        ]
    },
    'other_license': {
        'aliases': [
            'You may distribute under an enumerated \'Secondary License\' if authorized by the initial Contributor or combined with code under that Secondary License (see section 3.2 for more details)'
        ],
        'other_license': ['GPL-2.0-or-later']
    },
    'no_patent_claims': {
        'aliases': [
            "Any patent claims accusing the software by a licensee results in termination of all licenses to the licensee",
            "Any patent claims accusing the software by a licensee results in termination of patent licenses to the licensee",
            "Any patent claims accusing the work by a licensee results in termination of all patent licenses to the licensee.",
            "License terminates if you initiate litigation claiming use of the program under this license violates a patent",
        ]
    },
    'copyleft-strong': {
        'aliases': [
            'Modifications or derivative work must be licensed under same license'
        ]
    },
    'copyleft-file': {
        'aliases': [
            'Modifications under same license'
        ]
    },
    'copyleft-module': {
        'aliases': [
            'You may distribute binary versions under a different license, so long as you do not limit or alter the recipient\'s right in the source code under this license.',
            'You may distribute binary versions under a different license, so long as you do not limit or alter the recipient\'s right in the source code under this license. You must make it clear that any differing terms are offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make. See section 3.6 for more details.'
        ]
    },
    'installation-instructions': {
        'alias': [
            'Provide information necessary to install modified versions on \'User Products\''
        ]
    },
    'prohibit-circumvention': {
        'alias': [
            'May not prohibit circumvention of technological measures that prevent users from exercising rights under the license (see section 3 for more details)'
        ]
    },
    'disclaim-contributors': {
        'alias': [
            'You may distribute program under a different license, provided you disclaim contributors from warranties, liability, and defend contributors against any third party claims brought as a result of your distribution. Clarify that any provisions offered by you are offered by you only (see section 3 for details)'
        ]
    },
    'contributor-additions': {
        'alias': [
            'Contributors may add certain additional restrictions for their contributions, including disclaimers, legal notices, limitation of trademark and publicity rights, extension of indemnification received by licensor.'
        ]
    },
    'or-later-license-version': {
        'aliases': [
            'Allows use of covered code under the terms of same version or any later version of the license.',
            'Allows use of covered code under the terms of same version or any later version of the license or that version only, as specified. If no license version is specificed, then you may use any version ever published by the FSF.',
            'Allows use of covered code under the terms of same version or any later version of the license or that version only, as specified. If no license version is specified, then you may use any version ever published by the FSF.'
        ]
    },
    'allow-offer': {
        'aliases': [
            'You may offer and charge a fee for warranty, support, indemnity or liability obligations to recipients. However, you must make it clear that any such offer is offered by you alone and you agree to indemnify the initial developer and every contributor for any liability incurred by them as a result of the offer you make. See section 3.5 for more details.'
        ]
    },
    'library-facilities': {
        'aliases': [
            'If you create a combined library combining parts of the library (modified or not) with functions that are not based on the library, then you must accompany the combined library with a copy of the same work based on the library uncombined; give prominent notice that the library is used and explain where to find the accompanying uncomibed form of the work (see section 5 for more details)'
        ]
    },
    'header-file-inclusion': {
        'aliases': [
            'Object code incorporating header file material from the library that is not limited to numerical parameters, data structure layouts and accessors or small macros, inline functions and templates of fewer than ten lines must include a prominent notice that the library is used, its use is covered by LGPL-3.0, and provide a copy of the license (see section 3 for more details)'
        ]
    },
    'relicense': {
        'aliases': [
            'If you modify the library so that it does not function without data or function supplied by your application, the modified library can only be distributed under the terms of GPL-3.0. This restriction does not apply if the data or function is supplied as an argument.',
            'If software is combined with software under AGPL-3.0, AGPL-3.0 applies to combined work and this license continues to the covered work originally under GPL-3.0 (see section 13 for more details).'
        ]
    }
}

license_extras = {
    'relicense': {
        'If you modify the library so that it does not function without data or function supplied by your application, the modified library can only be distributed under the terms of GPL-3.0. This restriction does not apply if the data or function is supplied as an argument.': {
            'trigger': 'modified',
            'application': 'warning',
            'licenses': {
                'LGPL-3.0': {
                    'new-license': 'GPL-3.0'
                },
                'LGPL-3.0-only': {
                    'new-license': 'GPL-3.0-only'
                },
                'LGPL-3.0-or-later': {
                    'new-license': 'GPL-3.0-or-later'
                }
            }
        },
        'If software is combined with software under AGPL-3.0, AGPL-3.0 applies to combined work and this license continues to the covered work originally under GPL-3.0 (see section 13 for more details).': {
            'trigger': 'combined',
            'trigger-argument': 'AGPL-3.0',
            'application': 'warning',
            'licenses': {
                'GPL-3.0': {
                    'new-license': 'AGPL-3.0'
                },
                'GPL-3.0-only': {
                    'new-license': 'AGPL-3.0-only'
                },
                'GPL-3.0-or-later': {
                    'new-license': 'AGPL-3.0-or-later'
                }
            }
        }
    }
}

'ignorable': [
    'This license places no conditions whatsoever on using, copying, modifying or distributing the software for any purpose.',
    'License automatically terminates if you do not comply with the terms of the license',
    'License terminates upon failure to comply with license unless certain conditions are met by you and contributor (see section 5.1 for more details)',
    'License terminates upon failure to comply with "material terms or conditions" and failure to cure in a reasonable period of time after becoming aware of noncompliance',
    'Author may include \'additional permissions\' making exceptions from license terms. You may remove additional permission when you convey the work.',
    'Allows distribution of combined LGPL-3.0 and other code under under a different license, under certain conditions.',
    'Allows dynamic linking of code with “a work that uses the Library” under a different license, under certain conditions.'
]

### L/GPL version 3
