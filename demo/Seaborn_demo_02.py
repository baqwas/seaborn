#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Seaborn_demo_02.py
#  Introductory example on using the Seaborn library
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

def Seaborn_demo_02(args):
	"""
	subplots: create a figure and a set of subplots
	parameters:
		nrows, ncols:	int, optional, default=1
		sharex, sharey:	bool or {"none", a"all", "row", "col"}, default: False
		squeeze:	bool, optional, default=True
		subplot_kw:	dict, optional
		gridspec_kw:	dict, optional
		**fig_kw:	passed to figure call
	returns:
		fig:	matplotlib.figure.Figure object
		ax:		axes object or array of axes objects
	"""
	fig, ax = plt.subplots()			# initialize figure and axies objects
	"""
	load_dataset: load a dataset from the online repository
	parameters:
		name:		str, name of dataset, use get_dataset_names() for list or visit https://github.com/mwaskom/seaborn-data
		cache:		bool, optional, =True for local cache
		data_home:	string, to write cache data, default ~/seaborn-data/
		kws:		dict, optional, used by pandas_read_csv
	"""
	tips = sns.load_dataset("tips")	# data courtesy: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
	"""
	violinplot: draw a combination of boxplot and kernel density estimate
	parameters:
		x. y, hue:	names of variables in data, optional
		data:		DataFrame, array or list of arrays, optional
		order, hue_order:	list of strings, optional
		bw:			{"scott", "silverman"}, optional
		cut:		float, optional
		scale:		{"area", "count"}, optional
		scale_hue:	bool, optional
		gridsize:	int, optional
		width:		float, optional
		inner:		{"box", "quartile", "point", "stick", None}, optional
		split:		bool, optional
		dodge:		bool, optional
		orient:		["v" | "h"], optional
		linewidth:	float, optional
		color:		matplotlib color, optional
		palette:	palette name, list or dict, optional
		saturation:	float, optional
		ax:			matplotlib axes, optional
	returns:
		ax:			matplotlib axes object with plot rendered
	"""
	sns.violinplot(x="total_bill", data=tips) # violin plot
	"""
	set_window_title: set the title text of the window containing the figure
	parameters:
		title:		str, optional
	"""
	fig.canvas.set_window_title("Demo 2: Violinplot")
	"""
	savefig: save the current figure
	parameters:
		fname:		str, file-like object
		dpi:		scalar, [None | scalar > 0 | "figure"]
		facecolor:	[None | color spec], optional
		orientation:{"landscape", "portrait"}
		papertype:	str, for PostScript output only
		format:		as supported by backend, png, pdf, ps, eps and svg
		transparent:bool, optional
		frameon:	bool, optional
		bbox_inches:str | Bbox, inches, optional
		pad_inches: scalar, optional
		bbox_extra_artists: list of Artist, optional
	returns:
		none?
	"""
	#plt.savefig("../images/demo_02.png")# for documentation use
	"""
	show: display a figure
	parameters:
		args:
		kwargs:
	returns:
	"""
	plt.show()							# render plot on screen
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(Seaborn_demo_02(sys.argv))
