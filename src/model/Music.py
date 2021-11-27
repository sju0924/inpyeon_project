#-*- coding:utf-8 -*- 
import requests

class Music:
    def __init__(self):
        self.lst_code = []
        self.lst_title = []
        self.lst_singer = []

        self.length = 0
        self.session = requests.Session()

    def Length(self):
        return self.length

    def getURL(self, keyword):
        return 'http://www.boom4u.net/lyrics/?keyword='+keyword+'&searchoption='
    
    def getMusic(self,title):
        self.length = 0

        res = self.session.get(self.getURL(title))
        res =res.text
        get_id = "a href='view.php?id="
        idx = res.find(get_id)


        while(idx !=-1):

            # 코드 찾기
            start = idx+len(get_id)
            end = res.find("'",start)
            self.lst_code.append(res[start:end])
            # 제목 찾기
            idx = res.find("'>",end+1)
            start = idx+2
            end = res.find("</a>",start)
            self.lst_title.append(res[start:end])

            #가수 찾기
            idx = res.find("searchartist=1&keyword=",end+1)
            start = idx+len("searchartist=1&keyword=")
            end = res.find("'style='",start)
            self.lst_singer.append(res[start:end])

            self.length += 1
            idx = res.find(get_id,end+1)
    
        for i in range(self.length):
            print(self.lst_code[i],self.lst_title[i],self.lst_singer[i])

    def clear(self):
        self.lst_code = []
        self.lst_title = []
        self.lst_singer = []

        self.length = 0

class lyric:
    def __init__(self):
        self.lyrics = ""    
        self.session = requests.Session()
    def getLyric(self, code):
        data = self.session.get('http://www.boom4u.net/lyrics/view.php?id='+code)
        data = data.text

        res = ""

        idx = data.find("<table class='tabletext' cellspacing=0 cellpadding=0>")
        idx = idx + len("<table class='tabletext' cellspacing=0 cellpadding=0>")
        idx_end = data.find('</table>',idx)
        while(idx < idx_end and idx != -1):
            start = data.find("<td>",idx)
            end = data.find("<br>",start+1)
            res = res + data[start+4:end] + " "
    

            idx = end+5
        res = res.replace("</table>","")
        return res