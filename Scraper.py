#!/usr/bin/env python3
from selenium import webdriver
import time
URL = "https://sf.vods.co/ultimate/character"
CHARACTERS = [
    "Banjo",
    "Bayonetta",
    "Bowser",
    "Bowser Jr."
]

class VideoLink:
    def __init__(self, charA, charB):
        self.charA = charA
        self.charB = charB
        self.links = []
    
    def addLink(self, link):
        self.links.append(link)

    def getLinks(self):
        return self.links

    def display(self):
        print("%s vs %s:" % (self.charA, self.charB))
        for link in self.links:
            print(link, sep=", ", end="")

#Fill this out
def getScrotFromVideo(videoLinks):
    pass


def getVideoLinks(browser, charA, charB):
    temp = VideoLink(charA, charB)
    browser.get(URL + charA + "/character2/" + charB)
    vodTableList = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div[1]/div/section/div/div/div/div')
    for tR in vodTableList.find_elements_by_css_selector('tr'):
        linkElement = tR.find_elements_by_css_selector('td')[2]
        smashVodsLink = linkElement.find_element_by_css_selector('a').get_attribute('href')
        print("%s vs %s --> %s" % (charA, charB, smashVodsLink))
        temp.addLink(smashVodsLink)

    return temp

def main():
    browser = webdriver.Chrome()
    relevantLinks = []
    for charA in CHARACTERS:
        for charB in CHARACTERS:
            relevantLinks = getVideoLinks(browser, charA, charB)
            relevantLinks.display()

    browser.quit()

if __name__ == "__main__":
    main()
