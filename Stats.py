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

from Filters import *
import Squares
import Skips
import csv

# Write statistics to CSV files.

def kenoSqrFilter(sqrs): # count total number of ball appearance
  calcDict = {} # A dictionany of balls appearances in each spot (1 to 17)
  nums = {} # A dictionary of 70 balls
  
  for i in range(1, 71):
    nums[i] = 0 # reset value of each list in the dictionary
  
  n = 1
  for j in range(1, 18): # iterate through columns
    calcDict[j] = sqrs.calc(j) # call calc funtion 
    for k in range(1, 71): # iterate through balls
      if k in calcDict[n]: # add 1 to count for each ball if its in the calcDict
        nums[k]+=1 
    n += 1
    
  sqr_list = []
  for h in range(1, 71): 
    if nums[h] > 1: # find if a ball has an overall count of >1 and append to list
      sqr_list.append(h) 
      
  return str(sqr_list), len(sqr_list)


def writeStats(dtype, results):
  # determine draw type
  if dtype == '777':
    max_num = 70
  else:
    max_num = 37
  k=0 # count number of lines
  
###################
# Write draw statistics 

  lines = csv.writer(open('draw_stats.csv','wb'),delimiter=',')  
  first_line = ['Draw','Ticket','OddEven','LowHigh','Sum','SumOddEven','SumRoot','SumOENums','SumLHNums','SumLastDig','DigitSum','StdDev']
  lines.writerow(first_line)

  for line in results:
    a = results[k][1:]
    draw_num = results[k][0]
    b =[draw_num, a, oddEven(a), lowHigh(a, max_num), sumRange(a), sumRangeOddEven(a), sumRoot(a), sumOddEvenNums(a), sumlowHighNums(a, max_num), sumLastDig(a), digitsSum(a), stdDev(a)]
    lines.writerow(b)  # write statistics to draw_stats
    k+=1 # last iteration will be the maximum line number

###################
# Write ball statistics 

  skipper = Skips.skipCtr(max_num, results, k) #create skip object
  lines = csv.writer(open('ball_stats.csv','wb'),delimiter=',')  
  first_line = ['Ball','Skip 1','Skip 2','Skip 3','Skip 4','Skip 5','5 Skips Sum','Skip Average']
  lines.writerow(first_line)
  ball = 1
  skp = skipper.skip
  for key in skp:
    avg = (sum(skp[key])/len(skp[key])) # skip average
    lst5skps = sum(skp[key][0:5]) # skip sum

    if len(skp[key]) < 5: # check for empty indexes 
      length = len(skp[key])
      while length < 5:
        skp[key].append(None)
        length += 1

    balls = [ball, skp[key][0], skp[key][1], skp[key][2], skp[key][3], skp[key][4], lst5skps,avg]
    lines.writerow(balls)
    ball+=1

####################
# look for ball appearance in each square
  
  if dtype == '777': # Special 777 algorithm
    fname = open('777_numbers.txt','wb')
    sqr = Squares.square(results, max_num, k) # create square object
    sqr_list, sqr_length = kenoSqrFilter(sqr)
    fname.write(sqr_list)
    print 'A total of %d possible numbers has been written to 777_numbers.txt' % sqr_length

