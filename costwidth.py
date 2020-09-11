from ROOT import *
import sys
import numpy as np
import matplotlib.pyplot as plt
if len(sys.argv)!=2:
    print "Usage: %s <Input File path>"%(sys.argv[0])
    sys.exit(1)

fil=sys.argv[1]
inf=TFile(fil,"READ")
t1=inf.Get("Mincost")
t2=inf.Get("Opt-wid")
Events=t2.AsMatrix(columns=["NumOfEvents"])
Ncw=np.squeeze(t2.AsMatrix(columns=["Ncount"]))
Npw=np.squeeze(t2.AsMatrix(columns=["Npos"]))
Nnw=np.squeeze(t2.AsMatrix(columns=["Nneg"]))
Sw=np.squeeze(t2.AsMatrix(columns=["Npos+Nneg"]))
Dw=np.squeeze(t2.AsMatrix(columns=["Npos-Nneg"]))
Nc_wid,Np_wid,Nn_wid,S_wid,D_wid=np.zeros((np.size(Events)), dtype="float32"),np.zeros((np.size(Events)), dtype="float32"),np.zeros((np.size(Events)), dtype="float32"),np.zeros((np.size(Events)), dtype="float32"),np.zeros((np.size(Events)), dtype="float32")
name=["Nc_wid","Np_wid","Nn_wid","S_wid","D_wid"]
x=np.squeeze(Events)
i=np.argsort(x)
k=0
print  i
file1= open("cost_width.txt","w")
head=["Events \t","Nc_wid \t","Np_wid \t","Nn_wid \t","S_wid \t","D_wid"]
file1.writelines(head)
for j in i:
    file1.write("\n")
    Nc_wid[k]=Ncw[j]
    Np_wid[k]=Npw[j]
    Nn_wid[k]=Nnw[j]
    S_wid[k]=Sw[j]
    D_wid[k]=Dw[j]
    line=[str(x[j]),"\t",str(Nc_wid[k]),"\t",str(Np_wid[k]),"\t",str(Nn_wid[k]),"\t",str(S_wid[k]),"\t",str(D_wid[k])]
    file1.writelines(line)
    k+=1
file1.close()
data=[Nc_wid,Np_wid,Nn_wid,S_wid,D_wid]
x=np.sort(x)
for i in range(0,len(data)):
    plt.xscale("log")
    plt.plot(x,data[i],label=str(name[i]),marker="*",linestyle='dashed', linewidth = 2, markerfacecolor='blue', markersize=12)
    plt.legend()
    plt.savefig(str(name[i])+".png")
    plt.close()