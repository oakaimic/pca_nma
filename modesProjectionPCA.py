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
import cmath
from matplotlib import pyplot as plt
import scipy.spatial.distance as ssd
import scipy, pylab
import scipy.cluster.hierarchy as sch
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
	vectorMatrix=np.zeros((number,len(a)/number))

	k=0
	for i in range(0,number):
		for j in range(0,len(a)/number):
			vectorMatrix[i][j]=a[k]
			k=k+1

	return vectorMatrix

def sameLength(a1,a2):
	l1=len(a1)
	l2=len(a2)
	if l1<l2:
		for i in range(0,l2-l1):
			a1.append(0)
	else:
		for i in range(0,l2-l1):
			a2.append(0)
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
def draw_hcluster(cc_matrix,cow,p):   
    D = 1.0 - cc_matrix
    # convert the redundant n*n square matrix form into a condensed nC2 array
    # flat_D = ssd.squareform(D)
    flat_D=D
    fig = pylab.figure()
    axdendro = fig.add_axes([0.09, 0.1, 0.2, 0.8])
    Y = sch.linkage(flat_D, method = 'complete')
    Z=sch.dendrogram(Y)

    Z = sch.dendrogram(Y, orientation='left', color_threshold=0.3, labels=range(1,cow+1), leaf_font_size=8)
    #axdendro.set_xticks([])
    #axdendro.set_yticks([])
    # Plot distance matrix.
    axmatrix = fig.add_axes([0.33,0.1,0.6,0.8])
    index = Z['leaves']
    D = D[index,:]
    D = D[:,index]
    im = axmatrix.matshow(D, cmap=plt.cm.viridis, vmin=0.0, vmax=0.4, aspect='auto', origin='lower')
    axmatrix.set_xticks([])
    axmatrix.set_yticks([])

    # Plot colorbar.
    axcolor = fig.add_axes([0.94,0.1,0.02,0.8])
    cbar = pylab.colorbar(im, cax=axcolor, ticks=[0.0,0.1,0.2,0.3,0.4])
    cbar.ax.tick_params( labelsize=20)
    

    # Display and save figure.
    fig.show()
    fig.savefig(p)
    return np.mean(flat_D)
if __name__ == '__main__':
		numOfStructue=53
		file_path="./r1.txt"
		value=getvalue(file_path)

		file_path1="./r2.txt"
		vector=getVector(file_path1,len(getvalue(file_path)))
		pc1=vector[0,:]
		pc2=vector[1,:]

		similarity_array=np.zeros((53,2))
		x=np.zeros((1,54))
		y=np.zeros((1,54))
		sixDimension=np.zeros((54,6))
		for w in range(1,54):################################20 need to change:19 structures
				file_path3="./modeVectortxt1/modeVector_"+str(w)+".txt"
				modesVector1=getVector(file_path3,909)##############################753 need to change number of eigenvector
				maxMode1=modesVector1[0,:]
				secondMode=modesVector1[1,:]
				thirdMode=modesVector1[2,:]
				# x[0,w]=cosine_similarity(pc1,maxMode1)*numpy.linalg.norm(maxMode1)
				# y[0,w]=cosine_similarity(pc2,maxMode1)*numpy.linalg.norm(maxMode1)
				sixDimension[w,0]=abs(cosine_similarity(pc1,maxMode1))
				sixDimension[w,1]=abs(cosine_similarity(pc2,maxMode1))
				sixDimension[w,2]=abs(cosine_similarity(pc1,secondMode))
				sixDimension[w,3]=abs(cosine_similarity(pc2,secondMode))
				sixDimension[w,4]=abs(cosine_similarity(pc1,thirdMode))
				sixDimension[w,5]=abs(cosine_similarity(pc2,thirdMode))
		print(sixDimension[1])
		sixFeatureSimilarity=np.zeros((53,53))
		for stru1 in range(1,54):
			for stru2 in range(1,54):
				sixFeatureSimilarity[stru1-1][stru2-1]=cosine_similarity(sixDimension[stru1],sixDimension[stru2])
		print(sixFeatureSimilarity)
		draw_hcluster(sixFeatureSimilarity,53,"./sixFeatureSimilarity.png")
		use_colors={52:'red',23:'red',38:'red',17:'red',16:'red',51:'red',49:'red',22:'red',32:'red',18:'red',20:'red',37:'red',33:'red',21:'red',19:'red',15:'green',45:'green',8:'green',35:'green',24:'green',10:'green',7:'green',9:'green',44:'green',36:'green',53:'green',2:'green',4:'green',6:'green',3:'green',5:'green',11:'green',1:'green',12:'green',13:'green',14:'green',46:'green',47:'green',48:'green',50:'green',30:'green',26:'green',25:'green',42:'green',43:'green',29:'green',39:'green',34:'green',27:'green',31:'green',40:'green',41:'green',28:'green'}
		fig,ax=plt.subplots()
		n=np.arange(1,54)
		ax.scatter(x,y,7,c=[use_colors[i] for i in range(1,54)])
		plt.rcParams['figure.figsize'] = (180.0, 140.0)
		for i,txt in enumerate(n):
			ax.annotate(txt,(x[0,i],y[0,i]),fontsize=7)
		plt.show()