from __future__ import division
import numpy as np
def optimize(data,events):
    # print data,events   
    mxp=max(data)
    mnp=min(data)
    N_bin=np.array(range(2,1001))
    width=(mxp-mnp)/N_bin
    cost=np.zeros(shape=(np.size(width),1))

    for i in range(np.size(N_bin)):
        hist,bin_edge=np.histogram(data,bins=N_bin[i])
        hist=hist[:]/events
        kmean=float(sum(hist)/N_bin[i])
        kvar=float(sum((hist[:]-kmean)**2)/N_bin[i])
        cost[i]=(2*kmean-kvar)/(width[i]**2)
    
    # print cost
    # plt.plot(width,cost)
    min_cost = min(cost)
    # print min_cost
    pos=np.where(cost==min_cost)
    index=int(pos[0])
    print pos,index
    opt_width=width[index]
    opt_N_bin=N_bin[index]
    return min_cost,opt_width,opt_N_bin

def fit(pt,C,q,T):
    # pt=np.array(pt)
    x=0.0
    if (1-q)!=0:
        x=float(q/(1-q))
    return C*pt*(1+((q-1)*(pt/T)))**x