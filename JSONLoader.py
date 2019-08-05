import JSONParser
from urllib.request import urlopen

def load(s, download):
    if (download):
        data = urlopen(s).read()
        s = data.decode("utf-8")
    
    return JSONParser.parse(s)

load("https://raw.githubusercontent.com/LearnWebCode/json-example/master/pets-data.json", True)