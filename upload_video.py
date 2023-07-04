import time, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def upload():
    # Create a service with the specified path
    service = Service(executable_path=r"C:\\Users\\patri\\Desktop\\auto_download\\chromedriver.exe") #change
    #option = webdriver.ChromeOptions()
    #option.add_argument("start-maximized")
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)

    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")
    options.add_argument("user-data-dir=C:\\Users\\patri\\AppData\\Local\\Google\\Chrome Beta\\User Data") #change
    options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe" # change

    # edit the time.sleep based on your connection/processing speed
    bot = webdriver.Chrome(service=service, options=options)

    bot.get("https://studio.youtube.com")
    time.sleep(3)
    upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
    upload_button.click()
    time.sleep(1)

    file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
    simp_path = 'videos/vid1.mp4'
    abs_path = os.path.abspath(simp_path)

    file_input.send_keys(abs_path)

    time.sleep(7)

    next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
    for i in range(3):
        next_button.click()
        time.sleep(1)

    done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
    done_button.click()
    time.sleep(5)
    bot.quit()
