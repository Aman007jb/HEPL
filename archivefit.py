from __future__ import division
from ROOT import *
from math import *
from no_of_event import name_to_number
import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt
if len(sys.argv)!=2:
    print "Usage: %s <Input File path>"%(sys.argv[0])
    sys.exit(1)

path = sys.argv[1]
files = [f for f in os.listdir(path) if f.endswith(".root")]
cmin=[]
optwidth=[]
no_events=[]
for f in files:
    filepath = os.path.join(path, f)
    inFile = TFile.Open(filepath,"READ")
    print " Reading from", f
    tree = inFile.Get("treeA")
    n=[]
    npos=[]
    nneg=[]
    npsum=[]
    npdiff=[]
    for entry in range(0, tree.GetEntries()):
        tree.GetEntry(entry)
        n.append(getattr(tree,"Ncount"))
        npos.append(getattr(tree,"fNtrackPos"))
        nneg.append(getattr(tree,"fNtrackNeg"))
        npsum.append(getattr(tree,"fNtrackPos")+getattr(tree,"fNtrackNeg"))
        npdiff.append(abs(getattr(tree,"fNtrackNeg")-getattr(tree,"fNtrackPos")))
    n=np.array(n)
    npos=np.array(npos)
    nneg=np.array(nneg)
    npsum=np.array(npsum)
    npdiff=np.array(npdiff)
    data=[n,npos,nneg,npsum,npdiff]
    minerr=[]
    minwid=[]
    print name_to_number(f)," events"
    no_events.append(name_to_number(f))
    for data_arr in data:
        
        mxp=max(data_arr)
        mnp=min(data_arr)
        N_bin=np.array(range(2,1001))
        width=float((mxp-mnp))/N_bin
        cost=np.zeros(shape=(np.size(width)))

        for i in range(np.size(N_bin)):
            hist,bin_edge=np.histogram(data_arr,bins=N_bin[i])
            kmean=float(sum(hist)/N_bin[i])
            kvar=float(sum((hist[:]-kmean)**2)/N_bin[i])
            cost[i]=(2*kmean-kvar)/(width[i]**2)
        
        # plt.plot(width,cost)
        min_cost = min(cost)
        pos=np.where(cost==min_cost)
        index=int(pos[0])
        opt_width=width[index]
        opt_N_bin=N_bin[index]
        minwid.append(opt_width)
        minerr.append(min_cost)
    cmin.append(minerr)
    optwidth.append(minwid)
    inFile.Close()

print cmin,optwidth