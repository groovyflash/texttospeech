import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup as bs
from pydub import AudioSegment
import re
import os
import time
from playsound import playsound
import requests
import sys


#This converts epub to text throught the next set of functions
def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters


blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script',
        '"',
        '[',
        ']',
        "'",
]
whitelist = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ',', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '?', '!']

element2 = ""

def chap2text(chap):
    output = ''
    soup = bs(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output

def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output

def cleantext(text):
    text2 = ''.join(str(e) for e in text)
    text2 = text2.replace('"', '')
    text2 = text2.replace("'", '')
    text3 = ""
    for element in text2:
        if element in whitelist:
            text3 = text3 + element 
    return text2

def epub2text(epub_path):
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    realbook = cleantext(ttext)
    return realbook


toread = []


for element in os.listdir():
     if ".epub" in element:
         toread += [element]

#print("Enter the book to read.")
# = input()

#Poorly converts epub to a list 


#This simply clears the system and defines variables

piece = ", "
command = "echo '" + piece + "' | nc 127.0.0.1 9988"
os.system(command)
time.sleep(0.2)
silence = AudioSegment.silent(duration=300)
command =""
sound1 = silence
sound1.export("out2.wav", format="wav")
sound2 = silence
combined_sounds = sound2[0:0.0001]
count = int(1)
export = ""
array = []
txt = ''
textout3 = ""
first = False
num = 0
count = 0

def squeakyclean (textout):
    count = 0
    first = False
    num = 0
    textout3 = ""
    for element in textout:
        if element == "purposes. ":
            first = True
            element = title + "."
        if element == " www.feedbooks.com ":
            num = num + 1
        for singlel in element:
            if count == 0:
                element = ""
            if singlel != '—':
                element = element + singlel
            if singlel == '—':
                element = element + " "
            count = count + 2
        count = 0 
        if first and num != 1:
            textout3 = textout3 + element + " "
        if num == 1:
            textout3 = textout3 + "This book was brought to you by robo reads. Thanks for listening. Bye."
            return textout3
            break

#cleans the text slightly




def texttospeech(textout3):
    piece = ", "
    num = 0
    command = "echo '" + piece + "' | nc 127.0.0.1 9988"
    os.system(command)
    silence = AudioSegment.silent(duration=300)
    first = False
    num = 0
    count = 0
    sound1 = silence
    sound1.export("out2.wav", format="wav")
    sound2 = silence
    combined_sounds = sound2[0:0.0001]
    for element in textout3:
        if element in ['.', '?', '!']:
             num = num + 1
             piece = piece + element
             sound1 = sound1[0:0.0001]
             command = "echo '" + piece + "' | nc 127.0.0.1 9988"
             os.system(command)
             sound1 = AudioSegment.from_wav("out2.wav")
             sound1 = sound1 + silence
             combined_sounds = combined_sounds + sound1
             if num == 2:
                 combined_sounds = combined_sounds + AudioSegment.silent(duration=1500)
             piece =''

        else:
            piece = piece + element

#This writes the last sentance and adds a pause at the beginning
    length = int(len(combined_sounds))
    combined_sounds = silence + combined_sounds[200:length]
#This writes the file
    combined_sounds.export("book.wav", format="wav")
    command2 = "ffmpeg -i book.wav -codec:a libmp3lame -b:a 64k " + title.replace(" ","_") + ".mp3"
    os.system(command2)



for element in toread:
    title = element.replace(".epub","")
    textout = epub2text(element)
    textout = textout.splitlines()
    textout3 = squeakyclean(textout)
    texttospeech(textout3)
    print(textout3)
    #break


#textout = epub2text(out)
#textout = textout.splitlines()
#textout3 = squeakyclean(textout)
#print (textout3)        
#texttospeech(textout3)



