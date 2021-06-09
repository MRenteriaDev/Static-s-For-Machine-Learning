#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 01:35:10 2021

@author: moisesr
"""

from scipy import stats
import numpy as np

xbar = 990
mu0=1000
s =12.5
n=30

# Test Statics
t_sample = (xbar-mu0) / (s/np.sqrt(float(n)))
print("Test Static :", round(t_sample,2))

# Critical value from t-table
alpha = 0.05
t_alpha = stats.t.ppf(alpha,n-1)
print("Critical value from a t-table :", round(t_alpha,3))

#Lower tail p-value from t-table
p_val = stats.t.sf(np.abs(t_sample), n-1)
print("Lower tail p-value from t-table", p_val)