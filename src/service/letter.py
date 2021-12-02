import requests
import conf

class letter:
    
    def __init__(self,seq,sodae):
        self.session = requests.Session()
        
        self.Addr1 = ''
        self.Addr2 = ''
        self.senderName = ''
        self.memberseqVal = conf.memberseqVal
        self.sodaeVal = conf.sodae
        self.senderZipcode=''
        self.relationship = ''
        self.password = ''
        
        self.is_sender = 0
        self.is_Receiver = 0
    def setSenderdata(self, Addr1,Addr2,Zipcode,senderName,relationship,password):
        self.Addr1 = Addr1
        self.Addr2 = Addr2
        self.senderZipcode = Zipcode
        self.senderName = senderName
        self.relationship = relationship
        self.password = password

        self.is_sender = 1
    

    def write(self,title,content,siteID):
        url = 'https://atc.airforce.mil.kr:444/user/emailPicSaveEmail.action'
        data = {
            'siteId': siteID,
            'parent': '%2Fuser%2FindexSub.action%3FcodyMenuSeq%3D159014200%26siteId%3D'+siteID+'%26menuUIType%3Dsub%26dum%3Ddum%26command2%3DgetEmailList%26searchName%3D'+conf.name+'%26searchBirth%3D'+conf.birthday+'%26memberSeq%3D285810103',
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
        
        return (response.status_code)

    def modify(self,title,content,siteID,letterseq,password):
        url = 'https://atc.airforce.mil.kr:444/user/emailPicModifyEmail.action'
        data = {
            'siteId': siteID,
            'parent': '%2Fuser%2FindexSub.action%3FcodyMenuSeq%3D159014200%26siteId%3D'+siteID+'%26menuUIType%3Dsub%26dum%3Ddum%26command2%3DmodifyForm%26searchCate%3D%26searchVal%3D%26page%3D1%26letterSeq%3D'+str(letterseq),
            'page': '1',
            'command2': 'writeEmail',
            'searchCate': '',
            'searchVal': '',
            'letterSeq': letterseq,
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
            'password': password
        }

        response = self.session.post(url = url, data=data, verify=False)
        
        return (response.status_code)

    def delete(self,letterseq,siteId,password,page):
        URL = 'https://www.airforce.mil.kr/user/emailPicDeleteEmail.action'
        data={
            'siteId': siteId,
            'letterSeq': letterseq,
            'page': page,
            'command1': 'deleteEmail',
            'password': password
        }

        response = self.session.post(url = URL, data=data, verify=False)
        
        return (response.status_code)