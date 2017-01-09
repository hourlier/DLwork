import ROOT
from ROOT import *
from larcv import larcv

ch=TChain("image2d_tpc_tree")
ch.AddFile("DataFiles/larcv_extBNB9131runs_cosmic_trained_only_on_mc_pscore_0.99_1598evts_23aug2016.root")

Nentries = ch.GetEntries()
print Nentries, "entries found"

evt=0
while evt < Nentries:
    ch.GetEntry(evt)
    print evt,"/",Nentries
    evt+=1

print "done"
