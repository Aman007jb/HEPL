import numpy as np
def optimize(data):    
    mxp=max(data)
    mnp=min(data)
    N_bin=np.array(range(2,1001))
    width=float((mxp-mnp))/N_bin
    cost=np.zeros(shape=(np.size(width)))

    for i in range(np.size(N_bin)):
        hist,bin_edge=np.histogram(data,bins=N_bin[i])
        kmean=float(sum(hist)/N_bin[i])
        kvar=float(sum((hist[:]-kmean)**2)/N_bin[i])
        cost[i]=(2*kmean-kvar)/(width[i]**2)
    
    # plt.plot(width,cost)
    min_cost = min(cost)
    pos=np.where(cost==min_cost)
    index=int(pos[0])
    opt_width=width[index]
    opt_N_bin=N_bin[index]
    return min_cost,opt_width