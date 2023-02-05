import csv
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

words = []
exitProgram = False


def sentenceOrWord(word):
    if " " in word:
        return "sentence"
    else:
        return "word"


def translate(word):
    setence_word = sentenceOrWord(word)

    driver = webdriver.Firefox()
    driver.get(
        "https://translate.google.com/#view=home&op=translate&sl=en&tl=pt&text=" + word)
    time.sleep(2)

    try:
        if setence_word == "word":
            print("word")
            translation = driver.find_element_by_xpath(
                '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span/span').text
        else:
            print("sentence")
            translation = driver.find_element_by_xpath(
                '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div[1]/div[1]/span[1]').text
    except NoSuchElementException:
        translation = driver.find_element_by_xpath(
            '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div[1]/div[1]/span[1]').text

    driver.quit()
    return translation


def add_to_csv():
    try:
        with open('words.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for word in words:
                spamwriter.writerow([word[0], word[1]])
    except FileNotFoundError:
        with open('words.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for word in words:
                spamwriter.writerow([word[0], word[1]])


while exitProgram == False:
    word = input("Enter a word to translate: ")
    if word == "exit":
        exitProgram = True
        add_to_csv()
    else:
        translation = translate(word)
        print(translation)
        words.append([word, translation])
        print(words)
