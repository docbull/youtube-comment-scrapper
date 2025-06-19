from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from videotype import LongFormCrawler, ShortFormCrawler

from pyautogui import alert
import numpy as np
import pandas as pd
import time
import os

# initiates driver ...
def initialize_driver():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# save_comments_to_excel creates an excel file for writing the comments
def save_comments_to_excel(folder, title, comments):
    try:
        df = pd.DataFrame(comments)
        if df.empty:
            alert("댓글이 없습니다")
            return
        
        file_path = os.path.join(folder, f"{title}.xlsx")
        df.to_excel(file_path, index=False, engine="openpyxl", header=True, startrow=0, freeze_panes=(1, 1))
        alert(f"{title} 댓글 저장 완료")
    except Exception as e:
        alert(f"파일 저장 중 오류 발생: {e}")

# get_youtube_comments crawls youtube comments that contains author, published time, comment, and the number of likes
def get_youtube_comments(video_url, selected_folder):
    if video_url == "" :
        alert(f"올바른 URL을 입력해주세요")
        return

    if selected_folder == "" or selected_folder == "저장 경로를 설정해주세요" :
        alert("폴더를 선택해주세요")
        return
    
    driver = None
    try:
        driver = initialize_driver()

        # open youtube page with given url
        driver.get(video_url)
        time.sleep(3)

        strategies = {
            "long": LongFormCrawler(),
            "short": ShortFormCrawler(),
        }
        
        video_type = None
        try:
            is_short = driver.find_element(By.ID, 'shorts-panel-container')
            video_type = "short"
        except NoSuchElementException as e:
            # this video is a long-form content
            video_type = "long"

        strategy = strategies.get(video_type)
        title, comments = strategy.run(driver)
        save_comments_to_excel(selected_folder, title, comments)
    except Exception as e:
        print(e)
        alert(f"오류 발생: {e}")
    
    driver.quit()