# Simple code for an instagram bot

##########################################################
#importing the libraries required

from selenium import webdriver
import time

#########################################################

#creating a class InstaBot

class Instabot:

    def __init__(self, username, password):

        self.username = username
        self.password = password

        self.insta_url = "https://www.instagram.com"

    def driver_func(self):

        self.driver = webdriver.Chrome(executable_path = '.\Chromedriver\chromedriver')
        self.driver.maximize_window()
        self.login()
    
    #login function - which allows to login into the instagram by automatically typing your username and password

    def login(self):

        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        time.sleep(1)

        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        time.sleep(3)

        save_info_button = self.driver.find_element_by_xpath("//*[contains(@class,'sqdOP yWX7d    y3zKF     ')]")
        save_info_button.click()
        time.sleep(2)
        notification_button = self.driver.find_element_by_xpath("//*[contains(@class,'aOOlW   HoLwm ')]")
        notification_button.click()
        time.sleep(2)

    #for accessing insta home page 

    def home(self):

        self.driver_func()
        time.sleep(1)
        home_button = self.driver.find_element_by_class_name("Fifk5")
        home_button.click()

    #for accessing your insta profile

    def profile(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]").click()
        time.sleep(1)
        self.driver.find_element_by_class_name("-qQT3").click()


    #follow function

    def follow(self):

        for i in range(10):
            follow_button = self.driver.find_element_by_xpath("//*[contains(@class,'sqdOP  L3NKy   y3zKF     ')]")
            follow_button.click()
            time.sleep(2)

    #visiting a profile

    def nav_user(self, user):

        self.driver_func()
        self.driver.get("{}/{}/".format(self.insta_url,user))


    #following a person

    def follow_nav_user(self, user):

        self.nav_user(user)
        time.sleep(1)
        follow_button_nav = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')
        follow_button_nav.click()

    #following suggested followers
    
    def follow_suggested_users(self):

        self.driver_func()
        see_all_users = self.driver.find_element_by_xpath("//*[contains(@class,'_7UhW9  PIoXz        qyrsm KV-D4          uL8Hv         ')]")
        see_all_users.click()
        time.sleep(2)
        self.follow()
        self.profile()

    #unfollowing several followers
        
    def unfollow(self):

        self.driver_func()
        self.profile()
        time.sleep(1)
        following_list = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]")
        following_list.click()
        time.sleep(2)

        for i in range(5):
            unfollow_button = self.driver.find_element_by_xpath("//*[contains(@class,'sqdOP  L3NKy    _8A5w5    ')]")
            unfollow_button.click()
            time.sleep(1)
            unfollow_confirmation = self.driver.find_element_by_xpath("//*[contains(@class,'aOOlW -Cab_   ')]")
            unfollow_confirmation.click()
            time.sleep(1)

        cancel_button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]")
        cancel_button.click()
        self.profile()

    #unfollowing a person
    
    def unfollow_nav_user(self, user):

        self.nav_user(user)
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[contains(@class,'_5f5mN    -fzfL     _6VtSN     yZn4P   ')]").click()
        time.sleep(1)
        unfollow_button = self.driver.find_element_by_xpath("//*[contains(@class,'aOOlW -Cab_   ')]")
        unfollow_button.click()
        time.sleep(2)
        self.profile()

    #function for liking the posts

    def like_posts(self):
        photo = self.driver.find_element_by_class_name('eLAPa')
        photo.click()

        for i in range(20):
            time.sleep(2)
            like_button = self.driver.find_element_by_class_name('fr66n')
            like_button.click()
            time.sleep(1)
            next_img = self.driver.find_element_by_xpath("//*[contains(@class,' _65Bje  coreSpriteRightPaginationArrow')]")
            next_img.click()

    #like a persons uploaded photos
    
    def like_user_posts(self, user):

        self.nav_user(user)
        time.sleep(2)
        self.like_posts()
        time.sleep(1)
        self.driver.get("{}/{}/".format(self.insta_url,user))

    #following the followers of a person

    def follow_nav_user_followers(self, user):

        self.nav_user(user)
        time.sleep(1)
        followers_list = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
        followers_list.click()
        time.sleep(1)
        self.follow()
        cancel_button = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]")
        cancel_button.click()
        time.sleep(1)



#############################################################

#main 


if __name__ == '__main__':

    print('''

          _____                  _                ____            _
         |_   _|                | |              |  _ \          | |
           | |    _ ___    ___  | |_     __ _    | |_) |   ___   | |_
           | |   |  _  |  / __| | __/  /  _| |   |  _ <   / _ \  | __/
          _| |_  | | | |  \ \   | |__  | (_| |   | |_) | | (_) | | |__
         |_____| |_| |_| |___/  \____| \___\_|   |____/   \___/  \____|

            ''')
    


    #reading the input username and password
    

    username = input("Username : ")

    password = input("Password : ")

    ig_bot = Instabot(username,password)

    print("""----Functions----\n\n1)Login to home page\n2)Follow suggested users(10)\n3)Visit a profile
4)Follow a person\n5)Like a friend's posts(20)\n6)Follow a friend's followers(10)\n7)Unfollow a person
8)Unfollow 10 recent following\n""")



    operation = int(input("Select any (Enter the number corrsponding to the required function): "))

    #dictionary contains functions and corresponding number

    operations = {
    1 : ig_bot.driver_func,
    2 : ig_bot.follow_suggested_users,
    3 : ig_bot.nav_user,
    4 : ig_bot.follow_nav_user,
    5 : ig_bot.like_user_posts,
    6 : ig_bot.follow_nav_user_followers,
    7 : ig_bot.unfollow_nav_user,
    8 : ig_bot.unfollow,
    }


    #actions which we need to pass an argument
    actions = [3, 4, 5, 6, 7]

    if operation in actions:

        user = input("Enter the insta id of the person : ")
        operations.get(operation)(user)

    else:
        operations.get(operation)()
