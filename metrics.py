#Using the API provided by metrics plugin to monitor jenkins 
import requests
from requests.auth import HTTPBasicAuth
import json

#url points to the metrics servlet, which is one of the four other servlet
s=requests.get('http://localhost:8080/metrics/rBk77lzPddP8iPUvra1UvuYGCsOcGqiH3r-qtE3eQfruga-uSPUBbhdaGnnSbVOm/metrics', auth=HTTPBasicAuth('harsha', '******'))

e=json.loads(s.content) # Converts object type into dict type
f=e.get("counters") #gauges is one of six keys in metrics servlet
with open("test_nested4.json", "w") as outfile:
    json.dump(f, outfile, indent=4, sort_keys=False)

#print(f.get("jenkins.executor.count.value"))# to find out the number of executors, other methods are available in the metrics plugin documentation
