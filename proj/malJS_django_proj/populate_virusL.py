import simplejson
import urllib
import urllib2


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','malJS_django_proj')

import django
django.setup()

from virusList.models import Virus


def populate():
	#from datetime import datetime
	#generate file path day be day
	'''
	now=datetime.now();
	day=str(now.day-1);
	if (len(day)==1):
		day='0'+day;
	mon=str(now.month);
	if (len(mon)==1):
		mon='0'+mon;
	dirName=str(now.year)+"-"+mon+"-"+day
	'''

	MAL_DIR = '/root/JS_repository/2015-11-14'
	print MAL_DIR
	dirs=os.listdir(MAL_DIR)
	#send malicious html found by MALTRIEVE to VIRUSTOTAL to scan
	for f in dirs:
		path=MAL_DIR
		md5=f
		
		rp=get_report_dict(md5)

		#detection
		detection="";
		det=rp.get("scans",{})
		for i in det:
			if rp.get("scans",{}).get(i,{}).get("detected")== True:
				detection+=i+', '


		print f
		add_virus(
			md5=md5,
			size=sizeOf(path),
			url=rp["permalink"],
			detection=detection
			)
		


def add_virus(md5,size,url,detection):
	v=Virus.objects.get_or_create(MD5=md5,size_KB=size)[0]
	v.VirusTotal_link=url
	v.Detection=detection
	v.save()
	return v;

def sizeOf(PATH):
	return (os.path.getsize(PATH)/1024.0)

def get_report_dict(resource):

    result_dict = {}
    APIKEY="659fd24c11e839f866f32b0dfa37887e91d6713439505e717541595252d3c47f"
    url = "https://www.virustotal.com/vtapi/v2/file/report"
    parameters = {"resource": resource,
                   "apikey": APIKEY}
    data = urllib.urlencode(parameters)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    json = response.read()
    #print json
    response_dict = simplejson.loads(json)
    return response_dict;


if __name__ == '__main__':
	print "Starting VirusList population script..."
	populate()