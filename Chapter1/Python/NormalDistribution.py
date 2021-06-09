#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 01:45:11 2021

@author: moisesr
"""

from scipy import stats

xbar = 67
mu0 = 52
s = 16.3


# Calculating z-scores
z = (67-52) / 16.3

# Calculating the probability under the curve
p_val = 1- stats.norm.cdf(z)
print("Prob. to score more than 67 is ", round(p_val*100,2),"%")