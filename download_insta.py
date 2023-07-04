import instaloader
import random

def get_account():
    with open("accounts.txt", 'r', encoding='utf-8') as f:
        accounts = [line.strip() for line in f]
    return random.choice(accounts)

def download(length):
    ig = instaloader.Instaloader(download_pictures=False,
                                 download_video_thumbnails=False,
                                 download_geotags=False,
                                 download_comments=False,
                                 save_metadata=False,
                                 compress_json=False)

    ig.login("bngcrash87", "yourpassword")  # change this :)
    profile = instaloader.Profile.from_username(ig.context, get_account())
    
    download_folder = "downloads"
    for count, post in enumerate(profile.get_posts()):
        if post.is_video:
            ig.download_post(post, target=download_folder)
            if count + 1 == length:
                break
