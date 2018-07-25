#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Seaborn_demo_27.py
#  Example on violin plot with custom palette and related parameters
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

def Seaborn_demo_27(args):
	sns.set(style="whitegrid")

	# Load the example dataset of brain network correlations
	df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)

	# Pull out a specific subset of networks
	used_networks = [1, 3, 4, 5, 6, 7, 8, 11, 12, 13, 16, 17]
	used_columns = (df.columns.get_level_values("network")
	.astype(int)
	.isin(used_networks))
	df = df.loc[:, used_columns]

	# Compute the correlation matrix and average over networks
	corr_df = df.corr().groupby(level="network").mean()
	corr_df.index = corr_df.index.astype(int)
	corr_df = corr_df.sort_index().T

	# Set up the matplotlib figure
	f, ax = plt.subplots(figsize=(11, 6))

	# Draw a violinplot with a narrower bandwidth than the default
	sns.violinplot(data=corr_df, palette="Set3", bw=.2, cut=1, linewidth=1)

	# Finalize the figure
	ax.set(ylim=(-.7, 1.05))
	sns.despine(left=True, bottom=True)
	#myFig.canvas.set_window_title("Demo 27: Violin Plot with parameter changes") # parent window title
	plt.show()							# render plot on screen
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(Seaborn_demo_27(sys.argv))
