# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 01:08:21 2025

@author: manee
"""

from pydantic import BaseModel
class Banknote(BaseModel):
    variance:float
    skewness:float
    curtosis:float
    entropy:float