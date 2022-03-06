from importlib.resources import path
from unittest import result
from charset_normalizer import CharsetDetector
import pandas as pd
import chardet
import os

import utils


def create_csvs_by_column_value(file_name, column_name):
    df = _read_csv(file_name)
    unique_values = _get_column_unique_values(df, column_name)

    file_name_without_ext = file_name.split('.')[0]
    destinition_dir_name = f"{column_name.lower()}_{file_name_without_ext}"
    _create_folder_in_reports(destinition_dir_name)

    for value in unique_values:
        report_name = value.lower() # lowercase report file 
        report_name = report_name + '.csv'

        filtered_df = _filter_df_by_column(df, column_name, value)

        destinition_dir_name = destinition_dir_name + "/"
        file_path = utils.create_path("reports/" + destinition_dir_name, report_name)

        filtered_df.to_csv(file_path)
    

def _read_csv(file_name):
    file_path = utils.create_path('reports/', file_name)
    file_encoding = _detect_file_encoding(file_path, 10000)['encoding']

    df = pd.read_csv(file_path, encoding=file_encoding)

    return df


def _filter_df_by_column(df:pd.DataFrame, column_name, common_value):
    filtered_df = df.loc[df[column_name] == common_value]

    return filtered_df


def _get_column_unique_values(df:pd.DataFrame, column_name:str):
    unique_values = df[column_name].unique()
    return unique_values


def _detect_file_encoding(file_path, n_byte: int):
    """
    To get the encoding more precisely use bigger n_byte to read
    """
    with open(file_path, 'rb') as rawdata:
        file_encoding = chardet.detect(rawdata.read(n_byte))
        return file_encoding


def _create_folder_in_reports(folder_name):
    folder_name = folder_name.lower()
    reports_path = utils.create_path('reports/')
    dir_name = reports_path + folder_name

    if os.path.exists(dir_name) != True:
        os.mkdir(dir_name)
        return dir_name
    


if __name__ == '__main__':
    file_name = 'pcm_donaciones.csv'
    #df = _read_csv(file_name)
    #print(_filter_df_by_column(df, 'REGION', 'LIMA'))
    #print(_get_column_unique_values(df, 'REGION'))

    create_csvs_by_column_value(file_name, 'REGION')
    #_create_folder_in_reports('region')
