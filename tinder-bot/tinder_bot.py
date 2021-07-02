from selenium import webdriver
from time import sleep
import sys 
from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        sleep(5)

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)
        
        # click the login button                        
        login_btn = self.driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
        login_btn.click()
        
        sleep(2)
        
        # click the facebook login button 
        fb_btn = self.driver.find_element_by_xpath('//*[@id="u276642426"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()
        
        #switch to login popup tab
        base_window = self.driver.window_handles[0]
        #stay on the login popup tab
        self.driver.switch_to_window(self.driver.window_handles[1])
        
        #email 
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        
        #password
        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)
        
        #click facebook login button
        fb_login_btn = self.driver.find_element_by_id('loginbutton')
        fb_login_btn.click()
        
        sleep(5)
        
        # #switch to tinder tab page
        self.driver.switch_to_window(base_window)
        
        #click the allow button on tinder
        location_allow_btn = self.driver.find_element_by_xpath('//button[@aria-label="Allow"]/span[@class="Pos(r) Z(1) Fz($xs)" and text()="Allow"]');
        location_allow_btn.click()
        
        #click the notification button on tinder
        ntfcs_btn = self.driver.find_element_by_xpath('//button[@aria-label="Enable"]/span[@class="Pos(r) Z(1) Fz($xs)" and text()="Enable"]');
        ntfcs_btn.click()
        sleep(5)
        
    def like(self):
        #first //*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[4]/button
        #second //*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[5]/div/div[4]/button
        #css selectoru2005023502 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(4px\)--s.Pos\(r\) > div > div > div.Pos\(a\).B\(0\).Isolate.W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-like-green\) > button
        # like_btn = self.driver.find_element_by_css_selector('u2005023502 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(4px\)--s.Pos\(r\) > div > div > div.Pos\(a\).B\(0\).Isolate.W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-like-green\) > button')
        # like_btn.click()
        # //*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[4]/button
        like_btn = self.driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[4]/button')
        second_like_btn = self.driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[5]/div/div[4]/button')

        if like_btn.is_displayed:
            like_btn.click()
        elif second_like_btn.is_displayed():
            second_like_btn.click()
        else:
            print("Something went wrong in like()")
        
        # like_btn.click()
        
        # try:
        #     like_btn.click() 
        #     print("like button is clikced!")
        # except Exception:
        #     try:
        #         second_like_btn.click()
        #         print("Second like button is clicked!")
        #     except Exception:
        #         print("Something went wrong in like()")
        #         raise
                
        
        
    
    # def dislike(self):
    #     dislike_btn = self.driver.find_element_by_xpath('//*[@id="u2005023502"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[5]/div/div[2]/button')
    #     dislike_btn.click()
        
    def auto_swipe(self):
        while True:
            sleep(3)
            try:
                self.like()
            except Exception:
                self.close_match()
                print("Something went wrong in auto_swipe")
                break

    def close_match(self):
        """
        <button title="Back to Tinder" aria-label="Close" class="C($c-divider) Bdc($c-divider) Bdc($c-light-bluegray):h C($c-light-bluegray):h close P(0) Lh(1) Cur(p) focus-button-style Scale(1.2)"><svg class="Sq(24px) P(4px)" viewBox="0 0 24 24" width="24px" height="24px" focusable="false" aria-hidden="true" role="presentation"><path class="" d="M14.926 12.56v-1.14l5.282 5.288c1.056.977 1.056 2.441 0 3.499-.813 1.057-2.438 1.057-3.413 0L11.512 15h1.138l-5.363 5.125c-.975 1.058-2.438 1.058-3.495 0-1.056-.813-1.056-2.44 0-3.417l5.201-5.288v1.14L3.873 7.27c-1.137-.976-1.137-2.44 0-3.417a1.973 1.973 0 0 1 3.251 0l5.282 5.207H11.27l5.444-5.207c.975-1.139 2.438-1.139 3.413 0 1.057.814 1.057 2.44 0 3.417l-5.2 5.288z"></path></svg></button>
        match_popup_btn = self.driver.find_element_by_xpath('//button[@aria-label="Close"]/svg[@class="Sq(24px) P(4px)");
        #u-1959572593 > div > div > div.CenterAlign.M\(a\).Expand.Pos\(r\).Fx\(\$flx1\) > div > div.Pos\(a\).T\(0\).P\(20px\).P\(12px\)--xs.End\(0\) > button > svg
        Basically this element is not shown on html file, so go try to select hidden element
        after I clikc button myself and call auto_swipe function, it works
        //*[@id="u-1959572593"]/div/div/div[1]/div/div[4]/button
        """
        # sleep(3)
        # is_match_popup_btn = self.driver.find_element_by_xpath('//*[@id="u-1959572593"]/div/div/div[1]/div/div[4]/button')
        # is_match_popup_btn = self.driver.find_element_by_id('u-1959572593').is_displayed()
        # is_match_popup_btn = self.driver.find_element_by_xpath('//*[@id="u-1959572593"]/div/div/div[1]/div/div[4]/button/svg').is_displayed()
        #is_match_popup_btn = self.driver.find_element_by_css_selector("#u-1959572593>div>div>div.CenterAlign.M\(a\).Expand.Pos\(r\).Fx\(\$flx1\)>div>div.Pos\(a\).T\(0\).P\(20px\).P\(12px\)--xs.End\(0\)>button>svg")
        # match_popup_btn = self.driver.find_element_by_xpath('//*[@id="u-1959572593"]/div/div/div[1]/div/div[4]/button')
        # is_match_popup_btn = self.driver.execute_script("arguments[0].click();", match_popup_btn)
        
        # try:
        #     sleep(5)
        #     match_popup_btn = self.driver.find_elements_by_xpath('//*[@id="u-1959572593"]/div/div/div[1]/div/div[4]/button')
        #     if match_popup_btn:
        #         match_popup_btn.click()
        #     else:
        #         self.auto_swipe()
        # except Exception:
        #     print("Something went wrong in close_match()")
        
        match_popup_btn = self.driver.find_element_by_xpath('//*[@id="u-1959572593"]')
        if match_popup_btn:
            is_match_popup_btn = self.driver.find_element_by_xpath('//*[@id="u-1959572593"]/div/div/div[1]/div/div[4]/button')
            if is_match_popup_btn:
                is_match_popup_btn.click()
                print("close button is clicked!")
            else:
                print("close button is not shown")
                sys.exit()
        else:
            print("ID:u-1959572593 is not shown")
            sys.exit()
            
            
        #//*[@id="u-1959572593"]/div/div/div[1]/div/div[4]/button
        # match_popup_btn = self.driver.find_element_by_xpath('//button[@aria-label="Close"]/svg[@class="Sq(24px) P(4px)and text()="Enable"]')
        # match_popup_btn = self.driver.find_element_by_id('u-1959572593')
        # match_popup_btn = self.driver.find_elements_by_xpath('//*[@id="u-1959572593"]/div/div/div[1]/div/div[4]/button').get_attribute("innerHTML")
        # match_popup_btn = self.driver.find_element_by_xpath('//*[@id="u-1959572593"]/div/div/div[1]/div/div[4]/button/svg')
        # match_popup_btn = self.driver.find_element_by_class_name('Sq(24px) P(4px)')
        # match_popup_btn = self.driver.find_element_by_css_selector('svg.Sq(24px)')
        # match_popup_btn = self.driver.find_element_by_xpath('//*[@id="u-1959572593"]/div/div/div[1]/div/div[4]')
        
                
        
        
        
bot = TinderBot()
bot.login()
bot.auto_swipe()

""" 
            In the console
            while True:
                sleep(2)
                try:
                    like_btn.click()
                except Exception:
                    sleep(2)
                    match_popup_btn = bot.driver.find_element_by_xpath('//*[@id="u-1959572593"]/div/div/div[1]/div/div[4]/button')
                    sleep(2)
                    match_popup_btn.click()
                    
            bot.driver.get("https://tinder.com/app/recs")
"""
                
            
    
    
        