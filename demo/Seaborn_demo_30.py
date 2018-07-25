#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Seaborn_demo_30.py
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
import seaborn as sns					# statistical visualization library

def Seaborn_demo_30(args):
	sns.set()
	myFig, myAxis = plt.subplots(figsize=(9,6))
	myData = sns.load_dataset('flights')
	flightData = myData.pivot("month", "year", "passengers")
	sns.heatmap(flightData, annot=True, fmt="d", linewidth=0.5, ax=myAxis)
	myFig.canvas.set_window_title("Demo 30: Heat Plot with pivot data") # parent window title
	plt.show()							# render plot on screen
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(Seaborn_demo_30(sys.argv))
