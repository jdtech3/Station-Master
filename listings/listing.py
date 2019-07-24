# SPDX-License-Identifier: MIT
#
# listing.py - defines Listing class
#
# Copyright (c) 2019 Joe Dai.


CATEGORIES = [          # Valid categories
    # Alliances
    'alliance_a',
    'alliance_b',
    'alliance_c',
    'alliance_d',
    'alliance_e',
    'alliance_f',
    'alliance_g',
    'alliance_h',
    'alliance_i',
    'alliance_j',
    'alliance_k',
    'alliance_l',
    'alliance_m',
    'alliance_n',
    'alliance_o',
    'alliance_p',
    'alliance_q',
    'alliance_r',
    'alliance_s',
    'alliance_t',
    'alliance_u',
    'alliance_v',
    'alliance_w',
    'alliance_x',
    'alliance_y',
    'alliance_z',

    # Businesses
    'art',
    'bank',
    'casino',
    'community',
    'mercenary',
    'news',
    'trade',
    'other',

    # Conglomerates / Corporations
    'beacon',
    'strategy'
]


class Listing:
    """Stores information for a single listing

    Attributes:
        name: Name of the listing
        url: Discord invite link of the listing
        category: Category of the listing

    Raises:
        ValueError: Invalid category
    """

    def __init__(self, name: str, url: str, category: str):
        self.name = name
        self.url = url

        if category in CATEGORIES:
            self.category = category
        else:
            raise ValueError("Invalid category")
