import JSONParser
from urllib.request import urlopen

def download(url):
    data = urlopen(url).read()
    s = data.decode("utf-8")
    
    return JSONParser.parse(s)

def load(json)
    return JSONParser.parse(json)
