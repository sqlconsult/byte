#!/usr/bin/env python3

import os
import controller as controller


def test_files_and_dirs_exist():
    """
    Tests input & output directories and files exist
    """
    input_params = {'input_dir': '../input',
                    'input_file': 'orders.csv',
                    'output_dir': '../output',
                    'output_file': 'redemptions.csv',
                    'input_file_path': '',
                    'output_file_path': '',
                    'files_exist': True}

    validated_params = controller.files_exist(input_params)

    assert validated_params['input_file_path'] == '../input/orders.csv'

    assert validated_params['output_file_path'] == '../output/redemptions.csv'

    assert validated_params['files_exist']


def test_inp_dir_not_exists():
    """
    Tests input directory does not exist
    """
    input_params = {'input_dir': '../input_xxx',
                    'input_file': 'orders.csv',
                    'output_dir': '../output',
                    'output_file': 'redemptions.csv',
                    'input_file_path': '',
                    'output_file_path': '',
                    'files_exist': True}

    validated_params = controller.files_exist(input_params)

    assert not validated_params['files_exist']


def test_inp_file_not_exists():
    """
    Tests input file does not exist
    """
    input_params = {'input_dir': '../input',
                    'input_file': 'orders_xxx.csv',
                    'output_dir': '../output',
                    'output_file': 'redemptions.csv',
                    'input_file_path': '',
                    'output_file_path': '',
                    'files_exist': True}

    validated_params = controller.files_exist(input_params)

    assert not validated_params['files_exist']


def test_out_dir_not_exists():
    """
    Tests output directory does not exist
    """
    input_params = {'input_dir': '../input',
                    'input_file': 'orders.csv',
                    'output_dir': '../output_xxx',
                    'output_file': 'redemptions.csv',
                    'input_file_path': '',
                    'output_file_path': '',
                    'files_exist': True}

    validated_params = controller.files_exist(input_params)

    assert os.path.isdir(input_params['output_dir'])
    assert validated_params['files_exist']

    # clean up
    os.system('rm -rf {0}'.format(input_params['output_dir']))
