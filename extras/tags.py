'''
this module contains functions that extracts metadata from
mp3 file and returns a python list of UniCode Characters
NOTE : Windows Does't support unicode in powershell and console by default

run `chcp 65001` if you getting erros releted to unicode in windows

'''

from mutagen.id3 import ID3
from bs4 import UnicodeDammit


def metadata(mp3file):
    metaText = []

    audio = ID3(mp3file)
    tags = audio.items()

    for tag in tags:
        if (tag[0] == 'USLT::eng'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TALB'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TPE1'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TPE2'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TSOP'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TIT2'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TCON'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
    return metaText


def metaTextToUnicode(metaText):
    final = []
    uniText = []
    # print(meta)
    for data in metaText:
        split = data.split()
        for text in split:
            final.append(text)

    for text in final:
        dammit = UnicodeDammit(text)
        uniText.append(dammit.unicode_markup)
    return uniText
