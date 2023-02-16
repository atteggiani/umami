#!/usr/bin/env python

# Copyright 2022 ACCESS-NRI and contributors. See the top-level COPYRIGHT file for details.
# SPDX-License-Identifier: Apache-2.0

# Script created by Davide Marchegiani (davide.marchegiani@anu.edu.au) at ACCESS-NRI.

import sys
from umami.quieterrors import QValueError

def get_dim_name(inputNCFile,dim_names,errmsg):
    for dim in dim_names:
        if dim in inputNCFile.dims:
            return dim
        else:
            raise QValueError(errmsg)

