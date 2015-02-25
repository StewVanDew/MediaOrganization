import os

#Variables
sourceFolder = "Z:\Torrents"
moviesDest = "J:\Media\Movies"
musicDest = "J:\Media\Musicc"
imageDest = "J:\Media\Photos"
image_ext = ('.bmp', '.gif', '.jpg', '.png', '.psd')
music_ext = ('raw', 'flac', 'mp2', 'mp3', 'aac', 'wma', 'wv', 'm3u', 'm4a', 'mpa', 'wav', 'ra',)
video_ext = ('3g2', '3gp', 'asf', 'asx', 'avc', 'avi', 'avs', 'bivx', 'bup', 'divx', 'dv', 'dvr-ms', 'evo', 'fli',
             'flv', 'm2t', 'm2ts', 'm2v', 'm4v', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'mts', 'nsv', 'nuv', 'ogm',
             'ogv', 'tp', 'pva', 'qt', 'rm', 'rmvb' 'sdp', 'svq3', 'strm', 'ts', 'ty', 'vdr', 'viv', 'vob', 'vp3',
             'wmv', 'wpl', 'wtv', 'xsp', 'xvid', 'webm')
video_count = 0
song_count = 0
image_count = 0

for dirPath, dirNames, files in os.walk(sourceFolder): #Getting all the directories and subdirectories
    for file in os.listdir(dirPath):
        if file.endswith(video_ext):#Checking if it is a video file
            video_count += 1
            filestr = str(file)
            foundFile = os.path.realpath(os.path.join(dirPath, filestr))#Creating a absolute path to the file to be moved
            destPath = os.path.realpath(os.path.join(moviesDest, filestr))#Finding out where to put the file
            os.rename(foundFile, destPath)#Moving the file to the new folder (This is only the file
            """Need to work on being able to take the parent folder of the file and move that instead of moving just the media file
            from what i have seen It might be easy to just scan the sub directories and move each file one by one. First check for
            being able to move a full directory in python"""
            print(foundFile)#Little visual for debugging and proving that it worked :)
        elif file.endswith(music_ext):#Checking if it is a music file
            song_count += 1
            filestr = str(file)
            foundFile = os.path.realpath(os.path.join(dirPath, filestr))#See Above
            destPath = os.path.realpath(os.path.join(musicDest, filestr))
            print(foundFile)
        elif file.endswith(image_ext):
            image_count += 1
            filestr = str(file)
            foundFile = os.path.realpath(os.path.join(dirPath, filestr))
            destPath = os.path.realpath(os.path.join(imageDest, filestr))
            print(foundFile)
        pass
print("You have a total of {0} video files, {1} music files, and {2} image files".format(video_count, song_count
                                                                                         , image_count))#Just so we can see how many files we moved.


"""Future ideas:
        -Logging to see what movie has been moved
        -moving the parent folder of a file(This is a priority)
        -For music look into song info module to allow for complete songs.
        -Movies see if I can find an API for IMDB to start getting proper titles for directories(Stupid torrent people)
"""





