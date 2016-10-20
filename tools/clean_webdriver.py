"""
this module used to kill all the webdrivers & browsers after the jenkins job execution done.
"""
import os

if "__main__" == __name__:
    os.system("taskkill /f /im chrome.exe")
    os.system("taskkill /f /im chromedriver.exe")
    os.system("taskkill /f /im firefox.exe")
    os.system("taskkill /f /im iexplore.exe")
    os.system("taskkill /f /im IEDriverServer.exe")
    os.system("taskkill /f /im phantomjs.exe")
