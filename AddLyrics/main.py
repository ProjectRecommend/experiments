# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:17:21 2016
"""
import os
# import loloLyrics module
import loloLyrics

# metadata module
from tags import (getLyricsMetadata, getArtistMetadata, getTitleMetadata)

from mutagen.id3 import USLT
from mutagen.id3 import ID3

# FIXED_VARIABLES FOR TESTING PURPOSES
ROOT_DIR = '/home/raghav/nu/ProjectRecommand/experiments/AddLyrics'
FILE_NAME = 'xxx.mp3'


# Function to check if file contains lyrics or not
# Returns 0 if it contains less than 15 words in Lyrics else returns 1
def ifLyrics(root_dir, fileName):
    filePath = os.path.join(root_dir, fileName)
    lyrics = getLyricsMetadata(filePath) # list of elements    
    # Assuming that a song can't have lyrics lesses than 15 words
    if(len(lyrics)<15):
        print(0)
        return(0)
    else: 
        print(1)
        return(1)
    
# remove lyrics form corresponding ID3 tag from file
def removeLyrics(root_dir, file_name):
    filePath = os.path.join(root_dir, file_name)
    audio = ID3(filePath)
    audio.delall('USLT')
    audio.add(USLT(encoding=3, text=u" "))
    return audio.save()
    
# fetch lyrics and add to corresponding ID3 tag from file
def addLyrics(root_dir, file_name):
    filePath = os.path.join(root_dir, file_name)
    audio = ID3(filePath)
    audio.add(USLT(encoding=3, text=fetchLyrics(filePath)))
    return audio.save()

# fetches lyrics from lololyrics.com
def fetchLyrics(file_path):
    artist = getArtistMetadata(file_path)
    title = getTitleMetadata(file_path)
    return(loloLyrics.getLyrics(artist, title))
    

if(ifLyrics(ROOT_DIR, FILE_NAME) == 0):
    removeLyrics(ROOT_DIR, FILE_NAME)
    print("** removeLyrics function done **")
    addLyrics(ROOT_DIR, FILE_NAME)
    print("** addLyrics function done **")
elif(ifLyrics(ROOT_DIR, FILE_NAME) == 1):
    print("***ALL OK ***")
    