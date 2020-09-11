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
files = [f for f in os.listdir(path) if f.endswith("pT.root")]
nt=[]
pt=[]
for f in files:
    filepath = os.path.join(path, f)
    inFile = TFile.Open(filepath,"READ")
    # print " Reading from", f
    tree = inFile.Get("newtree")
    for entry in range(0, tree.GetEntries()):
        tree.GetEntry(entry)
        # px=(getattr(tree,"px"))
        # py=(getattr(tree,"py"))
        ntrak=getattr(tree,"ntrak")
        fpt=getattr(tree,'fPt')
        nt=[fpt[i] for i in range(0,ntrak)]
        pt=np.concatenate((pt,nt))
    inFile.Close()
events = entry +1
print events
mxp=max(pt)
mnp=min(pt)
N_bin=np.array(range(2,1001))
width=(mxp-mnp)/N_bin
cost=np.zeros(shape=(np.size(width),1))

for i in range(np.size(N_bin)):
    hist,bin_edge=np.histogram(pt,bins=N_bin[i])
    hist = hist[:]/events
    kmean=float(sum(hist)/N_bin[i])
    kvar=float(sum((hist[:]-kmean)**2)/N_bin[i])
    cost[i]=(2*kmean-kvar)/(width[i]**2)

min_cost = min(cost)
pos=np.where(cost==min_cost)
index=int(pos[0])
opt_width=width[index]
opt_N_bin=N_bin[index]
hist,bin_edge=np.histogram(pt,bins=opt_N_bin)
hist=np.array(hist)
# print hist
hist=[double(i/events) for i in hist]
# print hist
width = (bin_edge[1] - bin_edge[0])
center = (bin_edge[:-1] + bin_edge[1:]) / 2
# width=np.log10(width)
# center=np.log10(center)
# print hist
plt.yscale("log")
# plt.xscale("log")
plt.bar(center,hist,align='center', width=width,log=False,label=str(len(center)))
plt.xlabel("pT")
plt.ylabel("particle count per event")
plt.title("pT distribution for"+str(events)+"events")
plt.legend()
# plt.show()
plt.savefig("optbin_newpt_5k.eps")
plt.close()

plt.hist(pt,bins=opt_N_bin,color='green',alpha=0.5,label='calculated bins ='+str(opt_N_bin),histtype='step')
plt.xlabel("pT")
plt.ylabel("particle count")
plt.title("pT distribution")
plt.yscale("log")
plt.legend()
plt.savefig("optbin_pt.png")
plt.close()
print "#############Done#############"