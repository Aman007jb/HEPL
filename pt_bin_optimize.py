from __future__ import division
from ROOT import *
from no_of_event import name_to_number
from optimization import optimize,fit
from scipy.optimize import curve_fit 
# from math import round
import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt
if len(sys.argv)!=2:
    print "Usage: %s <Input File path>"%(sys.argv[0])
    sys.exit(1)

path = sys.argv[1]
files = [f for f in os.listdir(path) if f.endswith("pT.root")]
data_pt=[]
for f in files:
    filepath = os.path.join(path, f)
    inFile = TFile.Open(filepath,"READ")
    tree = inFile.Get("newtree")
    # fpt=np.squeeze(tree.AsMatrix(exclude=["ntrak"]))
    event=np.squeeze(tree.AsMatrix(columns=["ntrak"]))
    fpt=np.asarray([[np.asarray(tree.fPt)] for event in tree])
events=fpt.size
print events
pt=np.squeeze(fpt)
for i in pt:
    for j in i:
        data_pt.append(j)

data_pt=np.asarray(data_pt)
print data_pt
pt_cmin,opt_pt_wid,opt_pt_bin=optimize(data_pt,events)
print pt_cmin,opt_pt_wid,opt_pt_bin
hist,bin_edge=np.histogram(data_pt,bins=opt_pt_bin)
hist=np.array(hist)
hist=[double(i/events) for i in hist]
width = (bin_edge[1] - bin_edge[0])
center = (bin_edge[:-1] + bin_edge[1:]) / 2
center=np.array(center)
test=np.zeros(shape=(np.size(center)))
for i in range(len(center)):
    test[i]=hist[i]/center[i]
# data=np.array(data)
param, param_cov = curve_fit(fit, center, test)
print "params",param
print "params_cov", param_cov

ans = [fit(i,param[0],param[1],param[2]) for i in center]
plt.yscale("log")
plt.bar(center,test,align='center', width=width,log=False,label=str(len(center)))
plt.plot(center,ans,label="fit",color="red")
plt.xlabel("pT")
plt.ylabel("particle count per event")
plt.title("pT distribution for"+str(events)+"events")
plt.legend()
plt.savefig("pt_bin_newpt_5k.eps")
plt.close()