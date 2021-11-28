'''
Module containing functions to calculate the statistics from the file
'''

from typing import Dict
from statistics import stdev, mean, median


def filter_columns(d: Dict) -> Dict:
    filtered_dict = {}
    for key in d.keys():
        if not isinstance(d[key][0], str):
            filtered_dict[key] = d[key]
    return filtered_dict


def calculate(d: Dict) -> Dict:
    value = {'mean':0, 'median':0, 'std':0}
    result_dict = dict(zip(d.keys(), [value.copy(), value.copy(), value.copy()]))
    print(d.keys())
    print(result_dict)
    for key in d.keys():
        print(key)
        result_dict[key]['mean'] = mean(d[key])
        result_dict[key]['median'] = median(d[key])
        result_dict[key]['std'] = stdev(d[key])
        print(result_dict)
    return result_dict


def get_statistics(d: Dict) -> Dict:
    filtered_dict = filter_columns(d)
    result_dict = calculate(filtered_dict)
    return result_dict
