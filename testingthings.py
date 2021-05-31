import pandas as pd
import numpy as np
from math import atan,pi
path='C:/Users/m.chebaane/Desktop/Testfiles/white wall.csv'

h_res=0.45
v_res=0.2
number_of_frames=10
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

print(path)
points=read_file(str(path))
xvalues=[]
yvalues=[]
zvalues=[]
inttvalues=[]
for i in range(len(points)):
    xvalues.append(points[i].x)
    yvalues.append(points[i].y)
    zvalues.append(points[i].z)
    inttvalues.append(points[i].intensity)
    
x = np.asarray(xvalues, dtype=np.float32)
y = np.asarray(yvalues, dtype=np.float32)
z = np.asarray(zvalues, dtype=np.float32)
intt = np.asarray(inttvalues, dtype=np.float32)
numberofpoints=len(x)
target_h = np.max(y) - np.min(y)                                
alpha = (atan(target_h / np.mean(x)))*(180/pi) 
pxl_soll_h = np.ceil(alpha / h_res)   +1                        

target_v = np.max(z) - np.min(z)
alpha2 = (atan(target_v / np.mean(x)))*(180/pi) 
pxl_soll_v = np.ceil(alpha2 / v_res)  +1                          
pxl_soll = pxl_soll_h * pxl_soll_v                                

detect_prob = (numberofpoints/number_of_frames) / pxl_soll 

calcul = {'Number of points in File': [numberofpoints],'Farthest detected Point':[np.max(x)],
       'Nearest detected Point': [np.min(x)],'Mean of Distance values':[np.mean(x)],
       'Distance Median': [np.median(x)],'Standard Deviation of Distance values':[np.std(x)],
       'Highest Intensity value': [np.max(intt)],'Lowest Intensity value':[np.min(intt)],
       'Mean of Intensity': [np.mean(intt)],'Intensity Median':[np.median(intt)],
       'Standard Deviation of Intensity': [np.std(intt)],'Calculated number of h-Pixels':[pxl_soll_h],
       'Calculated number of v-Pixels': [pxl_soll_v],'Calculated number of Pixels per Frame':[pxl_soll],
       'Number of Pixels per Frame': [np.ceil(numberofpoints/number_of_frames)],
       'Detection Propability (%)': [np.round(detect_prob * 100)] }
df = pd.DataFrame(calcul)
print(df)