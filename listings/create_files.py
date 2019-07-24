# SPDX-License-Identifier: MIT
#
# create_files.py - tool to create the JSON files required for listing storage
#
# Copyright (c) 2019 Joe Dai.

import os
import json
from pathlib import Path

from listing import CATEGORIES


def create_files(categories: list):
    """Create files function

    Creates empty files in ./data directory based on
    the given categories.

    Args:
        categories: list of categories (used as filenames: {category}.json

    Returns: nothing

    """
    for category in categories:
        path = (Path()/'data'/f'{category}.json')

        path.touch()

        if os.stat(path).st_size == 0:    # so we don't accidentally overwrite files
            with open(path, 'w') as f:
                json.dump([], f)          # write empty array

        print("Touched: " + str(path))


if __name__ == '__main__':
    create_files(CATEGORIES)
