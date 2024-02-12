#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script includes the local computations for single-shot ridge
regression with decentralized statistic calculation
"""
import sys
import ujson as json
from scripts.ancillary import list_recursive, get_unique_phase_key
from scripts.local_funcs import local_1, local_2


def start(PARAM_DICT):
    PHASE_KEY = list(list_recursive(PARAM_DICT, "computation_phase"))

    if not PHASE_KEY:
        return local_1(PARAM_DICT)
    elif 'remote_1' in PHASE_KEY:
        return local_2(PARAM_DICT)
    else:
        raise ValueError("Error occurred at Local")