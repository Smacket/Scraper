#!/usr/bin/env python3
from selenium import webdriver
import time
#TODO: Use beautiful soup to extract the correct youtube URLs from smashvods
#      Navigate to an arbitrary time in the video e.g.:
#       - https://www.youtube.com/watch?v=BD5eP6lk32A
#       - becomes --> https://www.youtube.com/watch?v=BD5eP6lk32A&t=200s
#      Full Screen the video, and take screenshot with filename corresponding to names and characters
#      Pulled from Beautiful Soup

CHARACTERS = [
    "Banjo",
    "Bayonetta",
    "Bowser",
    "Mario"
        ]



def main():
    browser = webdriver.Chrome()
    URL = "https://sf.vods.co/ultimate/character"
    
    for charA in CHARACTERS:
        for charB in CHARACTERS:
            if charA == charB:
                break

            browser.get(URL + charA + "/character2/" + charB)
            time.sleep(3)
            vodTableList = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/div/section/div/div/div/div')
            for tR in vodTableList.find_elements_by_css_selector('tr'):
                linkElement = tR.find_elements_by_css_selector('td')[2]
                smashVodsLink = linkElement.find_element_by_css_selector('a').get_attribute('href')
                print(smashVodsLink) 
    #browser.save_screenshot('image.png')
    browser.quit()

if __name__ == "__main__":
    main()
