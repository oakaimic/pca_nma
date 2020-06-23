library("bio3d")
pdb<-read.pdb("./aaa//split_chain/1M0Z_B.pdb")
mode<-nma(pdb,rm.gaps = TRUE)
modesVector<-mode[1]

fileconn1<-file("mode.txt","w+")

m=matrix(unlist(modesVector),nrow=length(unlist(mode[1])))
row<-length(unlist(mode[1]))
cow<-(length(unlist(modesVector))/length(unlist(mode[1])))
for(i in 1: row){
	for(j in  1:cow){
		writeLines(as.character(m[i,j]),fileconn1)
	}
}
print(i)
print(j)
close(fileconn1)