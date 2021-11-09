from src.model.Music import Music, lyric

class MusicClient:
    def __init__(self):
        self.music = Music()

    def searchMusicByTitle(self,title):
        self.music.getMusic(title)
        return [self.music.lst_code,self.music.lst_title,self.music.lst_singer] 

    def getCode(self):
        if(self.music.Length() == 0):
            return ValueError(0)

        return self.music.lst_code
    
    def getTitle(self):
        if(self.music.Length() == 0):
            return ValueError(0)

        return self.music.lst_title

    def getSinger(self):
        if(self.music.Length() == 0):
            return ValueError(0)

        return self.music.lst_singer

    def clear(self):
        self.music.clear()

class lyricClient:
    def __init__(self):
        self.lyric = lyric()

    def getLyricByCode(self,code):
        res = self.lyric.getLyric(code)
        return res