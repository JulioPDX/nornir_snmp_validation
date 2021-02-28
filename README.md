# Nornir SNMP Validation

## Purpose

This is my example of using Nornir and NAPALM to validate device configurations. In this case we are looking at SNMP. If you have any questions please check out the associated blog post [here](https://juliopdx.com/2021/02/27/network-validation-with-nornir-napalm/). Thank you for checking out the repo.

## Environment

- `python3 -m venv venv`
- `source venv/bin/activate`
- `git clone https://github.com/JulioPDX/nornir_snmp_validation.git`
- `cd nornir_snmp_validation/`
- `pip install -r requirements.txt`

## Setup

Feel free to update the host file to match your environment.

## Output

```bash
(venv) juliopdx@juliopdx-virtual-2004:~/git/nornir_snmp_validation$ python snmp_validate.py 
GATHERING SNMP******************************************************************
* NE-RTR-01 ** changed : False *************************************************
vvvv GATHERING SNMP ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'get_snmp_information': { 'chassis_id': '',
                            'community': { 'private': { 'acl': 'N/A',
                                                        'mode': 'rw'},
                                           'public': { 'acl': 'N/A',
                                                       'mode': 'ro'}},
                            'contact': 'JulioPDX',
                            'location': 'mylocation'}}
^^^^ END GATHERING SNMP ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* NY-SW-01 ** changed : False **************************************************
vvvv GATHERING SNMP ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'get_snmp_information': { 'chassis_id': '9NA76XNH9Z8',
                            'community': { 'myreadonly': { 'acl': 'N/A',
                                                           'mode': 'ro'},
                                           'mysecurestring': { 'acl': 'N/A',
                                                               'mode': 'rw'}},
                            'contact': 'JulioPDX',
                            'location': 'mylocation'}}
^^^^ END GATHERING SNMP ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* OR-SW-01 ** changed : False **************************************************
vvvv GATHERING SNMP ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'get_snmp_information': { 'chassis_id': '9QA913OVFJS',
                            'community': { 'myreadonly': { 'acl': 'N/A',
                                                           'mode': 'ro'},
                                           'mysecurestring': { 'acl': 'N/A',
                                                               'mode': 'rw'}},
                            'contact': 'JulioPDX',
                            'location': 'mylocation'}}
^^^^ END GATHERING SNMP ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
VALIDATE SNMP*******************************************************************
* NE-RTR-01 ** changed : False *************************************************
vvvv VALIDATE SNMP ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'complies': False,
  'get_snmp_information': { 'complies': False,
                            'extra': [],
                            'missing': [],
                            'present': { 'community': { 'complies': False,
                                                        'diff': { 'complies': False,
                                                                  'extra': [],
                                                                  'missing': [ 'myreadonly',
                                                                               'mysecurestring'],
                                                                  'present': { }},
                                                        'nested': True},
                                         'contact': { 'complies': True,
                                                      'nested': False},
                                         'location': { 'complies': True,
                                                       'nested': False}}},
  'skipped': []}
^^^^ END VALIDATE SNMP ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* NY-SW-01 ** changed : False **************************************************
vvvv VALIDATE SNMP ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'complies': True,
  'get_snmp_information': { 'complies': True,
                            'extra': [],
                            'missing': [],
                            'present': { 'community': { 'complies': True,
                                                        'nested': True},
                                         'contact': { 'complies': True,
                                                      'nested': False},
                                         'location': { 'complies': True,
                                                       'nested': False}}},
  'skipped': []}
^^^^ END VALIDATE SNMP ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* OR-SW-01 ** changed : False **************************************************
vvvv VALIDATE SNMP ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
{ 'complies': True,
  'get_snmp_information': { 'complies': True,
                            'extra': [],
                            'missing': [],
                            'present': { 'community': { 'complies': True,
                                                        'nested': True},
                                         'contact': { 'complies': True,
                                                      'nested': False},
                                         'location': { 'complies': True,
                                                       'nested': False}}},
  'skipped': []}
^^^^ END VALIDATE SNMP ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(venv) juliopdx@juliopdx-virtual-2004:~/git/nornir_snmp_validation$ 
```
