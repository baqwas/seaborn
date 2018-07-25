#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Seaborn_demo_01.py
#  Introductory example on using matplotlib library
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
#  References
#  https://matplotlib.org/faq/howto_faq.html
#  https://www.datacamp.com/community/tutorials/seaborn-python-tutorial

import matplotlib.pyplot as plt			# 2D plotting library
import pandas as pd						# numerical data handling library

def Seaborn_demo_01(args):
	"""
	subplots: create a figure and a set of plots
	parameters:
	returns:
		fig: object
		ax: axes object
	This utility wrapper makes it convenient to create common layouts of subplots, 
	including the enclosing figure object, in a single call.
	"""
	fig, ax = plt.subplots()			# create a figure and a set of subplots
	"""
	read_csv: read comma-separated values from a file into pandas DataFrame
	parameters:
		filepath_or_buffer:	str, pathlib.Path
		object with a read method
		sep:		str, default=","
		delimiter:	str, default=None
		delim_whitespace:	bool, default=False
		header: 	int, list of ints, default="infer"
		names:		array-like, default=None
		index_col:	int or sequence, default=False
		usecols:	list-like, default=None
		and many more: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
	returns:
		result:		DataFrame or TextParser
	"""
	tips = pd.read_csv("tips.csv")		# data courtesy: https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
	"""
	violinplot:
	parameters:
		dataset: 	array or sequence of vectors
		positions: 	array-like, default=[1,2,...n]
		vert:		bool, default=True
		widths:		array-like, default=0.5
		showmeans: 	bool, default=False
		showextrema: bool, default=True
		showmedians: bool, default=False
		points: scalar, default=100
		bw_method: str, scalar or callable, optional
	returns:
		result: dict
	"""
	ax.violinplot(tips["total_bill"], vert=False) # violin plot
	"""
	set_window_title:
	"""
	fig.canvas.set_window_title("Demo 1: Hello Matplotlib")
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
	#plt.savefig("../images/demo_01.png")# for documentation use only
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
	sys.exit(Seaborn_demo_01(sys.argv))
