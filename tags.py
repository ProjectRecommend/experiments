'''
ID3 tags Fun
'''
from mutagen.id3 import ID3

audio = ID3("Hopeless Opus.mp3")
tags = audio.items()
# print(type(tags))
for tag in tags:
    if tag[0] == 'APIC:':
        print("cover art image")
        # this is becuse we don't want to parse Cover Art image as Text'
    else:
        print(str(tag).encode(encoding='utf_8'))
