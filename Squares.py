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

# a class to search which balls appeared in each square(1 to 17) of the results list.

class square:
  def __init__(self, draws, max_ball, max_draws):
    self.draws = draws
    self.max_draws = max_draws
    self.max_ball = max_ball
    
  def calc(self, col):
    if self.max_draws > 31:
      self.max_draws = 31 # limit max_draws to 31, an efficient number of draws to load for this algorithm
    
    tmpSqrList = []
    sqrList = []
    for y in range(0, self.max_draws): # iterate through lines
      tmpSqrList.append(self.draws[y][col]) # temp list to append all nums in a single column
 
    for i in range(1, self.max_ball+1): 
      count = tmpSqrList.count(i) # count all the numbers from the temp list
      if count > 1: 
        sqrList.append(i) # append to new list if count > 1
    return sqrList
     
