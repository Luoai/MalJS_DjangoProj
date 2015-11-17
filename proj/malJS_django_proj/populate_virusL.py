import simplejson
import urllib
import urllib2


import os
os.envron.setdefault('DJANGO_SETTINGS_MODULE','malJS_django_proj')

import django
django.setup()

from virusList.models import virusList

def populate():
	path=""
	md5=""
	rp=get_report_dict(md5)
	add_virus(
		MD5=md5,
		size_KB=sizeOf(path),
		VitusTotal_link=rp.permalink)


def add_virus(md5,size,url):
	v=Virus.objects.get_or_create(MD5=md5,size_KB=size)[0]
	v.VirusTotal_link=url
	v.save()
	return v;

def sizeOf(PATH):
	return (os.path.getsize(PATH)/1024.0)

def get_report_dict(self,resource):

    result_dict = {}
    
    url = "https://www.virustotal.com/vtapi/v2/file/report"
    parameters = {"resource": resource,
                   "apikey": APIKEY}
    data = urllib.urlencode(parameters)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    json = response.read()
    
    response_dict = simplejson.loads(json)
    return response_dict;