library("bio3d")


rt<-read.table("name.txt",head=TRUE)
rt_a<-as.matrix(rt)
l<-list()
for (i in 1:length(rt_a))
{
	l[i]<-(substr(rt_a[i],0,6))
}

dirname="./aaa//"
# files<-list()
# for (i in 1:length(rt_a)){
# 	files[i]<-get.pdb(unlist(l[i]),URLonly=FALSE,split=TRUE,path=dirname,overwrite=TRUE)

# }
ll<-NULL
for(i in 1:length(rt_a)){
	nnn<-paste(dirname,"split_chain/",l[i],".pdb",sep="")
	ll<-c(ll,nnn)
}

# for(i in 1:length(rt_a)){
# 	for(j in 1:length(rt_a)){
# 		pdb1<-read.pdb(ll[i])
# 		pdb2<-read.pdb(ll[j])
# 		m1<-nma(pdb1)
# 		m2<-nma(pdb2)
# 		eigenvalueM1<-length(m1$L)
# 		eigenvalueM2<-length(m2$L)
# 		matrixM1<-matrix(m1$U,c(length(unlist(m1$U))/length(m1$L),length(m1$L)))
# 		matrixM2<-matrix(m2$U,c(length(unlist(m2$U))/length(m2$L),length(m2$L)))
# 	}
# }
file.create('eigenvalue.txt')
fileconn2<-file("eigenvalue.txt","w+")
for(i in 1:length(rt_a)){
	pdb<-read.pdb(ll[i])
	m<-nma(pdb,fit =TRUE)
	
	eigenvalue=m$L
	e=unlist(eigenvalue)

	row<-length(e)
	
	name=paste("./modeVectortxt1/modeVector_",i,".txt",sep = "")
	
	print(name)

	fileconn1<-file(name,"w+")
	eigenvector=m$U
	e=unlist(eigenvector)
	cc=length(e)/row
	mmmm=array(e,c(row,cc))
	print(row)
	print(cc)
		for(i in 1: row){
			for(j in  1:cc){
			writeLines(as.character(mmmm[i,j]),fileconn1)
		}
	}

	
	writeLines(as.character(row),fileconn2)

	close(fileconn1)
}
close(fileconn2)