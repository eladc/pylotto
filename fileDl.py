#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
#
#    Elad Cohen <eladco@gmail.com> 
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

import requests
import os

## Download latest results.

def csvDl(u, file_size, file_name):

    print "Downloading: %s - %s" % (file_name, file_size)

    with open(file_name, 'wb') as f:
        for chunk in u.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    f.close)

def fChk(draw): # check for an updated csv
    print 'Checking for updated csv file...'
    os.chdir(draw)
    fname = '%s.csv' % draw

    old_f_size = os.path.getsize(fname)  # get the file size of an existing csv 

    url = 'http://www.pais.co.il/%s/Pages/last_Results.aspx?download=1' % draw

    u = requests.get(url)
    file_size = int(u.headers['content-length'])

    if old_f_size == file_size: # compare size of existing file with downloadable file
        print 'You have the latest version, no update needed.'
    else:
        csvDl(u, file_size, fname)

