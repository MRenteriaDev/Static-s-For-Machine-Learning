#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 01:11:16 2021

@author: moisesr
"""
import numpy as np
from scipy import stats
from statistics import variance, stdev


game_points = np.array([35,56,43,59,63,79,35,41,64,43,93,60,77,24,82])

# Calculare Variance
#This is the mean of squared deviations from the mean
dt_var = variance(game_points)
print("Sample Variance :" ,round(dt_var,2))

# Calculate Stadard Deviation
#This is the square root of variance
dt_std = stdev(game_points)
print("Sample std.dev :", round(dt_std,2))

# Calculate Range
dt_rng = np.max(game_points, axis=0) - np.min(game_points, axis=0)
print("Range :", dt_rng)

# Calculate the percentiles
print("Quantiles :")
for val in [20,80,100]:
    dt_qnls = np.percentile(game_points,val)
    print(str(val)+"%", dt_qnls)

# Calculate IQR
q75, q25 = np.percentile(game_points, [75,25])
print("Interquantile range :",q75 - q25)