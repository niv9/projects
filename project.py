# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:52:52 2024

@author: MS Surface Laptop
"""
import matplotlib.pyplot as plt
data=[[0,0,0,0,0,0,0,0],
      [0,0,1,1,1,1,0,0],
      [0,0,1,0,0,1,0,0],
      [0,0,1,0,0,1,0,0],
      [0,0,1,0,0,1,0,0],
      [0,0,1,0,0,1,0,0],
      [0,0,1,1,1,1,0,0],
      [0,0,0,0,0,0,0,0],
      ]

plt.imshow(data,cmap="gray")
plt.show()