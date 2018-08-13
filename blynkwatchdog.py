import urllib2
import json
import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context
req = urllib2.Request("https://blynk-cloud.com/yourblynktoken/isHardwareConnected")
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())
if json == 0:
   os.system("sudo /usr/bin/blynk-client yourblynktoken")
