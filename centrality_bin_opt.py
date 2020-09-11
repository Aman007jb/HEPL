from ROOT import *
from ip_to_cen import ip_centrality_conversion
import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt
if len(sys.argv)!=2:
    print "Usage: %s <Input File path>"%(sys.argv[0])
    sys.exit(1)

inputfile = sys.argv[1]
inFile = TFile.Open(inputfile,"READ")
print "Reading from", inFile

ip=[]
tree = inFile.Get("treeA")
for entry in range(0,tree.GetEntries()):
    tree.GetEntry(entry)
    ip.append(getattr(tree,"fb"))

ip = np.array(ip)
cent_arr= ip_centrality_conversion(ip)
print cent_arr
max_ip = max(cent_arr)
min_ip = min(cent_arr)
N_bin = np.array(range(2,71))
width = (max_ip-min_ip)/N_bin
cost = np.zeros(shape=(np.size(width),1))


for i in range(np.size(N_bin)):
    hist,bin_edge=np.histogram(cent_arr,bins=N_bin[i])
    kmean=float(sum(hist)/N_bin[i])
    kvar=float(sum((hist[:]-kmean)**2)/N_bin[i])
    cost[i]=(2*kmean-kvar)/(width[i]**2)

min_cost = min(cost)
pos=np.where(cost==min_cost)
index=int(pos[0])
opt_ip_width=width[index]
opt_N_bin=N_bin[index]

plt.hist(cent_arr,bins=opt_N_bin,color='green',alpha=0.5,label='calculated bins ='+str(opt_N_bin),histtype='step')
plt.xlabel("ip")
plt.ylabel("particle count")
plt.title("impact distribution")
plt.legend()
plt.savefig("opt_cent.png")
plt.close()

print opt_ip_width
print "#############Done#############"