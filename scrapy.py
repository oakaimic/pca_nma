import requests
import urllib3.request
import os

name2="1PT0"#####################need to change
name=name2+"_A"#####################need to change
url='http://ufq.unq.edu.ar/codnas/php/entry_conformers_ws.php'
post_data={'ID_POOL':name}
response=requests.post(url,data=post_data)
r=response.text
# r = r.encode('unicode-escape').decode('string_escape')
r=r[:-2]
r=r[2:]
r=r.replace('}','')
r=r.replace('{','')
array=r.split(',') 
print(array)
# os.mkdir('./'+name2)
#"PDB_id":"1GHD_A"
with open("./name.txt","w+") as n:
	n.write('name'+"\n")
	for i in range(0,len(array)):
		if array[i].find('PDB_id')>=0:
			pdbID="".join(list(array[i])[10:-1])
			print(pdbID[0:4])
			n.write(pdbID+"\n")
			# url="https://files.rcsb.org/download/"+pdbID+".pdb"
			# f=requests.get(url)
			
			# with open("./aaa/"+pdbID[0:4]+".pdb","w+") as code:
			# 	code.write(f.content)