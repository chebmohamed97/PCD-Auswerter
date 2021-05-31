import pandas as pd
import numpy as np
from tkinter import filedialog
from tkinter import *
import os
from os.path import isfile, join
import matplotlib.pyplot as plt
from math import atan,pi



    

def plot_dist(file_path,selected_file):
    path=file_path +'\\'+ selected_file
    points=read_file(path)
    xvalues=[]
    for i in range(len(points)):
        xvalues.append(points[i].x)
    x = np.asarray(xvalues, dtype=np.float32)    
    plt.hist(x)
    plt.gca().set_title('Distance Histogramm',loc='left')
    plt.axvline(x.mean(), color='k', linestyle='dashed', linewidth=1)
    min_ylim, max_ylim = plt.ylim()
    plt.text(x.mean()*1, max_ylim*1.01, 'Mean: {:.2f}'.format(x.mean()))
    plt.show()  






class point:
    # Define an object Point that contains the point's coordinates and intensity
    def __init__(self,x,y,z,intensity):
        self.x=x
        self.y=y
        self.z=z
        self.intensity=intensity
        if (x != 0):
            self.new_int=((x*x+y*y+z*z)/(x*x))*intensity
 

def read_file(path):
    #function to read the data from file and save it into a list of points
    liste=[]
    f1=pd.read_csv(path,sep=' ',header = None,names=['X','Y','Z','Intensity'])

    i=0
    while(i<len(f1)):        
        x_value=float(f1.iloc[i]['X'])
        y_value=float(f1.iloc[i]['Y'])
        z_value=float(f1.iloc[i]['Z'])
        intensity_value=float(f1.iloc[i]['Intensity'])
        liste.append(point(x_value,y_value,z_value,intensity_value) )
        i=i+1
    
    return liste

def get_neighbour(liste,y_start,abstand):                             
    #function to get the neighbor points to a certain point
    ymax= y_start + abstand + abstand/2
    ymin= y_start - abstand/2
    new_points=[]
    for i in range(0, len(liste)):
        if(liste[i].y < ymax and liste[i].y > ymin):
            new_points.append(i)
    
    return new_points

def find_start_point(liste):
    #get the index of the point with minimal y-value (farthest point on the left) and the index of the 
    # point with maximal y-value (farthest point on the right)
    i=0
    y_list=[]
    while(i<len(liste)):        
        y_list.append(liste[i].y )
        i=i+1
    return y_list.index(min(y_list)),y_list.index(max(y_list))

def get_koord(liste,indexes):
    #get the coordinates of certain points from their indexes
    xvalues=[]
    yvalues= []
    zvalues= []
    intvalues=[]
    new_intvalues=[]
    for i in range(0,len(indexes)):
        xvalues.append(liste[indexes[i]].x)
        yvalues.append(liste[indexes[i]].y)
        zvalues.append(liste[indexes[i]].z)
        intvalues.append(liste[indexes[i]].intensity)
        new_intvalues.append(liste[indexes[i]].new_int)
    return xvalues,yvalues,zvalues,intvalues,new_intvalues

def get_mean(xvalues,yvalues,zvalues,intvalues):
    #get the mean value of a list / array (in this case mean of x y z int values)
    x_mean = np.mean(np.asarray(xvalues, dtype=np.float32))
    #y_mean = np.mean(np.asarray(yvalues, dtype=np.float32))
    #z_mean = np.mean(np.asarray(zvalues, dtype=np.float32))
    int_mean = np.mean(np.asarray(intvalues, dtype=np.float32))
    return x_mean,int_mean

def get_std(xvalues,yvalues,zvalues,intvalues):
    #get the std value of a list / array (in this case std of x y z int values)
    x_std = np.std(np.asarray(xvalues, dtype=np.float32))
    #y_mean = np.mean(np.asarray(yvalues, dtype=np.float32))
    #z_mean = np.mean(np.asarray(zvalues, dtype=np.float32))
    int_std = np.std(np.asarray(intvalues, dtype=np.float32))
    return x_std,int_std