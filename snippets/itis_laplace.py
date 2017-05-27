# script for generating whole number ITI's that sum to a given run length
# a bit useless b/c we now use optseq2
#
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:05:57 2013

@author: Vaida Rimeikyte
"""

#add the libraries you will be using
import numpy as np
from scipy import stats

#define some vars
num_itis = 31 #the number of itis you need to draw
num_runs = 3 #the number of iti lists you will need 

"""
now to determine the total time I will want my itis to sum up to, I generally 
pull a bunch of them and calculate the stats

"""
sums = []
i=0

while i<10000:
    itis = stats.dlaplace.rvs(1, loc=3, scale=1, size=num_itis) #a discrete laplacian distribution, with mean 3
    a=np.clip(itis,2,8) #replace values <2 with 2 and >8 with 8
    sums.append(sum(a))
    i+=1

print 'mean sum = %.2f, median sum = %d'%(np.mean(sums),np.median(sums))

"""
I usually start with median and fiddle if I'm unhappy -- higer sums will generate 
distributions with longer ITIs 
"""


total_time = raw_input('Enter the Total ITI Time: ')

if not total_time.isdigit():
    print 'please try again, this time with numbers' 
else:
    total_time = int(total_time)
    i=0
    durs = []
    count = 0
    while i<10000 and count<num_runs:
        itis = stats.dlaplace.rvs(1, loc=3, scale=1, size=num_itis)
        a=np.clip(itis,2,8)
        if sum(a) == total_time:
            durs.append(a)
            count+=1
        i+=1
        
    if count == num_runs:
        for dur in durs:
            for num in dur:
                print num
            print '*******'
    else:
        print 'Could not find a distribution of ITIs that sumed up to the given Total ITI time.'
