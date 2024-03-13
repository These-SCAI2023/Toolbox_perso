#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 12:09:59 2023

@author: antonomaz
"""


import csv
import glob

DATA_path = "../DATA/*.csv"




for file_path in glob.glob(DATA_path):
    liste_resultat=[]
    print(file_path)
    with open(file_path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar=' ')
        next(spamreader)
        
        for row in spamreader:
#            print(row[1])
            liste_resultat.append(row)
    liste_Hapax =[]
    liste_Freq =[]
    liste_VP_Hapax=[]
    liste_VP_Freq =[]
    liste_FP_Hapax=[]
    liste_FP_Freq =[]
    liste_AMB_Hapax=[]
    liste_AMB_Freq =[]
    
    for data in liste_resultat:
    #    print(data)
        if data[1] == "1":
    #        print(data)
            liste_Hapax.append(data)
        else:
            liste_Freq.append(data)
    
    for dt in liste_Hapax:
        if dt[2]=="VP":
            liste_VP_Hapax.append(dt)
            liste_VP_Freq.append(dt)
            
        if dt[2]=="AMBIG":
            liste_AMB_Hapax.append(dt)
            liste_AMB_Freq.append(dt)
            
        if dt[2]=="FP" or dt[2]=="PERS" or dt[2]=="EVENT" or dt[2]=="TIME":
            liste_FP_Hapax.append(dt)
            liste_FP_Freq.append(dt)
    for dt in liste_Freq:
        if dt[2]=="VP":
            liste_VP_Freq.append(dt)
            
        if dt[2]=="AMBIG":
            liste_AMB_Freq.append(dt)
            
        if dt[2]=="FP" or dt[2]=="PERS" or dt[2]=="EVENT" or dt[2]=="TIME":
            liste_FP_Freq.append(dt)
    
#    res_SEM=[]
#    res_stanza=[]
#    res_spacy=[]
#    
#    if version=="SEMWiNER":
#    if version == "stanza":
#    if version == "spaCy2.3.5-lg"
        
    print("\\begin{tabular}{|l|l|l|l|}")
    print("\\hline")
    print("&\multicolumn{3}{c|}{",f"{file_path}","}\\")
    print("\hline")
    print("VP hapax",len(liste_VP_Hapax))
    print("FP hapax",len(liste_FP_Hapax))
    print("Ambig hapax",len(liste_AMB_Hapax))
    print("VP type",len(liste_VP_Freq))
    print("FP type",len(liste_FP_Freq))
    print("Ambig type",len(liste_AMB_Freq))
        



   
                



