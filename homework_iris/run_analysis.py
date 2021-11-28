'''
Main analysis script
'''

import argparse

from iris_analysis import load_csv, save_csv, get_statistics



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("result_file")
    args = parser.parse_args()

    input_path = args.input_file
    result_path = args.result_file

    file_dict = load_csv(input_path)
    statistics_dict = get_statistics(file_dict)

    save_csv(statistics_dict, result_path)
