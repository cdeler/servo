# Copyright 2013 The Servo Project Developers. See the COPYRIGHT
# file at the top-level directory of this distribution.
#
# Licensed under the Apache License, Version 2.0 <LICENSE-APACHE or
# http://www.apache.org/licenses/LICENSE-2.0> or the MIT license
# <LICENSE-MIT or http://opensource.org/licenses/MIT>, at your
# option. This file may not be copied, modified, or distributed
# except according to those terms.

from os import listdir
from os.path import isfile, isdir, join
import json
import sys
import test


def get_folders_list(path):
    folder_list = []
    for filename in listdir(path):
        if isdir(join(path, filename)):
            folder_name = join(path, filename)
            folder_list.append(folder_name)
        return folder_list


def mutation_test_for(mutation_path):
    test_mapping_file = join(mutation_path, 'test_mapping.json')
    if isfile(test_mapping_file):
        json_data = open(test_mapping_file).read()
        test_mapping = json.loads(json_data)
        # Run mutation test for all source files in mapping file.
        for src_file in test_mapping.keys():
            test.mutation_test(join(mutation_path, src_file.encode('utf-8')), test_mapping[src_file])
        # Run mutation test in all folder in the path.
        for folder in get_folders_list(mutation_path):
            mutation_test_for(folder)
    else:
        print("This folder {0} has no test mapping file.".format(mutation_path))

mutation_test_for(sys.argv[1])
