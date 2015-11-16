import os
import postfile


MAL_DIR = '/root/JS_repository/2015-11-14'
APIKEY="659fd24c11e839f866f32b0dfa37887e91d6713439505e717541595252d3c47f"
dirs=os.listdir(MAL_DIR)
#send malicious html found by MALTRIEVE to VIRUSTOTAL to scan
for f in dirs:
	myFile = MAL_DIR+"/"+f
	host = "www.virustotal.com"
	selector = "https://www.virustotal.com/vtapi/v2/file/scan"
	fields = [("apikey",APIKEY)]
#	file_to_send=open('test.txt','rb').read()
	file_to_send = open(myFile,'rb').read()
	files = [("file",myFile,file_to_send)]
	print file_to_send
	json = postfile.post_multipart(host,selector,fields,files)
	print json
	break
	
