# SPDX-License-Identifier: MIT
#
# interface.py - implements an interface to the raw JSON listing files
#
# Copyright (c) 2019 Joe Dai.

import json

from json import JSONDecodeError
from typing import List
from pathlib import Path

from listing import *


DATA_DIR = 'listings/data'


def get_listings(category: str) -> List[Listing]:
    """Returns listings based on a given category

    Args:
        category: Category that function should get

    Returns:
        A list of Listing objects which contain the name, url, and category of the listing(s)

    """
    if category in CATEGORIES:
        with open(Path()/DATA_DIR/f'{category}.json') as f:
            data = json.load(f)
    else:
        raise ValueError("Invalid category")

    listings = []
    for listing in data:
        listings.append(Listing(listing['name'], listing['url'], listing['category']))

    return listings


def add_listing(name: str, url: str, category: str) -> Listing:
    """Adds a listing to given category

    Args:
        name: Name of the listing
        url: Discord invite URL of the listing
        category: Category of the listing

    Returns:
        Listing object that contains the info for the listing

    """
    listing = Listing(name, url, category)

    with open(Path()/DATA_DIR/f'{category}.json', 'r+') as f:  # open file in read+write mode
        try:
            data = json.load(f)
        except JSONDecodeError as e:            # must be an empty file
            print(e)
            data = [listing.__dict__]
            json.dump(data, f, indent=2)
        else:
            data.append(listing.__dict__)

            f.seek(0)                           # reset pointer to beginning of file
            json.dump(data, f, indent=2)

    return listing


def remove_listing(name: str, url: str, category: str):
    """Removes a listing from a given category

    Args:
        name: Name of the listing
        url: Discord invite URL of the listing
        category: Category of the listing

    Returns: nothing

    """
    listing = Listing(name, url, category)
    path = Path() / DATA_DIR / f'{category}.json'

    with open(path, 'r') as f:                  # open file in read mode
        data = json.load(f)
        data.remove(listing.__dict__)

    with open(path, 'w') as f:                  # open file in write mode
        json.dump(data, f, indent=2)
