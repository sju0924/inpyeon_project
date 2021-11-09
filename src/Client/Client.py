from src.model.letter import letter
import conf

class Client:
    def __init__(self):
        
        self.seq = conf.memberseqVal
        self.sodae = conf.sodae
        self.myletter = letter(self.seq,self.sodae)

    def Sender(self,Addr1,Addr2,Zipcode,senderName,relationship,password):
        self.myletter.setSenderdata(Addr1,Addr2,Zipcode,senderName,relationship,password)
    
    def WriteContent(self,title,content):
        self.myletter.write(title,content)
        print('전송기로' , self.myletter.memberseqVal,'에게 전송 완료')
