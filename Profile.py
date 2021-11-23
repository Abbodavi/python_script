#!/usr/bin/python3
import sys
import numpy as np

def get_aln(alnfile):
	d_aln={}
	f=open(alnfile)
	for line in f:
		if line[0:2]!="sp": continue
		l=line.split()
		sid=l[0]
		seq=l[1]
		d_aln[sid]=d_aln.get(sid,"")+seq
	return d_aln

def get_profile(d_aln):
	profile=[]
	n=len(list(d_aln.values())[0])
	sids=d_aln.keys()
	for i in range(n):
		aas=[]
		for j in sids:
			aas.append(d_aln[j][i])
		vaas=get_iprofile(aas)
		tot=float(vaas[:20].sum())
		for j in range(20):
			vaas[j]=vaas[j]/tot
		#print(i,aas,vaas)
		profile.append(vaas)
	return profile

def get_iprofile(ass,aa_list="ACDEFGHIKLMNPQRSTVWY-"):
	v=np.zeros(len(aa_list))
	for aa in ass:
		pos=aa_list.find(aa)
		if pos>-1: v[pos]+=1
	return v

def print_profile(profile,aa_list="ACDEFGHIKLMNPQRSTVWY-"):
	n=len(profile)
	for i in range(n):
		pi=profile[i][:20]
		s=0
		for j in range(20):
			if pi[j]>0: s=s-pi[j]*np.log(pi[j])
		#s=np.sum(-pi*np.log(pi))
		pm=pi.argmax()
		print(i,s,pi[pm],aa_list[pm],profile[i][20])

if __name__ == '__main__':
	alnfile=sys.argv[1]
	d_aln=get_aln(alnfile)
	#for sid in d_aln.keys():
	#	print (sid.split("|")[1],d_aln[sid])
	profile=get_profile(d_aln)
	print_profile(profile)