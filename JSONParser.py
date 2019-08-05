from JSONObject import JSONObject
from JSONTypes import JSONTypes

def parse(json):
    p = None
    while (0 != len(json)):
        if not (getType(json[0]) == JSONTypes.INVALID):
            p = parser(json)
            json = p.getJSON()
        else:
            json = json[1:]
    print(p)
    return p
    
def parser(json):
    type = getType(json[0])
    if (type == JSONTypes.ARRAY):
        return parseArray(json)
    elif (type == JSONTypes.OBJECT):
        return parseObject(json)
    elif (type == JSONTypes.STRING):
        return parseString(json)
    elif (type == JSONTypes.NULL):
        json = json[3:]
        p = JSONObject(JSONTypes.BOOLEAN, None)
        p.setJSON(json)
        return p
    elif (json[0] == "r"):
        json = json[3:]
        p = JSONObject(JSONTypes.BOOLEAN, True)
        p.setJSON(json)
        return p
    elif (json[0] == "a"):
        json = json[4:]
        p = JSONObject(JSONTypes.BOOLEAN, False)
        p.setJSON(json)
        return p
    elif (isNumber(json[0])):
        return parseNumber(json)
    else:
        return JSONTypes.INVALID

def getType(firstChar):
    if (firstChar == "["):
        return JSONTypes.ARRAY
    elif (firstChar == "{"):
        return JSONTypes.OBJECT
    elif (firstChar == "\""):
        return JSONTypes.STRING
    elif (firstChar.lower() == "n"):
        return JSONTypes.NULL
    elif (firstChar.lower() == "t"):
        return JSONTypes.BOOLEAN
    elif (firstChar.lower() == "f"):
        return JSONTypes.BOOLEAN
    elif (isNumber(firstChar)):
        return JSONTypes.NUMBER
    else:
        return JSONTypes.INVALID

def parseNumber(json):
    for i in range(len(json)):
        if (json[i] == "e" or json[i] == "."):
            continue
        if not isNumber(json[i]):
            if ("e" in json[:i]):
                for j in range(i):
                    if (json[j] == "e"):
                        p = JSONObject(JSONTypes.NUMBER, float(json[:j]) * float(json[j:i]))
                        p.setJSON(json[i:])
                        return p
            elif ("." in json[:i]):
                p = JSONObject(JSONTypes.NUMBER, float(json[:i]))
                p.setJSON(json[i:])
                return p
            else:
                p = JSONObject(JSONTypes.NUMBER, int(json[:i]))
                p.setJSON(json[i:])
                return p
            


def parseString(json):
    stack = 1
    for i in range(1, len(json)):
        if (json[i] == "\\"):
            stack += 1
        elif (json[i] == "\""):
            stack -= 1

        if (stack < 1):
            value = json[1:i]
            json = json[len(value) + 2:]
            value = removeBackslashes(value)
            p = JSONObject(JSONTypes.STRING, value)
            p.setJSON(json)
            return p

def removeBackslashes(s):
    rtn = ""
    for c in s:
        if (c != "\\"):
            rtn = rtn + c
    return rtn

def getObjArrLen(json, type):
    if (type == JSONTypes.ARRAY):
        cplus = "["
        cminus = "]"
    else:
        cplus = "{"
        cminus = "}"
    
    stack = []
    for i in range(len(json)):
        if (json[i] == cplus):
             stack.extend(json[i])
        elif (json[i] == cminus):
            stack.pop()
        
        if (len(stack) == 0):
            return i

def parseObject(json):
    type = JSONTypes.OBJECT
    end = getObjArrLen(json, type)
    p = JSONObject(type, None)
    object = json[1:end + 1]

    tmpKey = ""
    buildKey = True
    while (0 != len(object)):
        if (buildKey and getType(object[0]) == JSONTypes.STRING):
            buildKey = not buildKey
            tmpKeyObj = parseString(object)
            object = tmpKeyObj.getJSON()
            tmpKey = tmpKeyObj.get(None)
        elif not (getType(object[0]) == JSONTypes.INVALID):
            buildKey = not buildKey
            element = parser(object)
            '''
            print(tmpKey, end="")
            print(" : ", end="")
            '''
            object = element.getJSON()
            '''
            print(element)
            '''
            p.add(tmpKey, element)
        else:
            object = object[1:]

    p.setJSON(json[end:])
    return p
    
    
def parseArray(json):
    type = JSONTypes.ARRAY
    end = getObjArrLen(json, type)
    p = JSONObject(type, None)
    array = json[1:end + 1]

    while (0 != len(array)):
        if not (getType(array[0]) == JSONTypes.INVALID):
            element = parser(array)
            array = element.getJSON()
            p.add(None, element)
        else:
            array = array[1:]

    p.setJSON(json[end:])
    return p

def isNumber(c):
    try:
        float(c)
        return True
    except:
        return False