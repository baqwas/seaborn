#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Seaborn_demo_25.py
#  Example on violin plot
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

def Seaborn_demo_25(args):
	myFig, ax = plt.subplots()
	myData = sns.load_dataset("tips")	# classic dataset: tips
	sns.violinplot(x="day", y="total_bill", data=myData, palette="rainbow") # violin plot
	myFig.canvas.set_window_title("Demo 25: Violin Plot") # parent window title
	plt.show()							# render plot on screen
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(Seaborn_demo_25(sys.argv))
