from selenium import webdriver
from lessons import *
from time import sleep
from os import system

profile_path = '--user-data-dir=/Users/davidohayon/Library/Application Support/Google/Chrome/'

print(schedule())

if not which_lesson(True):
    print("there's no class right now.\n")
    quit()

system("osascript -e \'quit app \"Google Chrome\"\'")

sleep(3)

options = webdriver.ChromeOptions()
options.add_argument(profile_path)
driver = webdriver.Chrome(options=options)

sleep(1)
driver.execute_script("window.open();")
sleep(1)
driver.switch_to.window(driver.window_handles[1])
driver.get(which_lesson(True))
sleep(2.5)
driver.close()
sleep(1)
driver.quit()

system('open -a "Google Chrome"')
