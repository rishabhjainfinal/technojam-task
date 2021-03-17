from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep as nap
import os
from pathlib import Path

class Twitter_bot:
    def __init__(self,username,passwd):
        self.username = username
        self.passwd = passwd
        print("setup drivers",end='')
        self.driver = webdriver.Chrome('chromedriver.exe')
        print(" ..successful")
        self.login_url = "https://twitter.com/login/"
        self.logout_url = "https://twitter.com/logout/"
        self.new_tweet = "https://twitter.com/compose/tweet"

    def __enter__(self):
        self.login()
        return self
    
    def __exit__(self,a,b,c):
        nap(3) # to complete any pending message
        self.logout()

    def login(self):
        # make login to the account
        print(f"opening {self.login_url}")
        self.driver.get(self.login_url)
        
        # find the username and password fields
        username_field = '//input[@name="session[username_or_email]"]'
        passwd_field = '//input[@name="session[password]"]'
        login_btn = '//div[@role="button"]//*[contains(text(),"Log in")]'
        
        # wait till element to appear on the screen
        self.execute_when_element_on_screen(username_field)

        # find the field on the pages
        username = self.driver.find_element_by_xpath(username_field)	
        password = self.driver.find_element_by_xpath(passwd_field)	
        login = self.driver.find_element_by_xpath(login_btn)
        
        # sending username and password 
        username.send_keys(self.username)
        password.send_keys(self.passwd)
        login.click()
        
        print("Making new Login.")

    def logout(self):
        # make logout form the account from the home page
        self.driver.get(self.logout_url)

        # find the log out fields
        logout_filed = '//div[@role="button"]//*[contains(text(),"Log out")]'

        # wait till element to appear on the screen
        self.execute_when_element_on_screen(logout_filed)

        logout = self.driver.find_element_by_xpath(logout_filed)
        logout.click()
        print("Making Log out.")

    def post_new_tweet(self,message = "",image_path = None):
        # post new tweet 
        '''type message: string'''
        self.driver.get(self.new_tweet)

        # input field
        text_field = '//div[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]'
        media_field = '//*[@accept="image/jpeg,image/png,image/webp,image/gif,video/mp4,video/quicktime,video/webm"]'
        post_btn = '//*[@aria-labelledby="modal-header"]//*[contains(text(),"Tweet")]'
        if message:
            print("Adding new message - ",message)
            self.execute_when_element_on_screen(text_field)
            text = self.driver.find_element_by_xpath(text_field)
            text.send_keys(message)
            nap_time = 1
        
        if image_path:
            nap(1) # to load the page 
            print("Adding new image - ",image_path)
            add_image = self.driver.find_element_by_xpath(media_field)
            add_image.send_keys(image_path)
            nap_time = 3

        # send post
        if message or image_path:
            self.execute_when_element_on_screen(post_btn)
            post_it = self.driver.find_element_by_xpath(post_btn)
            post_it.click()
            print("New Tweet posted.")
            nap(nap_time) # to post the message or image successfully

    def execute_when_element_on_screen(self,xpath,time=10):
        print(f"Waiting for {xpath} to appear.")
        WebDriverWait(self.driver, float(time)).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    
    @classmethod
    def runner(cls,username,passwd):
        with cls(username,passwd) as bot:
            # read the tweet and post it 
            tweet_list = open("tweet.txt",'r').read().split("\n\n")
            for i in tweet_list:
                bot.post_new_tweet(message = i)
            bot.post_new_tweet(message = "",image_path = os.path.join(Path.home(),'Desktop','a.PNG'))

if __name__ == "__main__":
    username = "<username>"
    passwd = "<password>"
    Twitter_bot.runner(username,passwd)