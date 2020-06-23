library("bio3d")

rt<-read.table("name.txt",head=TRUE)
rt_a<-as.matrix(rt)

avg="ave.txt"
avg=read.table(avg)
avg_a<-as.matrix(avg)
avg_m<-matrix(unlist(avg),nrow=1)
write.pdb(file="./avg.pdb",xyz=avg_m)
for(i in 1:length(rt_a)){
	pro_file=paste("proj_pc1_xyz",as.character(i),".txt",sep="",collapse = NULL)
	print(pro_file)
	pro<-read.table(pro_file)
	pro_a<-as.matrix(pro)
	pro_m<-matrix(unlist(pro),nrow=1)
	write_file=paste("proj_pc1_",as.character(i),".pdb",sep="",collapse = NULL)
	write.pdb(file=write_file,xyz=pro_m)
}
for(i in 1:length(rt_a)){
	pro_file=paste("proj_pc2_xyz",as.character(i),".txt",sep="",collapse = NULL)
	print(pro_file)
	pro<-read.table(pro_file)
	pro_a<-as.matrix(pro)
	pro_m<-matrix(unlist(pro),nrow=1)
	write_file=paste("proj_pc2_",as.character(i),".pdb",sep="",collapse = NULL)
	write.pdb(file=write_file,xyz=pro_m)
}
# pro_m<-matrix(unlist(pro),nrow=length(pro_a)/3)