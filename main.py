import os
import shutil
import schedule
import time
from download_insta import download
from make_compilation import makeCompilation
from upload_video import upload

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def job(length, output_dir, download_dir):
    # Create necessary directories
    create_directory(download_dir)
    create_directory(output_dir)

    # Download videos
    print("Downloading videos...")
    download(length)

    # Create video compilation
    print("Creating video...")
    makeCompilation(path="./downloads", totalVidLength=59, maxClipLength=59, outputFile=f"{output_dir}/vid1.mp4")

    # Upload video
    print("Uploading video...")
    upload()

    # Clean up directories
    shutil.rmtree("downloads")
    shutil.rmtree("videos")

if __name__ == "__main__":
    length = 5
    output_dir = "./videos"
    download_dir = "./downloads"

    job(length, output_dir, download_dir)

    # Schedule the job to run once a day
    #schedule.every().day.do(job, length, output_dir, download_dir)

    # Keep the script running
    #while True:
        #schedule.run_pending()
        #time.sleep(1)
