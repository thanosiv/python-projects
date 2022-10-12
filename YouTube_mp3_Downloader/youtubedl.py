from pytube import YouTube # needs pytube to download stream
import config # config.path is used to store the download directory string
import os # used to change directory and split the path/filename and the extension
from moviepy import editor as mp # used to convert the mp4 to an mp3

os.chdir(config.path) # Set the path for where to save the file
    
# function to download a specific mp4 from YouTube  
def file_download():
    url = input('Enter the URL of the video you wish to download:- ')
    yt = YouTube(url) # Construct an instance of the YouTube class with the url variable as the base

    mp4 = yt.streams.filter(only_audio=True) # get only streams that are just audio
    mp4 = mp4.filter(mime_type='audio/mp4').order_by("abr").desc() # get only mp4, order by abr (audio quality) desc
    mp4dl = mp4[0].itag # get the highest audio quality in the list

    stream = yt.streams.get_by_itag(mp4dl) # get the stream to the itag
    strfile = stream.default_filename # get the filename that will be downloaded
    stream.download() # download the mp4
    
    return strfile # return the filename that gets downloaded

# function to convert an mp4 to an mp3
def file_convert(filename):
    vidfile = mp.AudioFileClip(filename + '.mp4') # set the source of the audioclip
    vidfile.write_audiofile(filename + '.mp3') # convert the .mp4 to an .mp3
    os.remove(filename + '.mp4') # delete the .mp4


f_name, f_ext = os.path.splitext(config.path + file_download()) # run the file_download() function, then split the filename and extension for the new file

file_convert(f_name) # run the file_convert function, passing the path/filename and extension as args

print('Download completed') # Print out completion message
