'''
this module contains functions that extracts metadata from
mp3 file and returns a python list of UniCode Characters
NOTE : Windows Does't support unicode in powershell and console by default

run `chcp 65001` if you getting erros releted to unicode in windows

'''

#pip install mutagen
#pip install BeautifulSoup4

from mutagen.id3 import ID3
from bs4 import UnicodeDammit

def __init__(self):
    self.metaDataDict={}
    self.metaText = []


def getMetadata(mp3file):
    

    audio = ID3(mp3file)
    tags = audio.items()
    """
    print ("type of tags is:")
    print (type(tags))

    print ("tags are:")
    print (tags)
    """
    for tag in tags:
        if (tag[0] == 'USLT::eng'):
            self.metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TALB'):
            self.metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TPE1'):
            self.metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TPE2'):
            self.metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TSOP'):
            self.metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TIT2'):
            self.metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TCON'):
            self.metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TDRC'):
            self.metaText.append(str(tag[1]).encode(encoding='utf_8'))
    return self.metaText


def getMetaText(self):# getter function for metaText
    return self.metaText

def getMetadataDict(self):
    return self.metaDataDict

def getMetadataDict(self,mp3file):
    

    audio = ID3(mp3file)
    tags = audio.items()
    """
    print ("type of tags is:")
    print (type(tags))

    print ("tags are:")
    print (tags)
    """
    for tag in tags:
        if (tag[0] == 'USLT::eng'):
            self.metaDataDict["USLT::eng"]=(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TALB'):
            self.metaDataDict["TALB"]=(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TPE1'):
            self.metaDataDict["TPE1"]=(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TPE2'):
            self.metaDataDict["TPE2"]=(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TSOP'):
            self.metaDataDict["TSOP"]=(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TIT2'):
            self.metaDataDict["TIT2"]=(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TCON'):
            self.metaDataDict["TCON"]=(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TDRC'):
            self.metaDataDict["TDRC"]=(str(tag[1]).encode(encoding='utf_8'))
    return self.metaDataDict


def metaTextToUnicode(metaText):
    # print(metaText)
    final = []
    uniText = []
    for data in metaText:
        split = data.split()
        for text in split:
            final.append(text)

    for text in final:
        dammit = UnicodeDammit(text)
        uniText.append(dammit.unicode_markup)
    return uniText

if __name__=="main":
    getMetadata("D:/Songs(english)/naked/7 Years - Lukas Graham.mp4")