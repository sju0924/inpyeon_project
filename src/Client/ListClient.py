from src.model.List import LetterList
from src import conf

class ListClient:
    def __init__(self):
        self.List = LetterList()
        self.name = conf.name
        self.birthday = conf.birthday
        self.memVal=conf.memberseqVal
    

    def searchletter(self,siteId,page):
        print("찾기: ",siteId,self.name,self.birthday,self.memVal,page)
        self.List.getList(siteId,self.name,self.birthday,self.memVal,page)
        return [self.List.lst_code,self.List.lst_title,self.List.lst_author,self.List.lst_state,self.List.lst_relation]

    def getCode(self):
        if(self.music.Length() == 0):
            return ValueError(0)

        return self.List.lst_code
    
    def getTitle(self):
        if(self.music.Length() == 0):
            return ValueError(0)

        return self.List.lst_title

    def getAuthor(self):
        if(self.music.Length() == 0):
            return ValueError(0)

        return self.List.lst_author

    def getState(self):
        if(self.music.Length() == 0):
            return ValueError(0)

        return self.List.lst_state

    def getLetter(self,code,page,pw):
        res = self.List.getLetter(code,page,pw)
        return res



    def clear(self):
        self.List.clear()

