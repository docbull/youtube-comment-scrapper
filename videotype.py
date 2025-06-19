from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pyautogui import alert
import time

class CrawlingStrategy:
    def run(self, driver, url):
        raise NotImplementedError

class LongFormCrawler(CrawlingStrategy):
    def run(self, driver):
        # waiting for comment box to be shown
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "comments")))
        driver.execute_script('window.scrollTo(0, 600);')

        title = driver.find_element(By.ID, 'title').text.strip().replace('/', '_')

        comments_len = -1
        while True:
            comments_loaded = driver.find_elements(By.XPATH, '//*[@id="comment"]')
            if len(comments_loaded) == comments_len:
                break

            comments_len = len(comments_loaded)
            driver.execute_script('window.scrollBy(0, document.documentElement.scrollHeight);')
            time.sleep(1.5)

        comments = []
        for comment_element in comments_loaded:
            try:
                comments.append({
                    '아이디': comment_element.find_element(By.ID, 'author-text').text.strip(),
                    '날짜': comment_element.find_element(By.ID, 'published-time-text').text.strip(),
                    '댓글': comment_element.find_element(By.ID, 'content-text').text.strip(),
                    '좋아요': comment_element.find_element(By.ID, 'vote-count-middle').text.strip(),
                })
            except NoSuchElementException:
                continue

        return title, comments

class ShortFormCrawler(CrawlingStrategy):
    def run(self, driver):
        try:
            # waiting for comment box is clickable
            comment_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "comments-button")))
            comment_button.click()
        except TimeoutException:
            alert(f'시간 내에 웹 페이지를 불러오지 못 했습니다')

        meta_title = driver.find_elements(By.XPATH, '//meta[@name="title"]')
        title = meta_title[0].get_attribute("content")

        comments_len = -1
        while True:
            comments_loaded = driver.find_elements(By.XPATH, '//*[@id="comment"]')
            if len(comments_loaded) == comments_len:
                break
            
            comments_len = len(comments_loaded)

            comment_container = driver.find_element(By.ID, "contents")
            comment_box = comment_container.find_element(By.ID, "contents")
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight;', comment_box)
            time.sleep(1.5)

        comments = []
        for comment_element in comments_loaded:
            try:
                comments.append({
                    '아이디': comment_element.find_element(By.ID, 'author-text').text.strip(),
                    '날짜': comment_element.find_element(By.ID, 'published-time-text').text.strip(),
                    '댓글': comment_element.find_element(By.ID, 'content-text').text.strip(),
                    '좋아요': comment_element.find_element(By.ID, 'vote-count-middle').text.strip(),
                })
            except NoSuchElementException:
                continue

        return title, comments