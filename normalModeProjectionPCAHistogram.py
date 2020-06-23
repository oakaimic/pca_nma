import numpy
from operator import itemgetter
from mpl_toolkits.mplot3d import Axes3D
import mdtraj as md
import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
import pylab
import seaborn as sns
import os
import argparse
import numpy as np
from matplotlib import mlab
from matplotlib import rcParams


def cosine_similarity(vec1, vec2):
	num=float(numpy.sum(vec1*vec2))
	denom=numpy.linalg.norm(vec1)*numpy.linalg.norm(vec2)
	cos=num/denom
	sim=0.5+0.5*cos
	return cos
def read_xvg(file):
	result_array=[]
	with open(file) as f:
		line=f.readlines()
		# print(line[0])
	for j in range(16,len(line)):	
		
		a=(line[j].strip('\n').split())
		b=int(a[0])
		c=float(a[1])
		result_array.append([b,c])
	# numpy.savetxt("result_array.txt", result_array)
	result_array2=numpy.array(result_array,dtype=float)
	return result_array2
def draw_heatmap(data,ii,jj):
    cmap = sns.color_palette("rainbow", 7)
    figure=plt.figure(facecolor='w')
    outputname="./clusterPicture/"
    ax = sns.heatmap(pd.DataFrame(data),annot=True,vmin=-0.5,vmax=0.5,xticklabels= True, yticklabels= True,cmap='rainbow',linewidths = 0.05,linecolor = 'white')
    # ax = sns.heatmap(pd.DataFrame(data),annot=True,xticklabels= True, yticklabels= True,cmap='rainbow',linewidths = 0.05,linecolor = 'white')

    ax.set_ylabel('AA kind', fontsize = 2)
    ax.set_xlabel('AA kind', fontsize = 2)
    plt.xticks(rotation=90)  
    plt.yticks(rotation=360)

    file_1=outputname+str(ii)+"and"+str(jj)+".png"
    print(str(ii)+str(jj))
    plt.savefig(file_1)
    # plt.show()



def pca(result_array2):
	sum=0
	i=0
	
	for i in range(len(result_array2)):
		sum=sum+float(result_array2[i])
	# print(sum)

	bound=sum*0.9
	
	# print(bound)
	sum=0
	i=0
	while(i<len(result_array2)):
		if(sum>=bound):
			break;
		sum=sum+float(result_array2[i])
		i=i+1
	return i
def getvalue(file):
	f=open(file,"r")
	s=f.read()
	a=s.strip().split("\n")

	return a 
def getVector(file,number):
	f=open(file,"r")
	s=f.read()
	a=s.strip().split("\n")
	print(len(a)/number)
	vectorMatrix=np.zeros((number,int(len(a)/number)))

	k=0
	for i in range(0,number):
		for j in range(0,int(len(a)/number)):
			vectorMatrix[i][j]=a[k]
			k=k+1

	return vectorMatrix

def sameLength(a1,a2):
	l1=len(a1)
	l2=len(a2)
	if l1<l2:
		a1=numpy.pad(a1,(0,l2-l1),'constant',constant_values=(0,0))
	else:
		a2=numpy.pad(a2,(0,l1-l2),'constant',constant_values=(0,0))
	return a1,a2
def add_vector(arr):
	row=arr.shape[0]
	column=arr.shape[1]
	sum_vector=0
	for i in range(0,row):
		sum=0
		for j in range(0,column):
			sum=sum+arr[i][j]**2
		sum_vector=sum_vector+sum

	return sum_vector/row
if __name__ == '__main__':
		filename = "name.txt"
		myfile = open(filename) 
		l=myfile.readlines()
		lines = len(l) 
		path='normalModeProjectionPCAfigure'
		folder = os.path.exists(path)
		if not folder:
			os.makedirs(path)
		# figN=l[1].strip()
		figN='mode_'
		numOfStructue=lines-1

		file_path="./r1.txt"#eigenvalue
		value=getvalue(file_path)
		myfile = open(file_path) 
		numOfEigenvalue=len(myfile.readlines()) 
		

		file_path1="./r2.txt"#eigenvector
		vector=getVector(file_path1,len(getvalue(file_path)))
		print(vector.shape)
		pc1=vector[0,:]
		pc2=vector[1,:]

		similarity_array=np.zeros((lines-1,2))
		x=np.zeros((1,lines))
		y=np.zeros((1,lines))

		for modeChoosed in range(0,4):
			for w in range(1,lines):################################20 need to change:19 structures
					file_path3="./modeVectortxt/modeVector_"+str(w)+".txt"
					modesVector1=getVector(file_path3,numOfEigenvalue)##############################753 need to change number of eigenvector
					maxMode1=modesVector1[modeChoosed,:]
					
					# x[0,w]=cosine_similarity(pc1,maxMode1)*numpy.linalg.norm(maxMode1)
					# y[0,w]=cosine_similarity(pc2,maxMode1)*numpy.linalg.norm(maxMode1)
					pc1,maxMode1=sameLength(pc1,maxMode1)
					pc2,maxMode1=sameLength(pc2,maxMode1)
					x[0,w]=abs(cosine_similarity(pc1,maxMode1))
					y[0,w]=abs(cosine_similarity(pc2,maxMode1))
			
			plt.hist(y[0], bins =  [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],color="skyblue") 
			plt.xlabel('projection value')
			plt.ylabel('frequency')
			figName=figN+""+str(modeChoosed)
			# plt.text(0.8,9,figName+"_pc2")
			plt.savefig("normalModeProjectionPCAfigure/"+figName+"_pc2")
			# plt.show()
		

			
			plt.hist(x[0], bins =  [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],color="skyblue") 
			plt.xlabel('projection value')
			plt.ylabel('frequency')
			figName=figN+""+str(modeChoosed)
			# plt.text(0.8,9,figName+"_pc1")
			plt.savefig("normalModeProjectionPCAfigure/"+figName+"_pc1")
		
		# use_colors={52:'red',23:'red',38:'red',17:'red',16:'red',51:'red',49:'red',22:'red',32:'red',18:'red',20:'red',37:'red',33:'red',21:'red',19:'red',15:'green',45:'green',8:'green',35:'green',24:'green',10:'green',7:'green',9:'green',44:'green',36:'green',53:'green',2:'green',4:'green',6:'green',3:'green',5:'green',11:'green',1:'green',12:'green',13:'green',14:'green',46:'green',47:'green',48:'green',50:'green',30:'green',26:'green',25:'green',42:'green',43:'green',29:'green',39:'green',34:'green',27:'green',31:'green',40:'green',41:'green',28:'green'}
		# fig,ax=plt.subplots()
		# n=np.arange(1,54)
		# ax.scatter(x,y,7,c=[use_colors[i] for i in range(1,54)])
		# plt.rcParams['figure.figsize'] = (180.0, 140.0)
		# for i,txt in enumerate(n):
		# 	ax.annotate(txt,(x[0,i],y[0,i]),fontsize=7)
		# plt.show()