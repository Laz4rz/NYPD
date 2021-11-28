import csv
from typing import Dict, List


def list_transpose(a: List) -> List:
    list_transposed = [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
    return list_transposed


def list_to_dict(a: List) -> Dict:
    column_names = [column[0] for column in a]
    column_values = [
        column[1:] if not column[1][0].isdigit()
        else  list(map(float, column[1:]))
        for column in a
    ]
    dictionary = dict(zip(column_names, column_values))
    return dictionary


def load_csv(path: str) -> Dict:
    content_reader = csv.reader(open(path), delimiter=',')
    content_list = list(content_reader)
    content_list_T = list_transpose(content_list)
    content_dictionary = list_to_dict(content_list_T)
    return content_dictionary
