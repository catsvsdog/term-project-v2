class Top:
    def __init__(self, name, color, season, type, serialNum = 0):
        self.name = name
        self.color = color
        self.season = season
        self.type = type #baggy or not
        self.serialNum = serialNum
        self.isTop = "Top"

    def getType(self):
        return self.type
    def getSeason(self):
        result = list(self.season)
        final = ", ".join(result) 
        return final
    
    def changeName(self, other):
        self.name = other
    def changeSeason(self, other):
        self.season = other
    def changeColor(self, other):
        self.color = other
    def changeType(self, other):
        self.type = other
        
    def getColor(self):
        result = ""
        if isinstance(self.color, list):
            for i in self.color:
                result = ",".join(i)
            return result
        else:
            return self.color
    
    def __eq__(self, other):
        if ((self.name == other.name) and (self.color == other.color) and (self.season == other.season) and (self.type == other.type)):
            return True
        else:
            return False

    def __repr__(self):
        return f"Top: {self.name}"

class Bottom:
    def __init__(self, name, color, season, type, serialNum = 0):
        self.name = name
        self.color = color
        self.season = season
        self.type = type
        self.serialNum = serialNum
        self.isBottom = "bottom"
    def getType(self):
        return self.type
    def changeName(self,other):
        self.name = other
    def changeSeason(self, other):
        self.season = other
    def changeColor(self, other):
        self.color = other
    def changeType(self, other):
        self.type = other
    
    def getSeason(self):
        return self.season
    
    def getColor(self):
        return self.color
    def __repr__(self): 
        return f"Bottom: {self.name}"#, color: {self.color}, season: {self.season}"
    def __eq__(self, other):
        if (self.name == other.name) and (self.color == other.color) and (self.season == other.season) and (self.type == other.type):
            return True
        else:
            return False
class Outfit:
    def __init__(self, top, bottom):
        self.top = top
        self.bottom = bottom
    def getTop(self):
        return self.top
    def getBottom(self):
        return self.bottom
    def getColor(self):
        # col = set()
        # col.add(self.top.getColor())
        # col.add(self.bottom.getColor())
        # return col
        return [self.top.getColor(), self.bottom.getColor()]
    def getStyle(self):
        # st = set()
        # st.add(self.top.getType())
        # st.add(self.bottom.getType())
        # return st
        return [self.top.getType(),self.bottom.getType()]
    
    def __repr__(self):
        return f"{self.top}, {self.bottom}"
    
    def __eq__(self, other):
        return (self.top.name == other.top.name) and (self.bottom.name == other.bottom.name)
    #def replaceTop(self, other):