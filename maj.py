import os
import zipfile

downloadF = os.system("wget -i source.txt")
if downloadF:
	print("Download fail (error "+ str(downloadF) + ")" )
	exit()

with zipfile.ZipFile("main.zip", 'r') as zip:
    zip.printdir()
    zip.extractall() 

with open("target.txt",'r') as target:
	importF = os.system("scp -r site-perso-main/* "+ next(target))
	if importF:
		print("Upload fail (error "+ str(importF) + ")" )
		exit()
print("Update success")

#panautre@perso.isima.fr:~/public_html