from moviepy.editor import VideoFileClip, concatenate_videoclips
import os
from os.path import isfile, join
import random

def makeCompilation(path,
                    totalVidLength,
                    maxClipLength,
                    outputFile):

    allVideos = []
    totalLength = 0

    for fileName in os.listdir(path):
        filePath = join(path, fileName)
        if isfile(filePath) and fileName.endswith(".mp4"):
            print(fileName)
            clip = VideoFileClip(filePath)

            # If clip duration > maxClipLength, shorten it
            if clip.duration > maxClipLength:
                clip = clip.subclip(0, maxClipLength)

            allVideos.append(clip)

    random.shuffle(allVideos)

    videos = []
    for clip in allVideos:
        if totalLength + clip.duration > totalVidLength:
            # If adding the whole clip exceeds totalVidLength, trim it
            clip = clip.subclip(0, totalVidLength - totalLength)
        videos.append(clip)
        totalLength += clip.duration
        if totalLength >= totalVidLength:
            break

    finalClip = concatenate_videoclips(videos, method="compose")

    audio_path = os.path.join(os.path.dirname(outputFile), "temp_audiofile.m4a")
    # update threads= accordingly
    finalClip.write_videofile(outputFile, threads=12, temp_audiofile=audio_path, remove_temp=True, codec="libx264", audio_codec="aac")

    print(f'Created {outputFile} with a duration of {totalLength} seconds.')







