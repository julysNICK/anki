import csv
from selenium import webdriver
import time
import re
from selenium.common.exceptions import NoSuchElementException

words = []
exitProgram = False


def formatSetence(word):
   specialCharacters = re.findall(r'[^\w\s]', word)
   
   if len(specialCharacters) == 0:
       return word

   if len(specialCharacters) > 0:
        for character in specialCharacters:
            word = word.replace(character + " ", character)
   finalText = word

   return finalText


def sentenceOrWord(word):
    if " " in word:
        return "sentence"
    else:
        return "word"


def translate(word):
    setence_word = sentenceOrWord(word)

    driver = webdriver.Firefox()
    driver.get(
        "https://translate.google.com/#view=home&op=translate&sl=en&tl=pt&text=" + formatSetence(word))
    time.sleep(5)

    try:
        if setence_word == "word":
            print("word")
            # translation = driver.find_element_by_xpath(
            #     '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span/span').text
            translation = driver.find_element("xpath","/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]/span[1]/span/span").text
        else:
            print("sentence")
            # translation = driver.find_element_by_xpath(
            #     /html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]/span[1]/span/span
            translation = driver.find_element("xpath","/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]/span[1]/span/span").text

    except NoSuchElementException:
        print("word")
        # translation = driver.find_element_by_xpath(
        #     '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div[1]/div[1]/span[1]').text
        translation = driver.find_element("xpath","/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[9]/div/div[1]/span[1]/span/span").text
        driver.quit()
    driver.quit()
  
    return translation


def add_to_csv():
    try:
        with open('words.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            for word in words:
                spamwriter.writerow([word[0], word[1]])
    except FileNotFoundError:
        with open('words.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            for word in words:
                spamwriter.writerow([word[0], word[1]])


while exitProgram == False:
    word = input("Enter a word to translate: ")
    if word == "exit":
        exitProgram = True

    else:
        formattedWord = formatSetence(word)
        translation = translate(word)
        print(translation)
        words.append([word, translation])
        add_to_csv()
        words.clear()
        print(words)
