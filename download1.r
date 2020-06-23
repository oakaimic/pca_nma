library("bio3d")
# library("rPython")

# file_name="./scrapy.py"
# python.load(file_name)
rt<-read.table("name1.txt",head=TRUE)
rt_a<-as.matrix(rt)
l<-list()
for (i in 1:length(rt_a))
{
	l[i]<-((rt_a[i]))
}


# ll<-NULL
# for(i in 1:length(unique)){
# 	nnn<-paste("./aaa/",unique[i],".pdb",sep="")
# 	ll<-c(ll,nnn)
# }

ll<-NULL
for(i in 1:length(rt_a)){
	nnn<-paste(l[i],sep="")
	ll<-c(ll,nnn)
}
pdd=pdbaln(ll,web.args=list(email="oakaimic@163.com"),fit=TRUE)
pdd_matrix=matrix(pdd$xyz,nrow=length(rt_a))
attach(transducin)
r<-pca.pdbs(pdd,rm.gaps=TRUE,fit=TRUE)
r<-pca(pdd,core.find =TRUE,fit =TRUE)


mktrj(r)
#generate trajectory
mktrj(r,pc=1)
mktrj(r,pc=2)
mktrj(r,pc=3)
mktrj(r,pc=4)
mktrj(r,pc=5)
mktrj(r,pc=6)
mktrj(r,pc=7)
mktrj(r,pc=8)
pymol(r,mode=1,file="1.py")
pymol(r,mode=2,file="2.py")
pymol(r,mode=3,file="3.py")
file.create('r1.txt')
file.create('r2.txt')

fileconn<-file("r1.txt")
for(i in r[1]){
	writeLines(as.character(unlist(i)),fileconn)
}


fileconn1<-file("r2.txt","w+")
eigenvector=r[2]
m=matrix(unlist(eigenvector),nrow=length(unlist(r[1])))
row<-length(unlist(r[1]))#number of eigenvalue
cow<-(length(unlist(eigenvector))/length(unlist(r[1])))
for(i in 1: row){
	for(j in  1:cow){
		writeLines(as.character(m[j,i]),fileconn1)
	}
	
}

close(fileconn1)



file.create('sdev.txt')
fileconn2<-file("sdev.txt","w+")
for(i in r$sdev){
	print(unlist(i))
	writeLines(as.character(unlist(i)),fileconn2)
}
close(fileconn2)

fileconn4<-file("xyz.txt","w+")
eigenvector=pdd$xyz
m=matrix(unlist(eigenvector),nrow=length(rt_a))
row<-length(rt_a)#number of eigenvalue
cow<-(length(unlist(eigenvector))/length(rt_a))
for(i in 1: row){
	for(j in  1:cow){
		writeLines(as.character(m[i,j]),fileconn4)
	}
	
}

close(fileconn4)
fileconn5<-file("project.txt","w+")
pdbs=pdd
gaps.pos <- gap.inspect(pdbs$xyz)
pc.xray <- pca.xyz(pdbs$xyz[, gaps.pos$f.inds])
d <- project.pca(pdbs$xyz[, gaps.pos$f.inds], pc.xray)
m=matrix(unlist(d),nrow=length(rt_a))
row<-length(rt_a)#number of eigenvalue
cow<-(length(unlist(d))/length(rt_a))
for(i in 1: row){
	for(j in  1:cow){
		writeLines(as.character(m[i,j]),fileconn5)
	}
	
}
close(fileconn5)

fileconn6<-file("resno.txt","w+")
eigenvector=pdd$resno
m=matrix(unlist(eigenvector),nrow=length(rt_a))
row<-length(rt_a)#number of eigenvalue
cow<-(length(unlist(eigenvector))/length(rt_a))
for(i in 1: row){
	for(j in  1:cow){
		writeLines(as.character(m[i,j]),fileconn6)
	
	}
	
}

close(fileconn6)
# plot(pc.xray$z[,1], pc.xray$z[,2],col="gray")
# pro<-read.table("proj_xyz1.txt")
# pro_a<-as.matrix(pro)
# pro_m<-matrix(unlist(pro),nrow=3)
# pro_m<-matrix(unlist(pro),nrow=length(pro_a)/3)
print(i)
print(j)
