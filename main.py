import random
from dotenv import load_dotenv
import os
import time
from instagrapi import Client

def get_account():
    with open("accounts.txt", 'r', encoding='utf-8') as f:
        accounts = [line.strip() for line in f]
    return random.choice(accounts)

def load_env():
    load_dotenv()
    username = os.getenv("USER_NAME")
    password = os.getenv("PASS_WORD")
    print("Account details ready.")
    return username, password

def login_with_retry(username, password, max_attempts=5):
    cl = Client()
    for attempt in range(max_attempts):
        try:
            cl = Client()
            iphone_user_agent = "Instagram 272.0.0.14.73 (iPhone14,2; iOS 15_4_1; en_US; en-US; scale=3.00; 1170x2532; 382468104)" # keep or chnage
            cl.set_user_agent(iphone_user_agent)
            cl.login(username, password)
            return cl
        except Exception as e:
            print(f"Login attempt {attempt + 1} failed: {e}")
            time.sleep((2 ** attempt) + random.random())
    print("Failed to log in after multiple attempts")
    return None

def download(length):
    username, password = load_env()
    cl = login_with_retry(username, password)
    
    if not cl:
        print("Could not log in. Exiting.")
        return

    target_account = get_account()
    print(f"Downloading from account: {target_account}")
    
    try:
        user_id = cl.user_id_from_username(target_account)
        medias = cl.user_medias(user_id, amount=length)
        
        download_folder = "downloads"
        os.makedirs(download_folder, exist_ok=True)
        
        for count, media in enumerate(medias):
            if media.media_type == 2:  # Type 2 is video content
                print(f"Downloading video {count + 1}/{length}")
                cl.video_download(media.pk, folder=download_folder)
            
            if count + 1 == length:
                break
        
        print(f"Downloaded {count + 1} videos successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
