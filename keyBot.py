from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pynput.keyboard import Key, Listener
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://10fastfingers.com/typing-test/english")

def on_release(key):
    if key == Key.f2:
        start()

def start():
    try:
        html = driver.page_source
        html_soup = BeautifulSoup(html, 'html.parser')
        words = html_soup.find('div', attrs={"id":"row1"}).text.split(" ")
        del words[-1]
        del words[-1]
        inputBox = driver.find_element(By.XPATH, """//*[@id="inputfield"]""")
        timeout = time.time() + 60
        for word in words:
            if time.time() > timeout:
                break
            for letter in word:
                inputBox.send_keys(letter)
                time.sleep(0.05)
            inputBox.send_keys(" ")
    except Exception as e:
        print(e)

with Listener(on_release=on_release) as listener:
    listener.join()