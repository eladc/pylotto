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

from math import sqrt 
from numpy import average
from itertools import groupby, count
from operator import itemgetter

#Various filters to use on draw results.

## Odd/Even 
def oddEven(ticket):
  count_odd, count_even = 0, 0
  for i in ticket:
    if i%2 != 0:
      count_odd += 1
    else:
      count_even += 1
  return count_odd, count_even

## Low/High
def lowHigh(ticket, maxNum): #maxNum is the highest ball number in pool
  count_low, count_high = 0, 0
  for i in ticket:
    if i <= (maxNum/2):
      count_low += 1
    else:
      count_high += 1
  return count_low, count_high

## Sum Range
def sumRange(ticket):
  return sum(ticket)

## Odd/Even Sum Range - checks if sum value is either odd(Flase) or even(True)
def sumRangeOddEven(ticket):
  if sum(ticket)%2 != 0:
    return False
  else:
    return True

## Sum Root - Sum root is a single digit number ranging from 1 to 9
def sumRoot(ticket):
  def sumdigits(value):
    return value and (value % 10 + sumdigits(value // 10))
  b = sumdigits(sum(ticket))      
  return sumdigits(b)

## Sum of Odd/Even Numbers
def sumOddEvenNums(ticket):
  sum_odd, sum_even = 0, 0
  for i in ticket:
    if i%2 != 0:
      sum_odd += i
    else:
      sum_even += i
  return sum_odd, sum_even

## Sum of Low/High Numbers
def sumlowHighNums(ticket, maxNum): #maxNum is the highest ball number in pool
  sum_low, sum_high = 0, 0
  for i in ticket:
    if i <= (maxNum/2):
      sum_low += i
    else:
      sum_high += i
  return sum_low, sum_high

## Sum's Last Digit - returns total sum's last digit
def sumLastDig(ticket):
  return sum(ticket)%10

## Digits Sum - The first digit is the leading digit of the number, the last digit is the second digit of the number
def digitsSum(ticket):
  last_dig, first_dig = 0, 0
  for i in ticket:
    last_dig += i%10
    first_dig += i/10
  return last_dig+first_dig
  
## Match Numbers - returns True for tickets that have the desired match of selected  numbers in match_list.
def matchNums(ticket, match_list, match):
  if len(set(ticket) & set(match_list)) <= match:
    return True

## Match Tickets in File - compare ticket with other tickets in a selected input_file(type:dictionary), returns True
# max_match - limits that maximum count of matching tickets
# min_match - limits that minimum count of matching tickets
# match - desired amount of matching numbers
# check - number of lines to check
def matchTickFile(ticket, input_file, max_match, min_match, match, check): 
  n, counter = 0,0
  while n < check:
    if len(set(ticket) & set(input_file[n])) == match:
      counter+=1
    n+=1
  if counter >= min_match and counter <= max_match:
    return True
 
## Match Numbers in File - needs to be implemented   

## Standard Deviation - a mathematical formula, which evaluates how close are the ticket numbers to each other
def stdDev(ticket):
  avg = average(ticket)
  variance = map(lambda x: (x - avg)**2, ticket)
  return sqrt(average(variance))

## Number Groups - how many numbers should be in each group. (1-10[group 1], 11-20[group 2], etc.). returns True.
def numGroups(ticket, group, grp_min, grp_max):
  dclist = [] ## decades counter list
  [dclist.append(num/10) for num in ticket]
  if dclist.count(group) >= grp_min and dclist.count(group) <= grp_max:
    return True

## Consecutive Numbers - finds numbers with the same delta(diff)
# diff - step 
# max_consc - maximum consecutives numbers (24,25 = 2)
# max_match - maximun match of consecutive numbers (3,4,11,14,15 = 2) 
def consecNums(ticket ,diff, max_consc, max_match):
  def _sub(item):
    a, b = item
    return a - b

  def consecutive(iterable, step):
    for _, g in groupby(zip(count(step=step), iterable), _sub):
      yield map(itemgetter(1), g)

  counter, bad_counter = 0, 0
  for j in (list(consecutive(ticket, diff))):
    if len(j) <= max_consc:
      counter += 1
    else:
      bad_counter += 1
  if counter <= max_match and bad_counter == 0:
    return True

## Consecutive First/Last Digits - count of consecutive last digits
def consecDigits(ticket, diff, max_consc, max_match):
  dig_list = []
  for i in ticket:
    dig_list.append(i%10)
  return consecNums(dig_list, diff, max_consc, max_match)













