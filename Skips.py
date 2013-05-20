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

# Calculate ball skips, return skips in a dictionary

class skipCtr:
  def __init__(self, max_ball, draw, max_draws): # Search for number of skips for each ball
  
    self.skip = {}
    for num in range(1, max_ball+1):
      self.skip[num] = []
      skipctr = 0
      
      for i in range(0, max_draws): # iterate through range 1 - max_draws
        if num in draw[i]:
          self.skip[num].append(skipctr) # append to skip list if true
          skipctr = 0
        else:
          skipctr += 1        

      self.skip[num].append(skipctr)

