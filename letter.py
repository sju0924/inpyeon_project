import requests

class letter:
    
    def __init__(self,seq,sodae):
        self.session = requests.Session()
        
        self.Addr1 = ''
        self.Addr2 = ''
        self.senderName = ''
        self.memberseqVal = seq
        self.sodaeVal = sodae
        self.senderZipcode=''
        self.relationship = ''
        self.password = ''
        
        self.is_sender = 0
        self.is_Receiver = 0
    def setSenderdata(self, Addr1,Addr2,Zipcode,senderName,relationship,password):
        self.Addr1 = Addr1
        self.Addr1 = Addr2
        self.senderZipcode = Zipcode
        self.senderName = senderName
        self.relationship = relationship
        self.password = password

        self.is_sender = 1
        
    def setReceiverdata(self,memberseqVal,sodae):
        self.sodaeVal = sodae
        self.memberseqVal = memberseqVal

        self.is_Receiver = 1
    

    def write(self,title,content):
        url = 'https://atc.airforce.mil.kr:444/user/emailPicSaveEmail.action'
        data = {
            'siteId': 'last2',
            'parent': '%2Fuser%2FindexSub.action%3FcodyMenuSeq%3D156893223%26siteId%3Dlast2%26menuUIType%3Dtop%26dum%3Ddum%26command2%3DwriteEmail%26searchCate%3D%26searchVal%3D%26page%3D1%26memberSeqVal%3D282992654%26sodaeVal%3D3226',
            'page': '1',
            'command2': 'writeEmail',
            'searchCate': '',
            'searchVal': '',
            'letterSeq': '',
            'memberSeq': '',
            'memberSeqVal': self.memberseqVal,
            'sodaeVal': self.sodaeVal,
            'senderZipcode': self.senderZipcode,
            'senderAddr1': self.Addr1,
            'senderAddr2': self.Addr2,
            'senderName': self.senderName,
            'relationship': self.relationship,
            'title': title,
            'contents': content,
            'password': self.password
        }

        response = self.session.post(url = url, data=data, verify=False)
        
        print(response.text)
