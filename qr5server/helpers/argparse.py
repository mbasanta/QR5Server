'''Parse nested url dictionaries into appropriate python dictionaries'''

# pylint: disable=invalid-name
# pylint: disable=anomalous-backslash-in-string

import re

def __split__(string):
    matches = re.split("[\[\]]+", string)
    matches.remove('')
    return matches

def argparse(params):
    '''parse dictionary of url arguments into a nested dictionary'''
    results = {}
    for key in params:
        if '[' in key:
            key_list = __split__(key)
            d = results
            for partial_key in key_list[:-1]:
                if partial_key not in d:
                    d[partial_key] = dict()
                d = d[partial_key]
            d[key_list[-1]] = params[key]
        else:
            results[key] = params[key]
    return results
