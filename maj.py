import os
import zipfile

downloadF = os.system("wget -i configuration.txt")
if downloadF:
	print("Download fail (error "+ str(downloadF) + ")" )
	return

with zipfile.ZipFile("main.zip", 'r') as zip:
    zip.printdir()
    zip.extractall() 

importF = os.system("scp -r main-site-perso panautre@perso.isima.fr:~public_html")
if importF:
	print("Download fail (error "+ str(importF) + ")" )
	return
print("Update success")

