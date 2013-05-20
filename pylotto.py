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

import fileDl,loadRes
from Stats import *
from os import chdir
from sys import argv,exit

__version__ = 'v1.02'
__Author__ = 'Elad Cohen'

## CL usage message
def usage():
  print 'pylotto' , __version__ ,': invalid argument.\n', 
  print 'Usage:   pylotto.py 777\n         pylotto.py Lotto'
  return 0

## CL arguments
def parseArgs(): 
  if len(argv)<2:
    usage()
  elif argv[1] == '777' or argv[1] == 'Lotto':
    return argv[1]
  else:
    usage()

## Main 
def main(draw_type):
  if not draw_type:  # exit if arguments are wrong
    return 0  
  
  update  = raw_input(r'Do you want to update the draw results file? (Y\n): ')
  if update == 'Y': 
    fileDl.fChk(draw_type) #check for updated results file
  elif update != 'n':
    print "Invalid choice, Exiting..."
    return 0
  else:
    chdir(draw_type) # change directory to the selected draw

  draw = loadRes.readRes(draw_type) #load results from csv file
  print 'Latest draw loaded:' , draw.results[0][0]
  print 'Latest draw results:' 
  for i  in draw.results[0][1:]:
    print i, '-',
  
  print '\nWriting draw statistics... (draw_stats.csv)'
  print 'Writing ball statistics... (ball_stats.csv)'
  writeStats(draw_type, draw.results) # write statistics to a csv file
  print 'Done.'

if __name__== '__main__':
  args = parseArgs()
  exit(main(args))
