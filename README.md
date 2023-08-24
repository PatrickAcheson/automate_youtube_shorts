# Fully Automated Instagram to YouTube Shorts Channel

This project contains code to run a fully automated YouTube channel that can scrape video content from Instagram, convert them into YouTube shorts, and upload them daily to your YouTube channel.

## INSTALOADER IS BROKEN - download_insta.py wont work ##

## Instructions

1. **Clone the GitHub Repository**

   Clone this repository to your local machine.

2. **Install Python3 and pip**

   If not already installed, download and install Python3 and pip.

3. **Install Required Libraries**

   Install the necessary libraries using pip by running `pip3 install -r requirements.txt` or `python3 -m pip install -r requirements.txt`.

4. **Setup Instagram Account**

   Create an Instagram account and add all the accounts you like into the `accounts.txt`.

5. **Configure Instagram Credentials**

   Open `download_insta.py` in a text editor and fill in your Instagram credentials in the # change here line.
   
7. **Install Chrome Beta**

   Install and configure your PATHs inside the `upload_video.py` file. ( watch my youtube video if stuck :) ).

8. **Login to your YouTube channel**

   Open the Chrome Beta browser and login to your YouTube channel, close the browers after doing so. (or it will break)

9. **Run the Script**

   Run `python3 main.py` in your terminal or command prompt. Every 24 hours, the script will start scraping videos from the Instagram accounts, convert them into YouTube shorts, and upload them to your YouTube channel.

Known Issues: 
- Sending to many requests will results in a '429 - Too Many Requests' error in the cli - this seems to be a temp ban of 24 hours.
- Additionaly, make sure you are logged out of instagram when running the script or you will likely get an error.
- Google Chrome Beta needs to be closed before running the script.

Enjoy your fully automated Instagram to YouTube shorts channel! Note that you can edit variables inside `main.py` to customize things such as the maximum clip length. Have fun!
