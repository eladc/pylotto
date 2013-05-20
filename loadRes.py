#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
#
#    Copyright 2013 Elad Cohen <eladco@gmail.com>
##########################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##########################################

import csv

## Load the results CSV file in to a dictionary (self.results).

class readRes:
  def __init__(self, draw):
    if draw == '777': # check draw type
      fname = '777.csv'
      lcol = 19 # last column to load
      draw_num = 1 #draw number
    else:
      fname = 'Lotto.csv'  
      lcol = 8 
      draw_num = 0 
    fcol = 2 

    reader = csv.reader(open(fname, 'rb'), delimiter=',', quotechar='"') #load csv file to a variable
    skip = int(raw_input('How many first lines to skip?: '))
    load = int(raw_input('How many draws do you want to load?: '))
    print 'Loading next %d lines...' % load
    n = 0
    m = -1
    self.results = {}

    for line in reader: 
      if (m < skip):
        m += 1
      else:
        self.results[n] = [int(i) for i in line[fcol:lcol]] #copy each line to a new list of integers
        self.results[n].insert(0, line[draw_num]) # insert draw number to the list
        n += 1
        if ( n == load): #loading new line stops when condition is true.
          break

	

