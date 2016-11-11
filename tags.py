from mutagen.id3 import ID3


def metadata():
    metaText = []

    # audio = ID3("xxx.mp3")
    audio = ID3("Hopeless Opus.mp3")
    # audio = ID3("Broken Arrows.mp3")
    tags = audio.items()

    # for tag in tags:
    #     if tag[0] == 'APIC:':
    #         pass
    #         # print("cover art image")
    #         # this is becuse we don't want to parse Cover Art image as Text'
    #     else:
    #         print("\n")
    #         print(str(tag[0]).encode(encoding='utf_8'))
    #         # print(str(tag[1]).encode(encoding='utf_8'))

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

if __name__ == '__main__':
    meta = metadata()
    final = []
    # print(meta)
    for data in meta:
        split = data.split()
        for text in split:
            final.append(text)

    for text in final:
        print(text)
