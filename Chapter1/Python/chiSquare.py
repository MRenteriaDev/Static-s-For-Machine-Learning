#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 00:57:01 2021

@author: moisesr
"""

import pandas as pd
from scipy import stats

survey = pd.read_csv('../Data/survey.csv')

# Tabulating 2 variables with row & column variables respectively

survey_tab = pd.crosstab(survey.Smoke, survey.Exer, margins= True)

# Creating observed table for analysis
observed = survey_tab.iloc[0:4,0:3]

contg = stats.chi2_contingency(observed=observed)
p_value = round(contg[1],3)
print("p-value is :", p_value)