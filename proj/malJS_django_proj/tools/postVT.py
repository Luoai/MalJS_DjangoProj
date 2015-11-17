import os
import postfile
import VirusTotal
from datetime import datetime

#generate file path day be day
now=datetime.now();
day=str(now.day-1);
if (len(day)==1):
	day='0'+day;
mon=str(now.month);
if (len(mon)==1):
	mon='0'+mon;
dirName=str(now.year)+"-"+mon+"-"+day


MAL_DIR = '/root/JS_repository/'+dirName
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
	files = [("file",f,file_to_send)]
	#print file_to_send
	json = postfile.post_multipart(host,selector,fields,files)
	#print json
	
	
	
