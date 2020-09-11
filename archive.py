from __future__ import division
from ROOT import *
from no_of_event import name_to_number
from optimization import optimize
import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt
if len(sys.argv)!=2:
    print "Usage: %s <Input File path>"%(sys.argv[0])
    sys.exit(1)

path = sys.argv[1]
files = [f for f in os.listdir(path) if f.endswith(".root")]

no_events,N_cmin,Npos_cmin,Nneg_cmin,Sum_cmin,Diff_cmin,Ncount_opt_wid,Npos_opt_wid,Nneg_opt_wid,Sum_opt_wid,Diff_opt_wid = np.empty((1), dtype="int32"), np.empty((1), dtype="float32"), np.empty((1), dtype="float32"), np.empty((1), dtype="float32"), np.empty((1), dtype="float32"), np.empty((1), dtype="float32"), np.empty((1), dtype="float32"), np.empty((1), dtype="float32"), np.empty((1), dtype="float32"), np.empty((1), dtype="float32"), np.empty((1), dtype="float32")

cwfile=TFile("cost-width.root","RECREATE")
treec=TTree("Mincost","Minimum Cost")
treew=TTree("Opt-wid","Optimum Width")
treec.Branch("NumOfEvents",no_events,"NumOfEvents/I")
treec.Branch("Ncount",N_cmin,"Ncount/F")
treec.Branch("Npos",Npos_cmin,"Npos/F")
treec.Branch("Nneg",Nneg_cmin,"Nneg/F")
treec.Branch("Npos+Nneg",Sum_cmin,"Npos+Nneg/F")
treec.Branch("Npos-Nneg",Diff_cmin,"Npos-Nneg/F")
treew.Branch("NumOfEvents",no_events,"NumOfEvents/I")
treew.Branch("Ncount",Ncount_opt_wid,"Ncount/F")
treew.Branch("Npos",Npos_opt_wid,"Npos/F")
treew.Branch("Nneg",Nneg_opt_wid,"Nneg/F")
treew.Branch("Npos+Nneg",Sum_opt_wid,"Npos+Nneg/F")
treew.Branch("Npos-Nneg",Diff_opt_wid,"Npos-Nneg/F")

for f in files:
    filepath = os.path.join(path, f)
    inFile = TFile.Open(filepath,"READ")
    print " Reading from", f
    tree = inFile.Get("treeA")
    n=name_to_number(f)
    # print n
    no_events[0]=n
    # print no_events[0]
    Ncount=tree.AsMatrix(columns=["Ncount"])
    Npos=tree.AsMatrix(columns=["fNtrackPos"])
    Nneg=tree.AsMatrix(columns=["fNtrackNeg"])
    Sum=Npos+Nneg
    Diff=abs(Npos-Nneg)
    inFile.Close()
    
    N_cmin[0],Ncount_opt_wid[0]=optimize(Ncount)
    
    Npos_cmin[0],Npos_opt_wid[0]=optimize(Npos)
    # print Npos_cmin[0],Npos_opt_wid[0]
    Nneg_cmin[0],Nneg_opt_wid[0]=optimize(Nneg)
    # print Nneg_cmin[0],Nneg_opt_wid[0]
    Sum_cmin[0],Sum_opt_wid[0]=optimize(Sum)
    # print Sum_cmin[0],Sum_opt_wid[0]
    Diff_cmin[0],Diff_opt_wid[0]=optimize(Diff)
    # print Diff_cmin[0],Diff_opt_wid[0]
    treec.Fill()
    treew.Fill()
    # break;

cwfile.Write()
print "--------------------Done-------------------------"