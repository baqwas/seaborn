#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Seaborn_demo_20.py
#  Example on bar plot with parameter overrides
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
import seaborn as sns					# statistical visualization library

def Seaborn_demo_20(args):
	sns.set(style="whitegrid")	
	f, ax = plt.subplots(figsize=(6, 15))# Initialize the matplotlib figure

	crashes = sns.load_dataset("car_crashes").sort_values("total", 
		ascending=False)				# Load the example car crash dataset

	sns.set_color_codes("pastel")		# Plot the total crashes
	sns.barplot(x="total", y="abbrev", data=crashes,
	label="Total", color="b")

	sns.set_color_codes("muted")		# Plot the crashes where alcohol was involved
	sns.barplot(x="alcohol", y="abbrev", data=crashes,
	label="Alcohol-involved", color="b")
	
	ax.legend(ncol=2, loc="lower right", frameon=True)# Add a legend and informative axis label
	ax.set(xlim=(0, 24), ylabel="",
	xlabel="Automobile collisions per billion miles")
	sns.despine(left=True, bottom=True)
	#fig.canvas.set_window_title("Regression with hue") # regression plot
	plt.show()							# render plot on screen
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(Seaborn_demo_20(sys.argv))
