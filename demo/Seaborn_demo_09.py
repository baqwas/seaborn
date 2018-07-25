#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Seaborn_demo_09.py
#  Example on regression plot with size truncation
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
import seaborn as sns					# statistical visualization library

def Seaborn_demo_09(args):
	sns.set(style="ticks")							# initialization
	myData = sns.load_dataset("anscombe")		# classic dataset: Anscombe's quartet
	myPlot = sns.lmplot(x="x", y="y", data=myData,
		hue="dataset", col="dataset", col_wrap=2, ci=None, palette="muted", size=4,
		scatter_kws={"s":50, "alpha":1})
	#fig.canvas.set_window_title("Regression with hue") # regression plot
	plt.show()							# render plot on screen
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(Seaborn_demo_09(sys.argv))
