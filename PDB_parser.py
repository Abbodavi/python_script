#!/usr/bin/python3
import sys
import numpy as np
from Bio.SVDSuperimposer import SVDSuperimposer

def get_ca_atoms(pdbfile,chain,rlist,atom="CA"):
	l_coord=[]
	fpdb=open(pdbfile)
	for line in fpdb:
		if line[:4]!="ATOM": continue
		if line[21]!=chain: continue
		if line[22:26].strip() not in rlist: continue
		if line[12:16].strip() !=atom: continue
		x=float(line[30:38])
		y=float(line[38:46])
		z=float(line[46:54])
		l_coord.append([x,y,z])
	return l_coord

def get_rmsd(coord1,coord2):
	if len(coord1)!=len(coord2):
		print("ERROR: THe set of coordinates have different size", file =sys.stderr)
		sys.exit()
	svd=SVDSuperimposer()
	svd.set(np.array(coord1),np.array(coord2))
	svd.run()
	rmsd=svd.get_rms()
	rot,tran=svd.get_rotran()
	print(rot)
	print(tran)
	return rmsd

if __name__=="__main__":
	pdbfile1=sys.argv[1]
	pdbfile2=sys.argv[2]
	chain1=sys.argv[3]
	chain2=sys.argv[4]
	list1=sys.argv[5].split(',')
	list2=sys.argv[6].split(',')
	lcord1=get_ca_atoms(pdbfile1,chain1,list1)
	lcord2=get_ca_atoms(pdbfile2,chain2,list2)
	#print("cord1=", lcord1)
	#print("cord2=", lcord2)
	rmsd=get_rmsd(lcord1,lcord2)
	print(rmsd)
	#print(pdbfile1, pdbfile2, chain1, chain2, list1, list2)