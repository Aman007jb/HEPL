from __future__ import division
from ROOT import *
from math import *
import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt
if len(sys.argv)!=2:
    print "Usage: %s <Input File path>"%(sys.argv[0])
    sys.exit(1)

path = sys.argv[1]
files = [f for f in os.listdir(path) if f.endswith(".root") and f.startswith("event")]
pt=[]
for f in files:
    filepath = os.path.join(path, f)
    inFile = TFile.Open(filepath,"READ")
    # print " Reading from", f
    tree = inFile.Get("particles")
    for entry in range(0, tree.GetEntries()):
        tree.GetEntry(entry)
        px=(getattr(tree,"px"))
        py=(getattr(tree,"py"))
        pt.append(sqrt(px**2+py**2))
    inFile.Close()
pt=np.array(pt)
mxp=max(pt)
mnp=min(pt)
N_bin=np.array(range(2,1001))
width=float((mxp-mnp)/N_bin)
cost=np.zeros(shape=(np.size(width),1))

for i in range(np.size(N_bin)):
    hist,bin_edge=np.histogram(pt,bins=N_bin[i])
    kmean=float(sum(hist)/N_bin[i])
    kvar=float(sum((hist[:]-kmean)**2)/N_bin[i])
    cost[i]=(2*kmean-kvar)/(width[i]**2)

min_cost = min(cost)
pos=np.where(cost==min_cost)
index=int(pos[0])
opt_width=width[index]
opt_N_bin=N_bin[index]

plt.hist(pt,bins=opt_N_bin,color='green',alpha=0.5,label='calculated bins ='+str(opt_N_bin),histtype='step')
plt.xlabel("pT")
plt.ylabel("particle count")
plt.title("pT distribution")
plt.legend()
plt.savefig("optbin.png")
plt.close()

print "#############Done#############"