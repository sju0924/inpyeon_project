from letter import letter

class Client:
    def __init__(self):
        
        self.seq = '282992654'
        self.sodae = '3226'
        self.myletter = letter(self.seq,self.sodae)

    def Sender(self,Addr1,Addr2,Zipcode,senderName,relationship,password):
        self.myletter.setSenderdata(Addr1,Addr2,Zipcode,senderName,relationship,password)
    
    def WriteContent(self,title,content):
        self.myletter.write(title,content)
        print('전송기로' , self.myletter.memberseqVal,'에게 전송 완료')
