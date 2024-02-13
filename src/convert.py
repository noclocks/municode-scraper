# NOTE: File not currently in use.

import os
import pandas as pd

base_directory = os.path.dirname(os.path.abspath(__file__))
output_directory = os.path.join(base_directory, 'output')
output_csv_path = os.path.join(output_directory, 'output.csv')

os.makedirs(output_directory, exist_ok=True)

def combine_txt_files(path, output):
    folder_name = os.path.basename(path)
    output_path = os.path.join(output, f'{folder_name}.csv')
