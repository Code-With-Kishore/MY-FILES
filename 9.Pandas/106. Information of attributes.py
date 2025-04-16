# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 11:28:00 2025

@author: Admin
"""

import pandas as pd
import numpy as np

roll = [225213101 + i for i in range(20)]
sub=['Tamil', 'English', 'Maths', 'Science', 'Social']
m = np.random.randint(50, 100, (20, 5), dtype=np.uint32)
x = pd.DataFrame(m, index=roll, columns=sub)

print(x)

# Index (Row labels)
print("\nIndex:\n", x.index)

# Columns (Column labels)
print("\nColumns:\n", x.columns)

# Axes (Row and column axis)
print("\nAxes:\n", x.axes)

# Data types of columns
print("\nData Types:\n", x.dtypes)

# Size (Total number of elements)
print("\nSize:\n", x.size)

# Shape (Dimensions of the DataFrame)
print("\nShape:\n", x.shape)

# Number of dimensions
print("\nDimensions (ndim):\n", x.ndim)

# Check if DataFrame is empty
print("\nIs Empty:\n", x.empty)

# Check for NaN values 
print("\nCheck NaN:\n", x.isna())

# Count of non-NaN entries (overall, default axis=0)
print("\nCount (axis=0, columns):\n", x.count())

# Count of non-NaN entries (axis=0 => column-wise count)
print("\nCount (axis=0, column-wise):\n", x.count(axis=0))

# Count of non-NaN entries (axis=1 => row-wise count)
print("\nCount (axis=1, row-wise):\n", x.count(axis=1))
