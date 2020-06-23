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
pdd=pdbaln(ll,web.args=list(email="oakaimic@163.com"))
mode<-nma(pdd,fit = TRUE, full = FALSE, subspace = NULL,rm.gaps = TRUE, varweight=FALSE, outpath = NULL, ncore = 1, progress = NULL)
# aln<-read.fasta("./aln.fa")
# pdbs<-read.fasta.pdb(aln)
# mode<-nma(pdbs,rm.gaps = TRUE)

#generate trajectory
# mktrj(mode)
# trj_out=file.path("./trj_normalModes/", "mode_7.pdb")
# mktrj(mode,pdb=pdd,mode=8,file = trj_out)
# mktrj(mode,mode=8)
# mktrj(mode,mode=9)
# mktrj(mode,mode=10)
mktrj(mode,mode=11)
# plot(mode, pdbs=pdd)

#store eigenvalue into file
fileconn<-file("mode1.txt","w+")
eigenvalue=mode[4]
e=unlist(eigenvalue)
m=matrix(e,nrow=length(rt_a))

row<-dim(m)[1]
cow<-dim(m)[2]
	for(j in  1:cow){
		writeLines(as.character(1/m[1,j]),fileconn)
	}
	
close(fileconn)
dir.create("modeVectortxt")
#store eigenvector into file for every structure
for(w in 1:length(rt_a)){####################################################19 need to change
	name=paste("./modeVectortxt/modeVector_",w,".txt",sep = "")
	
	print(name)
	fileconn1<-file(name,"w+")
	eigenvector=mode[3]
	e=unlist(eigenvector)
	cc=length(e)/cow/row
	m=array(e,c(cc,cow,row))

		for(i in 1: cow){
			for(j in  1:cc){
			writeLines(as.character(m[j,i,w]),fileconn1)
		}
	}

	close(fileconn1)
}

