#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 01:12:14 2021

@author: moisesr
"""

import pandas as pd
from scipy import stats


fertiliziers = pd.read_csv("../Data/fetilizers.csv")

one_way_anova = stats.f_oneway(fertiliziers["fertilizer1"],
                               fertiliziers["fertilizer2"],
                               fertiliziers["fertilizer3"])

print("Statitics :", round(one_way_anova[0],2),",p-value :", 
      round(one_way_anova[1],3))