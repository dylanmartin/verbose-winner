#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script includes the remote computations for single-shot ridge
regression with decentralized statistic calculation
"""
import sys
import ujson as json
from scripts.ancillary import list_recursive, get_unique_phase_key
from scripts.remote_funcs import remote_1 ,remote_2


def start(PARAM_DICT):
    PHASE_KEY = list(list_recursive(PARAM_DICT, "computation_phase"))

    if "local_0" in PHASE_KEY:
        return remote_0(PARAM_DICT)
    elif "local_1" in PHASE_KEY:
        return remote_1(PARAM_DICT)
    elif "local_2" in PHASE_KEY:
        return remote_2(PARAM_DICT)
    else:
        raise ValueError("Error occurred at Remote")

