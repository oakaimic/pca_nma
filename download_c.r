library("bio3d")
# library("rPython")

# file_name="./scrapy.py"
# python.load(file_name)
rt<-read.table("name.txt",head=TRUE)
rt_a<-as.matrix(rt)
l<-list()
for (i in 1:length(rt_a))
{
	l[i]<-(substr(rt_a[i],0,6))
}

dirname="./aaa//"#####################need to change
# unlink("aaa",recursive=TRUE)
dir.create("aaa")
l_set=l
for(i in 1:length(rt_a)){
	l_set[i]=substr(l[i],start=1,stop=4)
}
unique=unique(l_set)
files<-list()
for (i in 1:length(rt_a)){
	print(i)
	t=paste("./aaa/",l[i],".pdb")
	if(file.exists(t)){
		
	}
	else{
		files[i]<-get.pdb(unlist(l[i]),split=TRUE,path=dirname)
	}
	

}
# ll<-NULL
# for(i in 1:length(unique)){
# 	nnn<-paste("./aaa/",unique[i],".pdb",sep="")
# 	ll<-c(ll,nnn)
# }

ll<-NULL
for(i in 1:length(rt_a)){
	nnn<-paste(dirname,"split_chain/",l[i],".pdb",sep="")
	ll<-c(ll,nnn)
}