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

import urllib2
import os

## Download latest results.

def csvDl(file_name, uRL):

  u = urllib2.urlopen(uRL)
  f = open(file_name, 'wb')
  meta = u.info()
  file_size = int(meta.getheaders('Content-Length')[0])
  print 'Downloading: %s Bytes: %s' % (file_name, file_size)

  file_size_dl = 0
  block_sz = 8192
  while True:
      buffer = u.read(block_sz)
      if not buffer:
        break

      file_size_dl += len(buffer)
      f.write(buffer)
      status = r'%10d  [%3.2f%%]' % (file_size_dl, file_size_dl * 100. / file_size)
      status = status + chr(8)*(len(status)+1)
      print status,

  f.close()

def fChk(draw): #check for an updated csv
  print 'Checking for updated csv file...'
  os.chdir(draw)
  fname = '%s.csv' % draw
  old_f_size = os.path.getsize(fname)  #get the file size of an existing csv 

  url = 'http://www.pais.co.il/%s/Pages/last_Results.aspx?download=1' % draw

  u = urllib2.urlopen(url)
  meta = u.info()
  file_size = int(meta.getheaders('Content-Length')[0])

  if old_f_size == file_size: # compare size of existing file with downloadable file 
    print 'You have the latest version, no update needed.'
  else:
    csvDl(fname, url)

