import numpy
import mdtraj as md
import numpy as np
from multiprocessing import Pool
import sys
import os
import time
import gc


def getvalue(file):
	f=open(file,"r")
	s=f.read()
	a=s.strip().split("\n")

	return a
def getVector(file,number):
	f=open(file,"r")
	s=f.read()
	a=s.split("\n")

	vectorMatrix=np.zeros((number,int(len(a)/number)))

	k=0
	
	for i in range(0,number):
		for j in range(0,int(len(a)/number)):
			if a[k]=='NA':
				a[k]=0
			vectorMatrix[i][j]=a[k]
			k=k+1

	return vectorMatrix
def load_evecs(evecs):
	eigenvecs = []
	file = open(evecs, 'r')
	for line in file:
		a = line.split()
		for i in range(len(a)):
			a[i] = np.float64(a[i])
		a = np.array(a, dtype = np.float64)
		eigenvecs.append(a)
	file.close()
	eigenvecs = np.array(eigenvecs, dtype = np.float64)
	return eigenvecs


def average_structure(traj):

	avg_xyz = traj.xyz.mean(axis = 0, dtype=np.float64)
	
	avg_traj = md.Trajectory([avg_xyz], traj.top)
	return avg_traj
if __name__ == '__main__':
	f = open("name.txt","r") 
	name=[]
	line=f.readline()
	numofstructure=0
	while line:
		
		line = f.readline().strip()
		name.append("./aaa/split_chain/"+line+".pdb")
		numofstructure=numofstructure+1

	#eigenvalue
	numofstructure=numofstructure-1

	f ="r1.txt"
	val=getvalue(f)
	numOfval=len(val)
	#eigenvector
	f = "r2.txt"
	vector=getVector(f,numOfval)

	PATH = os.getcwd() + '/'
	# save eigenvectors
	vec_file="./eigenvec.xvg"
	np.savetxt(PATH + vec_file,\
		np.flip(vector,axis=1).T,fmt='%20.17g')
	print('Wrote eigenvectors in "%s"' % vec_file)


	
	
	f="xyz.txt"
	xyz=getVector(f,len(name)-1)
	xyz=np.array(xyz)
	
	i=0
	#delete col which dosent have atom
	while i<xyz.shape[1]:
			if 0 in xyz[:,i]:
				
				xyz=np.delete(xyz,i,axis=1)
				i=0
			i=i+1
	i=0
	while i<xyz.shape[1]:
			if 0 in xyz[:,i]:
				xyz=np.delete(xyz,i,axis=1)
				i=0
			i=i+1
	
	ave_xyz=[]

	for i in range(0,xyz.shape[1]):

		ave_xyz.append( np.mean(xyz[:,i]) )
	ave_xyz=np.array(ave_xyz)
	# print(ave_xyz)
	#write ave_xyz into file
	ff="ave.txt"
	
	with open(ff,"w+") as n:
			for k in range(0,len(ave_xyz)):
				n.write(str(ave_xyz[k])+"\n")
	#load projection value
	# f="sdev.txt"
	# projection=getvalue(f)
	f="project.txt"
	m=getVector(f,len(name)-1)
	print(m[0,:])#m[1,1],m[2,1],m[i,1] project on pc1
	print(m[:,1])
	# print(m[:,0])  projection value on pc1
	for i in range(0,len(name)-1):
		#load eigenvec
		eigenvecs = load_evecs(vec_file)
		pc1=np.array(vector[0,:])
		pc2=np.array(vector[1,:])
		#generate projection xyz onto pc1
		
		p=float(m[i,0])
		proj_xyz1=ave_xyz+p*pc1
		pro_file="./proj_pc1_xyz"+str(i+1)+".txt"
		with open(pro_file,"w+") as n:
			for k in range(0,len(proj_xyz1)):
				n.write(str(proj_xyz1[k])+"\n")
		#generate projection xyz onto pc2
				
		p2=float(m[i,1])
		proj_xyz2=ave_xyz+p2*pc2
		pro_file="./proj_pc2_xyz"+str(i+1)+".txt"
		with open(pro_file,"w+") as n:
			for k in range(0,len(proj_xyz2)):
				n.write(str(proj_xyz2[k])+"\n")


		# avg_str = md.load(name[0])
		# #create pc topology
		# pc1_traj = md.Trajectory([proj_xyz1.reshape(len(proj_xyz1)//3,3)], \
		# 	avg_str.top)
	
	
	















