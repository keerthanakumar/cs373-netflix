#!/usr/bin/env python3

# ------------------------------
# projects/netfilx/RunNetflix.py
# Copyright (C) 2014
# Keerthana Kumar, Fatimah Zohra
# ------------------------------

# -------
# imports
# -------

import sys

from Netflix import netflix_solve

# ----
# main
# ----

if __name__ == "__main__" :
    netflix_solve(sys.stdin, sys.stdout)

