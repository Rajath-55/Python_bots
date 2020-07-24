from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

users = ['rajath_5', 'sonick_panick', 'sush._.n', 'anagha_shree']


class InstagramBot():
    def __init__(self, email, password):
        PATH = '/home/rajath/Desktop/chromedriver'
        self.browser = webdriver.Chrome(PATH)
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get(
            'https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(5)

        emailInput = self.browser.find_element_by_name('username')
        passwordInput = self.browser.find_element_by_name('password')
        print(emailInput, passwordInput)
        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def followWithUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(4)  # not necessary
        followButton = self.browser.find_element_by_xpath(
            '//button[text()="Follow"]')
        followButton.click()

    def getUserFollowers(self, username, max):
        self.browser.get('https://www.instagram.com/' + username)
        followersLink = self.browser.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(4)
        followersList = self.browser.find_element_by_css_selector(
            'div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(
            followersList.find_elements_by_css_selector('li'))

        followersList.click()
        actionChain = webdriver.ActionChains(self.browser)
        while (numberOfFollowersInList < max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(
                followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)

        followers = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector(
                'a').get_attribute('href')
            print(userLink)
            followers.append(userLink)
            if (len(followers) == max):
                break
        return followers


bot = InstagramBot('pythonraj55@gmail.com', 'Testpassword123')
bot.signIn()
for user in users:
    # bot.followWithUsername(user)
    userFollowers = bot.getUserFollowers(user, 100)
