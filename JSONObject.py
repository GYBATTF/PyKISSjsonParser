from JSONTypes import JSONTypes

class JSONObject:
    def __init__(self, type, value):
        self.type = type
        if (self.type != JSONTypes.ARRAY) and (self.type != JSONTypes.OBJECT):
            self.locked = True
            self.value = value
        elif (self.type == JSONTypes.ARRAY):
            self.data = []
            self.type = type
            self.locked = False
            self.size = 0
        elif (self.type == JSONTypes.OBJECT):
            self.data = {}
            self.type = type
            self.locked = False
            self.size = 0

    def __str__(self):
        if (self.type != JSONTypes.ARRAY) and (self.type != JSONTypes.OBJECT):
            return str(self.value)
        elif (self.type == JSONTypes.ARRAY):
            rtn = "["
            for i in self.data:
                rtn += str(i)
                rtn += ", "
            rtn = rtn[:len(rtn) - 2]
            rtn += "]"
            return rtn
        else:
            rtn = "{"
            for i in self.data:
                rtn += i
                rtn += " : "
                rtn += str(self.data[i])
                rtn += ", "
            rtn = rtn[:len(rtn) - 2]
            rtn += "}"
            return rtn

    def lock(self):
        self.locked = True

    def size(self):
        if (self.type == JSONTypes.OBJECT) or (self.type == JSONTypes.ARRAY):
            return self.size
        elif (self.type == JSONTypes.NULL):
            return 4
        else:
            return len(str(value))

    def add(self, key, value):
        if (not self.locked) and self.type == JSONTypes.OBJECT:
            self.data.update({key : value})
        elif (not self.locked) and self.type == JSONTypes.ARRAY:
            self.data.append(value)

    def get(self, index):
        if (self.type == JSONTypes.OBJECT):
            return self.data[index]
        elif (self.type == JSONTypes.ARRAY):
            return self.data[index]
        else:
            return self.value

    def getType(self):
        return self.type

    def setJSON(self, json):
        self.json = json
    
    def getJSON(self):
        s = self.json
        del self.json
        return s
