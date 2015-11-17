#code reference from http://m.blog.csdn.net/blog/xiaocaiju/7610424
import simplejson
import urllib
import urllib2
import os 


            
########################################################################



class VirusTotal:
    """"""

    #----------------------------------------------------------------------
    def __init__(self, md5):
        """Constructor"""
        self._virus_dict = {}
        self._md5 = md5
        
        
    def repr(self):
        return str(self._virus_dict)
    
    def submit_md5(self, file_path):
        import postfile                                                                          
        #submit the file
        FILE_NAME =  os.path.basename(file_path) 
                           
                                                                                                 
        host = "www.virustotal.com"                                                              
        selector = "https://www.virustotal.com/vtapi/v2/file/scan"                               
        fields = [("apikey", APIKEY)]
        file_to_send = open(file_path, "rb").read()                                              
        files = [("file", FILE_NAME, file_to_send)]                                              
        json = postfile.post_multipart(host, selector, fields, files)                            
        print json
        pass
    
    def get_report_dict(self):
        result_dict = {}
        
        url = "https://www.virustotal.com/vtapi/v2/file/report"
        parameters = {"resource": self._md5,
                       "apikey": APIKEY}
        data = urllib.urlencode(parameters)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        json = response.read()
        
        response_dict = simplejson.loads(json)
        if response_dict["response_code"]: #has result 
            scans_dict = response_dict.get("scans", {})
            for anti_virus_comany, virus_name in scans_dict.iteritems():
                if virus_name["detected"]:
                    self._virus_dict.setdefault(anti_virus_comany, virus_name["result"])
        return self._virus_dict