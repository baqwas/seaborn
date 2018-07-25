#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Seaborn_demo_31.py
#  Example on heat plot with pivot table data
#  
#  Copyright 2018  <pi@controller>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Reference: https://www.datacamp.com/community/tutorials/seaborn-python-tutorial

import matplotlib.pyplot as plt			# 2D plotting library
import numpy as np
import pandas as pd
import seaborn as sns					# statistical visualization library
from string import ascii_letters

def Seaborn_demo_31(args):
	sns.set(style="white")
	myFig, myAxis = plt.subplots(figsize=(11,9))# Set up the matplotlib figure
	rs = np.random.RandomState(33)		# Generate a large random dataset
	d = pd.DataFrame(data=rs.normal(size=(100, 26)),
	columns=list(ascii_letters[26:]))
	corr = d.corr()						# Compute the correlation matrix
	mask = np.zeros_like(corr, dtype=np.bool)# Generate a mask for the upper triangle
	mask[np.triu_indices_from(mask)] = True
	cmap = sns.diverging_palette(220, 10, as_cmap=True)# Generate a custom diverging colormap
	sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
		square=True, linewidths=.5, cbar_kws={"shrink": .5})# Draw the heatmap with the mask and correct aspect ratio
	myFig.canvas.set_window_title("Demo 31: Heat Plot with pivot data") # parent window title
	plt.show()							# render plot on screen
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(Seaborn_demo_31(sys.argv))
