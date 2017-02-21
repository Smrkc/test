#!/usr/bin/python

MyLog = open("C:\\Users\\wiNejc\\Music\\MyLog.txt", 'w')
MyPath = "C:\\Users\\wiNejc\\Music\\"
MyNewPath = "C:\\Users\\wiNejc\\Music\\Processed\\"
from collections import Counter
from os import listdir, rename, remove
from os.path import isfile, join, getsize
import re, glob
from mutagen.id3 import ID3, ID3NoHeaderError


def hasNumbers(inputString):
    return bool(re.search("\(\d\)", inputString))

def repeat(dict_a, f):
    for key, value in dict_a.items():   # iter on both keys and values
        if key.startswith(f[:-8]):
                dict_a.pop(f[:-4])
def concat(*args, sep=" - "):
    return sep.join(args)

def xstr(s):
     return s or ""

def ID3_tag(full_path):
            try:
                audio = ID3(full_path)
            except ID3NoHeaderError:
                print("Adding ID3 header;")
                audio = ID3()
            
            if "TPE1" in audio:
                artist = audio['TPE1'].text[0]
            else:
                artist = ""
            if "TALB" in audio:
                album = audio['TALB'].text[0]
            else:
                album = ""            
            if "TRCK" in audio:
                tracks = audio['TRCK'].text[0].split("/")
                if len(tracks[0]) > 1:
                    track = "0" + tracks[0]
                else:
                    track = tracks[0]
            else:
                track = ""
            if "TIT2" in audio:
                song = audio['TIT2'].text[0]
            else:
                song = ""
            return (artist, album, track, song)

dict_a = {}
mylist = []
audio_book = ["George R.R. Martin", "Yuval Harari", "Jon Stewart", "Stephen Colbert"]

# store list of all files in a folder
only_files = [f for f in listdir(MyPath) if isfile(join(MyPath, f))]

if __name__ == "__main__":

    for f in only_files:
        MySize = getsize(join(MyPath, f))
        if ".mp3" in f:
            # if MySize < 1536000:
            #     remove(join(MyPath, f))
                filemp3 = f[:-4]
                dict_a[filemp3] = MySize
                #repeat(dict_a, f)

    for key in glob.glob(MyPath + '*([3-99]).mp3'):
        only_files.remove(key[22:])
        try:
            only_files.remove(key[22:-8] + ".mp3")
            only_files.remove(key[22:-8] + " (1)" + ".mp3")
            only_files.remove(key[22:-8] + " (2)" + ".mp3")
        except:
            pass

    for f in only_files:
        # store just name, w/o ext
        filemp3 = f[:-4]
        full_path = join(MyPath, f)
        full_path_alt = join(MyPath, filemp3[:-4] + ".mp3")
        #ID3_tag(full_path)
        try:
            audio = ID3(full_path)
        except ID3NoHeaderError:
            #print("Adding ID3 header;")
            audio = ID3()
            
        if "TPE1" in audio:
            artist = audio['TPE1'].text[0]
        else:
            artist = ""
        if "TALB" in audio:
            album = audio['TALB'].text[0]
        else:
            album = ""            
        if "TRCK" in audio:
            tracks = audio['TRCK'].text[0].split("/")
            if len(tracks[0]) > 1:
                track = "0" + tracks[0]
            else:
                track = tracks[0]
        else:
            track = ""
        if "TIT2" in audio:
            song = audio['TIT2'].text[0]
        else:
            song = ""
        # verify if name inludes (1) (2)
        if hasNumbers(filemp3):            
            if len(filemp3) < 8:                
                # try:
                    new_full_path = MyPath + artist + " - " + album + " - " + track + " - " + song + ".mp3"
                    # new_full_path = MyPath + " - " + xstr(artist) + " - " + xstr(album) + " - " + xstr(track) + " - " + xstr(song) + ".mp3"
                    print("len < 8: " + new_full_path)
                    # new_full_path = concat(artist, album, track, song)
                    #rename(full_path, new_full_path)
                # except:
                #     print("no ID3 on: " + filemp3)
            else:
                try:
                    # if (1) smaller or equal
                    if dict_a[filemp3] <= dict_a[filemp3[:-4]]:
                        #remove(full_path)
                        print("dict(1) < dict: " + full_path)                           
                    else:
                        #remove(full_path_alt)
                        #rename(full_path, full_path_alt)
                        print("dict < dict(1): " + full_path)
                except:
                   # rename(full_path, full_path_alt) 
                   print(full_path_alt)
        
        for item in audio_book:
        #if any(x in artist for x in audio_book):
            if item in artist:
                print(f + " - " + item)
                # rename(full_path, MyPath + "audiobooks\\" + f)



# if __name__ == "__main__":
#     # traverse root directory, and list directories as dirs and files as files
#     for root, dirs, files in os.walk("C:\\Users\\wiNejc\\Music\\"):
#         #path = root.split(os.sep)
#         #print(path)
#         #print(os.path.basename(root))
        
#         for file in files:
#             try:
#                 # print(file)
#                 # print(root)
#                 print(root + file)
#                 # audio = MP3(root + "\\" + file)
#                 # print(audio)
#                 # duration = audio.info.length
#                 # da[file] = duration
#                 # print(duration)
#             except:
#                 print >> MyLog, "error on " + file