#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Seaborn_demo_24.py
#  Example on box plot with custom palette and hue
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

def Seaborn_demo_24(args):
	sns.set(style="ticks")

	f, ax = plt.subplots(figsize=(7, 6))# Initialize the figure with a logarithmic x axis
	ax.set_xscale("log")

	planets = sns.load_dataset("planets")# Load the example planets dataset

	sns.boxplot(x="distance", y="method", data=planets,
	whis=np.inf, palette="rainbow")# Plot the orbital period with horizontal boxes

	sns.swarmplot(x="distance", y="method", data=planets,
	size=2, color=".3", linewidth=0)# Add in points to show each observation

	ax.xaxis.grid(True)# Tweak the visual presentation
	ax.set(ylabel="")
	sns.despine(trim=True, left=True)

	#fig.canvas.set_window_title("Regression with hue") # regression plot
	plt.show()							# render plot on screen
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(Seaborn_demo_24(sys.argv))
