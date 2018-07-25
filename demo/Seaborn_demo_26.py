#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Seaborn_demo_26.py
#  Example on violin plot with custom palette
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

def Seaborn_demo_26(args):
	myFig, ax = plt.subplots()


	rs = np.random.RandomState(0)		# Create a random dataset across several variables
	n, p = 40, 8
	d = rs.normal(0, 2, (n, p))
	d += np.log(np.arange(1, p + 1)) * -5 + 10
	pal = sns.cubehelix_palette(p, rot=-.5, dark=.3)# Use cubehelix to get a custom sequential palette
	sns.violinplot(data=d, palette=pal, inner="points")# Show each distribution with both violins and points
	myFig.canvas.set_window_title("Demo 26: Violin Plot with custom palette") # parent window title
	plt.show()							# render plot on screen
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(Seaborn_demo_26(sys.argv))
