from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

import numpy as np
import pandas as pd

# import pyautogui
from pyautogui import alert

def initialize_driver():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    return driver

# get_youtube_comments crawls youtube comments that contains author, published time, comment, and the number of likes
def get_youtube_comments(video_url, selected_folder):
    if video_url == "" :
        alert(f"올바른 URL을 입력해주세요")
        return

    if selected_folder == "" :
        alert("폴더를 선택해주세요")
        return

    try:
        driver = initialize_driver()

        # open youtube page
        driver.get(video_url)

        # wait 3s for loading the page
        time.sleep(3)

        # crawl comments ...
        driver.execute_script('window.scrollTo(0, 1000);')

        fold = driver.find_element(By.ID, 'above-the-fold')
        title = fold.find_element(By.ID, 'title').text

        comment_len = 0
        while True:
            comment_box = driver.find_elements(By.XPATH, '//*[@id="comment"]')
            
            if comment_len == len(comment_box):
                break
            else:
                driver.execute_script('window.scrollBy(0, document.documentElement.scrollHeight);')
                comment_len = len(comment_box)
            
            time.sleep(1.5)

        comments = []
        comment_box = driver.find_elements(By.XPATH, '//*[@id="comment"]')
        for comment_element in comment_box :
            author = comment_element.find_element(By.ID, 'author-text').text
            publish = comment_element.find_element(By.ID, 'published-time-text').text
            comment = comment_element.find_element(By.ID, 'content-text').text
            likes = comment_element.find_element(By.ID, 'vote-count-middle').text
            comments.append({'author': author, 'publish': publish, 'comment': comment, 'likes': likes})
        
        # save comments to excel file
        save_comments_into_excel(selected_folder, title, comments)
    except Exception as e:
        alert(f"올바른 URL을 입력해주세요 {e}")
        
    # end of driver
    driver.quit()



# save_comments_into_excel creates an excel file for writing the comments
def save_comments_into_excel(selected_folder, title, comments):
    try:
        authors = []
        publishes = []
        texts = []
        likes = []
        for comment in comments :
            authors.append(comment['author'])
            publishes.append(comment['publish'])
            texts.append(comment['comment'])
            likes.append(comment['likes'])

        df = pd.DataFrame({
            '아이디': authors,
            '날짜': publishes,
            '댓글': texts,
            '좋아요': likes,
        })

        file_name = f"{selected_folder}/{title}.xlsx"
        df.to_excel(file_name, index=False, engine="openpyxl", header=True, startrow=0, freeze_panes=(1, 1))

        alert(f"{title} 댓글 저장 완료")
    except Exception as e:
        alert(f"파일 저장 중 에러 >> {e}")

# video_url = "https://www.youtube.com/watch?v=rG2Q5uiqiAs"
# get_youtube_comments(video_url)