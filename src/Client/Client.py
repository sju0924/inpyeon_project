from src.model.letter import letter
from src import conf

class Client:
    def __init__(self):
        
        self.seq = conf.memberseqVal
        self.sodae = conf.sodae
        self.myletter = letter(self.seq,self.sodae)

    def Sender(self,Addr1,Addr2,Zipcode,senderName,relationship,password):
        self.myletter.setSenderdata(Addr1,Addr2,Zipcode,senderName,relationship,password)
    
    def WriteContent(self,title,contents,siteID):
        res = self.myletter.write(title,contents,siteID)
        print(res)
        return res
    def ModifyContent(self, title,content,siteId,letterseq,password):
        res = self.myletter.modify(title,content,siteId,letterseq,password)
        print(res)
        return res

    def deleteContent(self, siteId,letterseq,password,page):
        res=self.myletter.delete(letterseq,siteId,password,page)
        print(res)
        return res
