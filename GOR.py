# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:35:43 2020

@author: david
"""

import sys, getopt, os
import numpy as np

def get_file(argv):
    try:
        opts, args = getopt.getopt(argv, 'p:s:o:', ['profile=','secondary=','output='])
        for opt, arg in opts:
            if opt in ("-p","--profile"):
                profile=arg
            elif opt in ("-s", "--secondary"):
                secondary=arg
            elif opt in ("-o", "--output"):
                output_file=arg
    except getopt.GetoptError:
        print("Invalid argument")
        sys.exit(2)
    return profile, secondary, output_file

def GOR(profile, SS,C,H,E):
    SS_file=open(SS,"r")
    #print(profile)
    profile_matrix=np.loadtxt(profile, skiprows=1, usecols=range(1,21))
    #profile_matrix=np.loadtxt(profile, skiprows=1)

    for line in SS_file:
        if line[0]!=">":
            Structure=line.strip()
    i=0
    v=0
    for chr in Structure:
        #print(chr)
        start = max(0, i-8)
        end = min(len(Structure), i+9)
        if v<8:
            point=(17-len(Structure[start:end]))  ##Set to a variable for the window
            v+=1
        else:
            point=0
        if chr in ("-", "C"):
            for row in range(start,end):
                C_matrix[point]=np.add(C_matrix[point],profile_matrix[row])
                total[point]=np.add(total[point],profile_matrix[row])
                point+=1
            C+=1
        elif chr in ("H"):
            for row in range(start,end):
                H_matrix[point]=np.add(H_matrix[point],profile_matrix[row])
                total[point]=np.add(total[point],profile_matrix[row])
                point+=1
            H+=1
        elif chr in ("E"):
            for row in range(start,end):
                E_matrix[point]=np.add(E_matrix[point],profile_matrix[row])
                total[point]=np.add(total[point],profile_matrix[row])     
                point+=1
            E+=1
        i+=1
    return C,H,E


def normalize(C_matrix,H_matrix,E_matrix,total):
    total_N=np.sum(total,axis=1)
    for i in range(len(total_N)):
        C_matrix[i]= np.divide(C_matrix[i],total_N[i])
        H_matrix[i]= np.divide(H_matrix[i],total_N[i])
        E_matrix[i]= np.divide(E_matrix[i],total_N[i])
    

    
def information(C_matrix,H_matrix,E_matrix,total_matrix,C_count,H_count,E_count):
    total=C_count+H_count+E_count
    C_count=C_count/total
    H_count=C_count/total
    E_count=C_count/total
    info_C=np.zeros((17, 20))
    info_H=np.zeros((17, 20))
    info_E=np.zeros((17, 20))
    i=0
    for (a, b, c, d) in zip(C_matrix,H_matrix,E_matrix, total_matrix):
        div_C=np.multiply(total_matrix[i],C_count)
        div_H=np.multiply(total_matrix[i],H_count)
        div_E=np.multiply(total_matrix[i],E_count)
        to_log_C=np.divide(a,div_C)
        to_log_H=np.divide(b,div_H)
        to_log_E=np.divide(c,div_E)
        info_C[i]=np.log(to_log_C)
        info_H[i]=np.log(to_log_H)
        info_E[i]=np.log(to_log_E)
        i+=1
    #info_H=info_H[info_H== np.NINF] = 0
    #info_C=info_C[info_C== np.NINF] = 0
    #info_E=info_E[info_E== np.NINF] = 0
    return info_C,info_H,info_E
    
    
if __name__=="__main__":
    profile, secondary, output = get_file(sys.argv[1:])
    C_matrix=np.zeros((17, 20))
    H_matrix=np.zeros((17, 20))
    E_matrix=np.zeros((17, 20))
    total=np.zeros((17,20))
    C=0
    H=0
    E=0
    #print(C_matrix)
    for file in os.listdir(profile):
        name=os.path.splitext(file)[0]
        name=os.path.splitext(name)[0]
        #print(name) #Da cambiare per evitare che perda i file con un punto nel nome
        SS_file= secondary + name + ".dssp"
        Profile_file = profile + name + ".psiblast.profile"
        C,H,E=GOR(profile+file, SS_file,C,H,E)
    normalize(C_matrix,H_matrix,E_matrix,total)
    Coil,Helix,Strand=information(C_matrix,H_matrix,E_matrix,total,C,H,E)
    print(Helix)

    #np.savetxt(output+'E_matrix.csv', E_matrix, delimiter=',')
    #np.savetxt(output+'H_matrix.csv', H_matrix, delimiter=',')
    #np.savetxt(output+'C_matrix.csv', C_matrix, delimiter=',')
    #np.savetxt(output+'total.csv',C_matrix, delimiter=',')