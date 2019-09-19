#!/usr/bin/env python3
from selenium import webdriver

#TODO: Use beautiful soup to extract the correct youtube URLs from smashvods
#      Navigate to an arbitrary time in the video e.g.:
#       - https://www.youtube.com/watch?v=BD5eP6lk32A
#       - becomes --> https://www.youtube.com/watch?v=BD5eP6lk32A&t=200s
#      Full Screen the video, and take screenshot with filename corresponding to names and characters
#      Pulled from Beautiful Soup
def getURL():
    return "https://www.google.com"


def main():
    browser = webdriver.Firefox()
    URL = getURL()
    browser.get(URL)
    browser.save_screenshot('image.png')
    browser.quit()

if __name__ == "__main__":
    main()
