# 기존 인편 목록을 가져옴
#-*- coding:utf-8 -*- 
import requests

class LetterList:
    def __init__(self):
        self.lst_code = []
        self.lst_title = []
        self.lst_author = []
        self.lst_state=[]
        self.lst_relation=[]
        self.length = 0
        self.session = requests.Session()

    def Length(self):
        return self.length

    
    
    def getList(self,siteId,name,birthday,memberseqVal,page):
        self.length = 0
        URL = 'https://www.airforce.mil.kr/user/indexSub.action'
        params={
            'codyMenuSeq': 159014200,
            'siteId': siteId,
            'menuUIType': 'sub',
            'dum': 'dum',
            'command2': 'getEmailList',
            'searchName': name,
            'searchBirth': birthday,
            'page':page,
            'memberSeq': memberseqVal
        }
        res = self.session.post(URL, data=params,verify=False)
        #print(res.text)

        res =res.text
        get_id =  "a href=\"javascript:viewEmail('"
        idx = res.find(get_id)


        while(idx !=-1):

            # 코드 찾기
            start = idx+len(get_id)
            end = res.find("'",start)
            self.lst_code.append(res[start:end])
            #print("코드: " ,res[start:end],"======================\n")
            # 제목 찾기
            idx = res.find('">',end)
            start = idx+2
            end = res.find("</a>",start)
            self.lst_title.append(res[start:end])
            #print("제목: " ,res[start:end],"======================\n")

            #작성자 찾기
            idx = res.find("<td>",end+1)
            start = idx+4
            end = res.find("</td>",start)
            self.lst_author.append(res[start:end])
            #print("작성자: " ,res[start:end],"======================\n")

            #상태 찾기
            idx = res.find("<td>",end+1)
            start = idx+4
            end = res.find("</td>",start)
            self.lst_relation.append(res[start:end])

            #상태 찾기
            idx = res.find("<td>",end+1)
            start = idx+4
            end = res.find("</td>",start)
            self.lst_state.append(res[start:end])
            self.lst_state[self.length]=self.lst_state[self.length].replace('\n',"").replace(" ","").replace('\t',"")

            self.length += 1
            idx = res.find(get_id,end+1)


        for i in range(self.length):
            print(self.lst_code[i],self.lst_title[i],self.lst_author[i],self.lst_relation[i])
            print(self.lst_state[i])
            

    def getLetter(self,code,page,pw):
        URL = 'https://www.airforce.mil.kr/user/emailPicEmailIntro.action'
        params = {
            'codyMenuSeq': 159014200,
            'siteId': 'haengjeong',
            'menuUIType': 'sub',
            'dum': 'dum',
            'command2': 'viewEmail',
            'page': page,
            'letterSeq': code,
            'password': pw
        }

        res = self.session.post(URL,data=params,verify=False)
        res = res.text
        #주소 찾기
        get_id =  '<td class="alignL">'
        idx = res.find(get_id)        
        start = idx+len(get_id)
        end = res.find("</td>",start)

        address = res[start:end].replace('\t',"").split('\r\n')

        postalcode = address[1][-7:-2]
        addr1 = address[2][:-1]
        addr2 = address[3]
        

        #내용 찾기

        get_id = '<td class="viewArea">'
        idx = res.find(get_id,end+1)   
        start = idx+len(get_id)     
        end = res.find('</td>',start)

        content = res[start:end].replace('\r\n\t\t\t\t\t',"").replace('\t',"")

        return {'postalcode': postalcode,'addr1':addr1,'addr2':addr2, 'content' : content,'letterseq':code}



    def clear(self):
        self.lst_code = []
        self.lst_title = []
        self.lst_author = []
        self.lst_state=[]
        self.lst_relation = []

        self.length = 0

